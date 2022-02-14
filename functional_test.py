from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')  # runserver를 하지 않으면 이 지점에서 에러가 발생함. 

# assert 'Django' in browser.title  # 현재의 스타팅 페이지 타이틀에는 Django가 들어있지 않아 아래와 같이 테스트를 진행함. 
assert 'congratulation' in browser.title.lower()