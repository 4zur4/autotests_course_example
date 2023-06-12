# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = "https://sbis.ru/"
tensor_site = "https://tensor.ru/"
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get(sbis_site)
    sleep(2)
    contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']")
    contacts.click()
    sleep(2)
    tensor_banner = driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    tensor_banner.click()
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    assert driver.current_url == tensor_site, "Открыт неверный сайт"
    news_pip = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content " ".tensor_ru-Index__card-title")
    assert news_pip.text == "Сила в людях", "Новость отсутствует"
    driver.execute_script("return arguments[0].scrollIntoView(true);", news_pip)
    sleep(2)
    about = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    about_link = about.get_attribute('href')
    about.click()
    assert driver.current_url == about_link, "Неверная ссылка"
    sleep(2)

finally:
    driver.quit()
