import os

import pandas as pd
from config import STATIONS_CODES, STATIONS_DATA_HTML, STATIONS_DATA_CSV
from lxml import html

if __name__ == "__main__":
    stations_df = pd.read_csv(STATIONS_CODES, sep=";")

    stations_details = {
        "name": [],
        "code": [],
        "latitude": [],
        "longitude": [],
        "altitude": [],
        "status_operation": [],
        "start_operation": []

    }

    for index, row in stations_df.iterrows():
        data = dict(zip(stations_df.columns, row.get_values()))
        name = data.get("name")
        code = data.get("code")

        if not os.path.exists(STATIONS_DATA_CSV):
            os.makedirs(STATIONS_DATA_CSV)

        input_filename = "{folder}{sep}{code}.html".format(
            folder=STATIONS_DATA_HTML,
            sep=os.sep,
            code=code)

        output_filename = "{folder}{sep}{code}.csv".format(
            folder=STATIONS_DATA_CSV,
            sep=os.sep,
            code=code)

        if os.path.exists(input_filename) and not os.path.exists(
                output_filename):
            print(input_filename)
            station_rawdata = html.fromstring(open(input_filename, 'r').read())

            content = station_rawdata.xpath("//body/pre")[
                0].text_content().split("--------------------\n")

            header = content[2]

            full_name, full_code = header.split("\n")[0].replace(
                "Estação           :", "").replace(")", "").split("(OMM:")
            full_name = full_name.strip()
            full_code = int(full_code.strip())
            latitude = float(
                header.split("\n")[1].replace("Latitude  (graus) :",
                                              "").strip())
            longitude = float(
                header.split("\n")[2].replace("Longitude (graus) :",
                                              "").strip())
            altitude = float(
                header.split("\n")[3].replace("Altitude  (metros):",
                                              "").strip())
            status_operation = header.split("\n")[4]
            start_operation = header.split("\n")[5].replace(
                "Inicio de operação:", "").strip()

            stations_details["name"].append(full_name)
            stations_details["code"].append(full_code)
            stations_details["latitude"].append(latitude)
            stations_details["longitude"].append(longitude)
            stations_details["altitude"].append(altitude)
            stations_details["status_operation"].append(status_operation)
            stations_details["start_operation"].append(start_operation)

            body = content[-1].replace("VelocidadeVentoInsolacao",
                                       "VelocidadeVento;Insolacao")

            with open(output_filename, "w+") as f:
                f.write(body)
        else:
            print("File {input_filename} not found!!!".format(
                input_filename=input_filename))

    df = pd.DataFrame(stations_details)

    # saving the dataframe
    df.to_csv(STATIONS_CODES, index=False, sep=";")
