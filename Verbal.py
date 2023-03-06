from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time
# C:\Users\Shinken\AppData\Local\Google\Chrome\User Data\Default
options = Options()
options.add_argument(r"user-data-dir=C:\Users\Shinken\AppData\Local\Google\Chrome\User Data\Default")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
  })
driver = webdriver.Chrome(service=Service(r'C:\Users\Shinken\Documents\BETA\chromedriver_win32\chromedriver.exe'), options=options)
driver.get('https://dictation.io/speech')
driver.minimize_window()
select = Select(driver.find_element("xpath", "//select[@id='lang']"))
select.select_by_value('pl-pl')
time.sleep(1)
driver.find_element("xpath", "//a[@class='btn-mic btn btn--primary-1']").click()
time.sleep(4)
textbox = driver.find_element("xpath", "//div[@class='ql-editor ql-blank']")
while True:
    if textbox.text != '':
        if textbox.text.strip() == 'koniec':
            driver.quit()
            print('Koniec1')
        print(textbox.text)
        textbox.clear()

#driver.quit()