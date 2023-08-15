from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os.path
import pandas as pd

def sendImage(phone, name):

      url = 'https://web.whatsapp.com/send?phone=+91'+str( phone)
      browser.get(url)
      print (name )
      file_to_open = os.path.join(data_folder, "sample.jpg")
      sleep(1.5)
      try:
            try:
                  alert = browser.switch_to.alert
                  alert.accept()
            
            except Exception as e : 
                  print('No alert')
      
            try:

                  attachment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@title = 'Attach']")))
                  attachment_box = browser.find_element(By.XPATH, "//div[@title = 'Attach']")
                  sleep(0.2)
                  attachment_box.click()
                  sleep(0.2)

                  image_box = browser.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                  image_box.send_keys(file_to_open)
                  sleep(0.4)
                  
                  final_text = sample_text.format(name)
                  text_field = browser.find_element(By.XPATH,  "//p[@class='selectable-text copyable-text iq0m558w']")
                  text_field.send_keys(final_text)

                  sleep(0.4)
                  send_button = browser.find_element(By.XPATH, "//div[@class='g0rxnol2']")
                  send_button.click()
                  sleep(0.5)

            except Exception as e:
                  print(e)
                  print("Sorry message could not sent to ONCE " )

      except Exception as e:
            print("Sorry message could not sent to " )


filedirectory = os.getcwd()
data_folder = os.path.join(filedirectory, "Image")

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://web.whatsapp.com/')

df = pd.read_excel('Test1.xlsx')
mylist = df['Name'].tolist()
phonelist = df['phone'].tolist()

sample_text = "Hello {} , I`m Riya, I hope you`ve heard about the upcoming institute elections. I`m writing to you because one of my friend, *Rishav Kumar* , is running for General Secretary of Hostel Affairs[GSHA]. He was previously ISHA and through his dedication was able to bring  CCD, re-tendered 7 Messes accross Institute and is playing a major role in digitalising Hospital. Click on the link shorturl.at/dkBPX to know more about the candidate.  Please cast your vote to *Rishav Kumar* as next GSHA"

input('Enter anything after scanning QR code')

for i in range(2):
      sleep(0.5)
      sendImage(phonelist[i], mylist[i])

input('Enter anything to close the window')
