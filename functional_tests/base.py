# 기능 테스트를 담고 있는 파일.
import os
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server_url = os.environ.get('URL', cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome()  # source ~/.bash_profile을 해주지 않으면 다음 에러 발생. selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
        self.browser.implicitly_wait(3)  # 암묵적 대기

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')



