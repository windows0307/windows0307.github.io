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

acmenu = driver.find_element_by_link_text("My Account").click()
email = driver.find_element_by_id("reg_email")
email.send_keys("test@email.com")
password = driver.find_element_by_id("reg_password")
password.send_keys("SomeHardPassword123!@#!@#")
regbtn = driver.find_element_by_name("register").click()
driver.quit()

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

acmenu = driver.find_element_by_link_text("My Account").click()
uname = driver.find_element_by_id("username")
uname.send_keys("test@email.com")
password = driver.find_element_by_id("password")
password.send_keys("SomeHardPassword123!@#!@#")
logbtn = driver.find_element_by_name("login").click()
driver.quit()



# Покупка товара
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

shop = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
htmlbook = driver.find_element_by_css_selector(".post-182 .add_to_cart_button").click()
time.sleep(5)
content = driver.find_element_by_class_name("wpmenucart-contents").click()
cbtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Maxim")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Logan")
email = driver.find_element_by_id("billing_email")
email.send_keys("mynewpost@gmail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89876543211")
country = driver.find_element_by_id("s2id_billing_country").click()
country_poisk = driver.find_element_by_id("s2id_autogen1_search")
country_poisk.send_keys("Christmas Island")
country_en = driver.find_element_by_class_name("select2-match").click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("The Wall")
city = driver.find_element_by_id("billing_city")
city.send_keys("Lockmyfase")
state = driver.find_element_by_id("billing_state")
state.send_keys("lubov")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("111111111")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_id("payment_method_cheque").click()
place = driver.find_element_by_id("place_order").click()
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
                                     "Thank you. Your order has been received."))
payment = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()