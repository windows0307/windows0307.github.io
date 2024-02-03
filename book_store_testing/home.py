from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

popup_selector = '.fc-dialog.fc-choice-dialog[role="dialog"]'

try:
    popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, popup_selector))
    )
    # Если всплывающее окно появилось, закрываем его
    do_not_consent_button = driver.find_element(By.CSS_SELECTOR, 'button.fc-cta-do-not-consent')
    do_not_consent_button.click()

except TimeoutException:

    print("Всплывающее окно не появилось, выполняем другие действия или просто продолжаем")

driver.execute_script("window.scrollBy(0, 600);")
read_more_btn = driver.find_element_by_css_selector(".post-160 > a > h3").click()
reviews_btn = driver.find_element_by_css_selector(".reviews_tab > a").click()
five = driver.find_element_by_css_selector(".star-5").click()
your_review_field = driver.find_element_by_id("comment")
your_review_field.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Test_Name")
email = driver.find_element_by_id("email")
email.send_keys("test@email.com")
submit = driver.find_element_by_id("submit").click()
driver.quit()
