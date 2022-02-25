# 기능 테스트를 담고 있는 파일.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # source ~/.bash_profile을 해주지 않으면 다음 에러 발생. selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
        self.browser.implicitly_wait(3)  # 암묵적 대기

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')  # runserver를 하지 않으면 이 지점에서 에러가 발생함.

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  # find_element_by_*는 deprecated라고 함. 나중에 이것들 다 바꿔줘야함.
        # header_text = self.browser.find_element('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # "공작깃털 사기"라고 텍스트 상자에 입력
        inputbox.send_keys('공작깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 "1: 공작깃털 사기" 아이템이 추가됨.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows)
        )

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다
        self.fail('Finish the test')

        # 페이지는 다시 갱신되고, 두 개의 아이템이 목록에 보인다

        # assert 'Django' in 다rowser.title  # 현재의 스타팅 페이지 타이틀에는 Django가 들어있지 않아 아래와 같이 테스트를 진행함.
        # assert 'congratulation' in browser.title.lower(), f"Browser title was {browser.title}"


if __name__ == '__main__':
    unittest.main(warnings='ignore')
