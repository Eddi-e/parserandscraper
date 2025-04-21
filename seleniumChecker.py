from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time

#first step given link get score, num of ratings, num of reviews, title cover
def getstats(isbn_of_book):
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.goodreads.com/search")


        time.sleep(1)

        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print("hello0")
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        #body1 = driver.find_element(By.TAG_NAME, "body")
        #body1.send_keys(Keys.ESCAPE)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".searchBox__input.searchBox__input--navbar")))
        search = driver.find_element(By.CSS_SELECTOR,".searchBox__input.searchBox__input--navbar")
        print("hello1")
        search.send_keys(isbn_of_book)
        print("hello2")
        try:
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".searchBox__icon--magnifyingGlass.gr-iconButton.searchBox__icon.searchBox__icon--navbar")))
            element.click()
        except Exception as e:
            print(type(e).__name__)

        print("hello3")
        
    #   bookpage = driver.find_element(By.CLASS_NAME,"bookTitle")
    #  linktobookpage = bookpage.get_attribute('href')
    # driver.get(linktobookpage)

        try:
            wait = WebDriverWait(driver, 5)
            print("here")
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__close .gr-iconButton")))
            print("here1")
            button.click()
    #   except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException) as e:
        except Exception as e:
            print("partial close button not clickable:",type(e).__name__, e)

        
        try:
            wait1 = WebDriverWait(driver, 5)
            close_button = wait1.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.Overlay__close .Button')))
            close_button.click()
        except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException) as e:
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            print("Close button not clickable:",type(e).__name__, e)

        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print("hello4")
        
        #]WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "RatingStatistics__rating")))



        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "RatingStatistics__rating")))
        ratings = driver.find_element(By.CLASS_NAME,"RatingStatistics__rating")
        ratingsmeta = driver.find_element(By.CLASS_NAME,"RatingStatistics__meta")
        ratingsnumber = ratingsmeta.find_element(By.XPATH,"./span[1]")
        reviewnumber = ratingsmeta.find_element(By.XPATH,"./span[2]")
        list_to_return = [ratings.text]
        list_to_return.append(int(ratingsnumber.text.split(' ')[0].replace(',','')))
        list_to_return.append(int(reviewnumber.text.split(' ')[0].replace(',','')))
        driver.quit()
        return(list_to_return)
    except:
        driver.quit()
        driver.save_screenshot('screenie.png')
        raise Exception("")

if __name__ == "__main__":
    name = "1517646669"
    print(getstats(name))
