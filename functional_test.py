# 기능 테스트를 담고 있는 파일.
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # source ~/.bash_profile을 해주지 않으면 다음 에러 발생. selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
        self.browser.implicitly_wait(3)  # 암묵적 대기

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')  # runserver를 하지 않으면 이 지점에서 에러가 발생함.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # assert 'Django' in browser.title  # 현재의 스타팅 페이지 타이틀에는 Django가 들어있지 않아 아래와 같이 테스트를 진행함.
        # assert 'congratulation' in browser.title.lower(), f"Browser title was {browser.title}"


if __name__ == '__main__':
    unittest.main(warnings='ignore')
