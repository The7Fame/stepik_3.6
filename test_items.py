from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser):
  browser.get(link)
  button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary').get_attribute('value')
  print(len(button))
  assert len(button) > 0, 'Add to cart button not found. (Кнопка добавления в корзину не найдена)'