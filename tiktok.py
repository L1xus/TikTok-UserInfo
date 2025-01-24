from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from bs4 import BeautifulSoup

from datetime import datetime
import time
start_time = datetime.now()

def get_comments_html(reel):
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.set_window_size(1920, 1080)
    wait = WebDriverWait(browser, 30)
    comments = []

    try:
        print(reel)
        browser.get(reel)

        try:
            wait.until(EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'css-1npmxy5-DivActionItemContainer er2ywmz0')]")
            ))
            try:
                comments_button = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/button[2]")
                ))
                browser.execute_script("arguments[0].scrollIntoView(true);", comments_button)
                browser.execute_script("arguments[0].click()", comments_button)
                print(comments_button.text)
                print("Clicked on the comments button.")
            except TimeoutException:
                print("Comments button not found or not clickable.")

        except TimeoutException:
            pass

    finally:
        browser.quit()
        
    return comments

test = get_comments_html('https://www.tiktok.com/@hidiralikaya/video/7246476904365133062')
print(test)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
