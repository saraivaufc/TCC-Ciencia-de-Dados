import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pathlib import Path

home = str(Path.home())

LABMET_WEBSITE = 'http://labmet.univasf.edu.br/joomla/index.php/dados-climaticos'
DOWNLOAD_DIR = home + os.sep + 'labmet_downloads'

if not os.path.exists(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)

print("Downloading to " + DOWNLOAD_DIR)

profile = FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.manager.showAlertOnComplete", False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,application/octet-stream,application/x-zip-compressed,multipart/x-zip,application/x-rar-compressed, application/octet-stream,application/msword,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/rtf,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,application/vnd.ms-word.document.macroEnabled.12,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/xls,application/msword,text/csv,application/vnd.ms-excel.sheet.binary.macroEnabled.12,text/plain,text/csv/xls/xlsb,application/csv,application/download,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/octet-stream')
profile.set_preference("browser.download.dir", DOWNLOAD_DIR)

browser = webdriver.Firefox(executable_path='geckodriver.exe', firefox_profile=profile)
browser.get(LABMET_WEBSITE)

table = browser.find_element_by_tag_name('table')
elements = table.find_elements_by_tag_name('a')
print(len(elements))
for element in elements:
    if element.text.find('.xls') != -1:
        element.click()