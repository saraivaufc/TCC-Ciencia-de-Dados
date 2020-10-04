import logging
import os
import argparse
from datetime import datetime
from time import sleep

import pandas as pd
from selenium import webdriver

from config import LOGIN_URL, STATIONS_CODES, STATIONS_DATA_HTML, \
    URL_TEMPLATES

def login(email, password):
    browser = webdriver.Chrome("geckodriver.exe")
    browser.get(LOGIN_URL)
    sleep(10)
    emailElement = browser.find_element_by_name("mCod")
    emailElement.send_keys(email)
    passElement = browser.find_element_by_name("mSenha")
    passElement.send_keys(password)
    passElement.submit()
    return browser


if __name__ == "__main__":
    # Initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--template",
        help="options: HOUR, DAY, DAYFULL and MONTH", required=False,
        default="DAYFULL")
    parser.add_argument("--start_date",
        help="format: dd/mm/yyyy", required=True,
        default="01/01/1961")
    parser.add_argument("--end_date",
        help="format: dd/mm/yyyy", required=False,
        default=datetime.now().strftime("%d/%m/%Y"))
    parser.add_argument("--email",
        help="format: username@email.com", required=True)
    parser.add_argument("--password",
        help="format: xxxxxxx", required=True)

    # Read arguments from the command line
    args = parser.parse_args()

    url_template = URL_TEMPLATES.get(args.template)
    start_date = args.start_date
    end_date = args.end_date
    email = args.email
    password = args.password

    browser = login(email=email, password=password)

    logging.basicConfig(filename='crawler.log', level=logging.INFO)

    stations_df = pd.read_csv(STATIONS_CODES, sep=";")

    if not os.path.exists(STATIONS_DATA_HTML):
        os.makedirs(STATIONS_DATA_HTML)

    for index, row in stations_df.iterrows():
        data = dict(zip(stations_df.columns, row.get_values()))
        name = data.get("name")
        code = data.get("code")

        filename = "{folder}{sep}{code}.html".format(
            folder=STATIONS_DATA_HTML,
            sep=os.sep,
            code=code)

        if not os.path.exists(filename):
            print(filename)

            logging.info('%s (%s): Crawling... ' % (name, code))

            url = url_template.get("URL").format(code=code,
                                                 start_date=start_date,
                                                 end_date=end_date)

            browser.get(url)

            f = open(filename, "w+")
            f.write(browser.page_source)
            f.close()

            logging.info('%s (%s): End of this station ...  ' % (code, name))
