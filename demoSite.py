from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="D:\\downloads\\chromedriver.exe")
baseUrl= "https://demosite.executeautomation.com/index.html"

class Demo():
    def test(self):
     driver.get(baseUrl)
    
     initial= driver.find_element(By.NAME, "Initial")
     initial.send_keys("Initial ceva")

     firstname= driver.find_element(By.NAME,"FirstName")
     firstname.send_keys("Numarul 1")

     middlename= driver.find_element(By.NAME,"MiddleName")
     middlename.send_keys("Valoare")

     title= Select(driver.find_element(By.NAME, "TitleId"))
     title.select_by_visible_text("Mr.")

     female= driver.find_element(By.NAME,"Female")
     female.click()

     man=driver.find_element(By.NAME,"Male")
     man.click()
     
     english= driver.find_element(By.NAME,"english")
     english.click()

     hindi= driver.find_element(By.NAME,"Hindi")
     hindi.click()

     link=driver.find_element_by_link_text("HtmlPopup")
     link.click()

     handles = driver.window_handles

     #handles[0]
     #handles[1]

     driver.switch_to_window(handles[1])
     initial= driver.find_element(By.NAME, "Initial")
     initial.send_keys("Initial ceva 2")

     time.sleep(5)

testare= Demo()
testare.test()
driver.quit()