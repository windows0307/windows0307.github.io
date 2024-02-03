#TEST-1

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

acmenu = driver.find_element_by_link_text("My Account").click()
uname = driver.find_element_by_id("username")
uname.send_keys("test@email.com")
password = driver.find_element_by_id("password")
password.send_keys("SomeHardPassword123!@#!@#")
logbtn = driver.find_element_by_name("login").click()
shop_tab = driver.find_element_by_link_text("Shop").click()
html_5_forms_book = driver.find_element_by_css_selector(".post-181 > a > h3").click()
booktitle = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))
driver.quit()

#TEST -2 количество товаров в категории
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

acmenu = driver.find_element_by_link_text("My Account")
acmenu.click()
uname = driver.find_element_by_id("username")
uname.send_keys("test@email.com")
password = driver.find_element_by_id("password")
password.send_keys("SomeHardPassword123!@#!@#")
logbtn = driver.find_element_by_name("login").click()
shop_tab = driver.find_element_by_link_text("Shop").click()
category = driver.find_element_by_link_text("HTML").click()
itcount = driver.find_elements_by_css_selector("a > h3")
if len(itcount) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка. Отображается другое количество, а именно: " + str(len(itcount)))
driver.quit()



# Shop: сортировка товаров

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
shop_tab = driver.find_element_by_link_text("Shop").click()
items_1 = driver.find_element_by_name("orderby")
items_2 = items_1.get_attribute("value")
if items_2 == "menu_order":
    print("Успешно, по умолчанию")
else:
    print("Ошибка, не по умолчанию")
select = Select(items_1)
select.select_by_value("price-desc")
items_1 = driver.find_element_by_name("orderby")
items_1_less = items_1.get_attribute("value")
if items_1_less == "price-desc":
    print("Успешно, по убыванию")
else:
    print("Ошибка, не по убыванию")
driver.quit()


#Shop: отображение, скидка товара


from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
android_quick_start_book = driver.find_element_by_css_selector(".post-169 h3")
android_quick_start_book.click()
priceold = driver.find_element_by_css_selector(".price > del > span")
priceold_text = priceold.text
pricenew = driver.find_element_by_css_selector(".price > ins > span")
pricenew_text = pricenew.text
assert priceold_text == "₹600.00"
assert pricenew_text == "₹450.00"
book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a"))).click()

book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
driver.quit()


#Shop: проверка цены в корзине

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 > a h3").click()
html5_webapp_development_book_add_btn = driver.find_element_by_css_selector(".single_add_to_cart_button").click()
content = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
content_text = content.text
assert content_text == "1 Item"
priceval = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
priceval_text = priceval.text
assert priceval_text == "₹180.00"
contentbattn = driver.find_element_by_class_name("wpmenucart-contents").click()
subtotal_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
total_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))
driver.quit()


# Shop: работа в корзине

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

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

shop_tab = driver.find_element_by_link_text("Shop").click()

driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button").click()
time.sleep(5)
html5_book = driver.find_element_by_css_selector(".post-169 .add_to_cart_button").click()
contentbattn = driver.find_element_by_class_name("wpmenucart-contents").click()
time.sleep(5)
removeiten = driver.find_element_by_class_name("remove").click()
undo = driver.find_element_by_link_text("Undo?").click()
field1 = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
field1.clear()
field1.send_keys("3")
update = driver.find_element_by_name("update_cart").click()
field1 = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
field1_value = field1.get_attribute("value")
assert field1_value == '3'
time.sleep(5)
apply = driver.find_element_by_name("apply_coupon").click()
mes_err = driver.find_element_by_css_selector(".woocommerce-error")
mes_err_text = mes_err.text
assert mes_err_text == 'Please enter a coupon code.'
driver.quit()
