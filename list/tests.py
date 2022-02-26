from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from list.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # 뷰를 위한 테스트를 작성할 때는 단순히 빈 함수를 작성하는 것이 아니라 HTML 형식의 실제 응답을 반환하는 함수를 작성해야 한다.
    # TODO 이 테스트는 문제가 있다... 나중에 고치던가 해야함.
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request=request)
        print(response.content.decode())
        print(expected_html)
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'home.html', {'new_item_text': '신규 작업 아이템'}
        )
        self.assertEqual(response.content.decode(), expected_html)

