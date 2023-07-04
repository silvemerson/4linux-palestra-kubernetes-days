import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class AllTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor="http://192.168.88.10:4444/wd/hub", desired_capabilities = DesiredCapabilities.FIREFOX)

    def tearDown(self):
      self.driver.close()

    def test_user_can_loging(self):
        self.driver.get("http://192.168.88.30:5000")
        self.driver.find_element_by_id("name").send_keys("devops")
        self.driver.find_element_by_id("password").send_keys("qwe123qwe")
        self.driver.find_element_by_id("loginbutton").click()
        print(self.driver.current_url)
        self.assertIn('http://192.168.88.30:5000/courses', self.driver.current_url)
        assert "No results found." not in self.driver.page_source

if __name__ == "__main__":
    unittest.main(warnings='ignore')

