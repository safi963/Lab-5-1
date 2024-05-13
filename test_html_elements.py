from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import unittest

class TestContacts(unittest.TestCase):
    def setUp(self):
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Ensures the browser window does not open
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_number_guessing_game(self):
        driver = self.driver
        driver.get("http://10.48.10.187")  # Replace with your target website

        # Check for the presence of the game elements
        assert "Guess a number between 1 and 100" in driver.page_source
        assert driver.find_element(By.ID, "guessInput")
        assert driver.find_element(By.ID, "guessButton")
        assert driver.find_element(By.ID, "result")

        print("Test completed successfully. Number Guessing Game elements were verified.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
        print("Test completed successfully. All 10 test contacts were verified.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
