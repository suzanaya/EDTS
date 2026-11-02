from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password")

# alternatif yang lebih stabil untuk test
# USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test='username']")
# PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")

driver.find_element(*USERNAME_INPUT).send_keys("standard_user")
driver.find_element(*PASSWORD_INPUT).send_keys("secret_sauce")