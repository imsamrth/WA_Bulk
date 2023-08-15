from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os.path
import pandas as pd

def sendImage(phone, name):
      #span_name = "//span[@title = '"+name+"']"
      #print(span_name)
      #user = browser.find_element(By.XPATH,span_name )
      #user.click()

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
                  #print(file_to_open)
                  attachment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@title = 'Attach']")))


            # WebDriverWait(driver, 7, poll_frequency=5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
            #alertFound = datetime.now()
            # WebDriverWait wait = new WebDriverWait(driver, 20);
            #wait.until(ExpectedConditions.elementToBeClickable(lastElementToLoad));
            #current_time_alertFound = alertFound.strftime("%H:%M:%S")
            #attachment_box  = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(By.XPATH, "//div[@title = 'Attach']"))
                  #sleep(10)
                  attachment_box = browser.find_element(By.XPATH, "//div[@title = 'Attach']")
                  sleep(0.5)
                  attachment_box.click()
                 # input('Enter anything to READ')
                  image_box = browser.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                  image_box.send_keys(file_to_open)

                  sleep(0.5)
                  #send_button = browser.find_element(By.XPATH, '//span[@data-icon="send"]')

                  final_text = sample_text.format(name)

                  text_field = browser.find_element(By.XPATH,  "//p[@class='selectable-text copyable-text iq0m558w']")
                  text_field.send_keys(final_text)

                  sleep(0.5)
                  #//*[@id = "app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p
                  send_button = browser.find_element(By.XPATH, "//div[@class='g0rxnol2']")
                  #input('Enter anything to send')
                  send_button.click()

                  sleep(1)
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
#mylist = mylist[100:130]
phonelist = df['phone'].tolist()
#phone_list = [int(item) for item in phonelist[1]]
#phone_list = phone_list[0:3]

sample_text = 'Hello {} , I`m Riya, I hope you`ve heard about the upcoming institute elections. I`m writing to you because one of my friend, *Rishav Kumar* , is running for General Secretary of Hostel Affairs[GSHA]. He was previously ISHA and through his dedication was able to bring  CCD, re-tendered 7 Messes accross Institute and is playing a major role in digitalising Hospital. Click on the link shorturl.at/dkBPX to know more about the candidate. Please cast your vote to *Rishav Kumar* as next GSHA'

input('Enter anything after scanning QR code')

for i in range(2):
#for i in range(1):
      sleep(1)
      sendImage(phonelist[i], mylist[i])

input('Enter anything to close the window')
