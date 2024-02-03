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



