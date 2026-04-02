from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import unittest

class TestH5Tag(unittest.TestCase):
    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_h5_tag_content(self):
        driver = self.driver
        driver.get("https://10.48.228.100")

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(driver, 10)
        h5_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h5")))
        h5_text = h5_element.text

        self.assertEqual("Lab 3-6 Works!", h5_text, "The <h5> tag does not contain the text 'Lab 3-6 Works!'")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
