from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    # 1. Akses web
    driver.get("https://www.klikindomaret.com/")

    # 2. Pilih Meta Kategori "Makanan"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Makanan')]"))).click()

    # 3. Pilih kategori "Madu"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Madu')]"))).click()

    # 4. Pilih salah satu produk (produk pertama)
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a[href*='/product/']"))).click()

    # 5. Halaman detail produk terbuka
    wait.until(EC.url_contains("/product/"))

    # 6. Klik "+ Keranjang"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(.,'Keranjang')]"))).click()

    time.sleep(3)
    print("Test selesai")
finally:
    driver.quit()