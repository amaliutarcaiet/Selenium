from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\downloads\\chromedriver.exe")
baseUrl= "http://www.demo.guru99.com/V4/"
username_text ="mngr303507"
password_text ="naqUdat"
class Login():
    
    def tc01_login_succes(self):
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys(username_text)

        password = driver.find_element(By.NAME, "password")
        password.send_keys(password_text)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()
        
        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle =="Guru99 Bank Manager HomePage"):
            print("Test Case T01 Login succes PASS")
        else:
            print("Test Case T01 Login succes FAIL")


    def login_username_maxim_char(self):
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys(username_text+ "gsAGDSABASBAS")

        password = driver.find_element(By.NAME, "password")
        password.send_keys(password_text)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()
        
        time.sleep(5)
        actualTitle = driver.title
        if (actualTitle =="Guru99 Bank Manager HomePage"):
            print("Test Case T10 Login with a username that has characters >10 PASS")
        else:
            print("Test CaseT10 Login with a username that has characters >10 FAIL")
      
    def login_username_NOK_password_OK(self, usernameString, passwordString, testCase):
        driver.get(baseUrl)
         
        if usernameString != "" : 
          username = driver.find_element(By.NAME, "uid")
          username.send_keys(usernameString)

        if passwordString != "" :    
          password = driver.find_element(By.NAME, "password")
          password.send_keys(passwordString)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()
        
        time.sleep(5)

        actualTitle = None
        try:
            actualTitle = driver.title
        except :
            print("Test Case"+ testCase +"PASS")
            
        if actualTitle is not None:
            print("Test Case"+testCase+"FAIL")    

test = Login()
test.tc01_login_succes()
test.login_username_NOK_password_OK(username_text, "NOK", " T02 Login correct user and wrong password-")
test.login_username_NOK_password_OK("NOK", password_text, " T03 Login correct password and wrong user-")
test.login_username_NOK_password_OK("NOK", "NOK", " T04 Login wrong password and wrong user-")
test.login_username_NOK_password_OK("", password_text, " T05 Login empty user and correct password-")
test.login_username_NOK_password_OK("", "NOK", " T06 Login empty user and wrong password-")
test.login_username_NOK_password_OK(username_text, "", " T07 Login correct user and empty password-")
test.login_username_NOK_password_OK("NOK", "", " T08 Login wrong user and empty password-")
test.login_username_NOK_password_OK("", "", " T09 Login empty user and empty password-")
test.login_username_maxim_char()
driver.quit()