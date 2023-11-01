import string
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup

# [CODE 1-1]
def Naver_news_link_Crowling_joongang():
    jsonResult = []
    cnt, tcnt = 0, 0
    Naver_news_URL = "https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2022.01.01&de=2022.06.12&docid=&related=0&mynews=1&office_type=1&office_section_code=1&news_office_checked=1025&nso=so%3Ar%2Cp%3Afrom20220101to20220612&is_sug_officeid=0"
    wd_op = webdriver.ChromeOptions()
    
    # 웹드라이버 설정
    wd_op.add_argument("--incognito")
    wd_op.add_argument("--headless")
    wd_op.add_argument("--no-sandbox")
    wd_op.add_argument("--disable-setuid-sandbox")
    wd_op.add_argument("--disable-dev-shm-usage")
    wd_op.add_experimental_option('chromedriver', ['enable-logging'])
    
    # 웹드라이버 호출 (현재 버전 102.x)
    wd = webdriver.Chrome(executable_path='C:/Users/user/Documents/인천재능대학교/2학년/AI파이썬머신러닝/WebDriver/chromedriver.exe')
    
    # '코로나' 관련 뉴스 페이지 호출 (중앙일보, 2022.01.01 ~ 2022.06.xx)
    wd.get(Naver_news_URL)
    time.sleep(2)
    
    while True:
        # refresh 될 때마다 html 태그를 가져온다
        # soup = BeautifulSoup(wd.page_source, 'html.parser')
                
        # 한 페이지 당 존재하는 페이징 수? 카운트
        news_titles = wd.find_elements_by_css_selector(".news_tit")
        news_contents = wd.find_elements_by_css_selector(".api_txt_lines")
        for news_num in news_contents:
            # 원래 title도 반복문을 돌려서 출력시키려 했지만 index가 고정되어버려서 아래처럼 바꿨다
            title = news_titles[tcnt].text
            content = news_num.text
            href = news_num.get_attribute('href')
            print("{ 순서 :", cnt, "\n제목 :", title, "\n내용: ", content, "\n주소: ", href, " }")
            jsonResult.append({"cnt":cnt, "title":title, "content":content , "href":href})
            cnt += 1
            tcnt += 1
        if tcnt >= 9:
            tcnt = 0
        
        # next 요소 위치 
        btn_next = wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]') 
        
        # 한 페이지당 주소를 크롤링 한 후, next 활성화 여부            
        if btn_next.get_attribute('aria-disabled') == "false":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            # 만약 next 버튼이 활성화 되어있다면 클릭...
            wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]').click()
        # next 페이지가 비활성화 되어있으면 리스트 저장을 종료  
        elif btn_next.get_attribute('aria-disabled') == "true":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            print("존재하는 페이지가 없으므로 종료합니다.")
            break
        # 예외적인 사항은 모르겠으나 오류로 강제 종료 시킴
        else:
            print("알수없는 오류")
            break
        
    return jsonResult, cnt

# [CODE 1-2]
def Naver_news_link_Crowling_kukmin(cnt):
    jsonResult = []
    tcnt = 0
    cnt += 1
    Naver_news_URL = "https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2022.01.01&de=2022.06.12&docid=&related=0&mynews=1&office_type=1&office_section_code=1&news_office_checked=1005&nso=so%3Ar%2Cp%3Afrom20220101to20220612&is_sug_officeid=0"
    wd_op = webdriver.ChromeOptions()
    
    # 웹드라이버 설정
    wd_op.add_argument("--incognito")
    wd_op.add_argument("--headless")
    wd_op.add_argument("--no-sandbox")
    wd_op.add_argument("--disable-setuid-sandbox")
    wd_op.add_argument("--disable-dev-shm-usage")
    wd_op.add_experimental_option('chromedriver', ['enable-logging'])
    
    # 웹드라이버 호출 (현재 버전 102.x)
    wd = webdriver.Chrome(executable_path='C:/Users/user/Documents/인천재능대학교/2학년/AI파이썬머신러닝/WebDriver/chromedriver.exe')
    
    # '코로나' 관련 뉴스 페이지 호출 (국민일보, 2022.01.01 ~ 2022.06.xx)
    wd.get(Naver_news_URL)
    time.sleep(2)
    
    while True:
        # 한 페이지 당 존재하는 페이징 수? 카운트
        news_titles = wd.find_elements_by_css_selector(".news_tit")
        news_contents = wd.find_elements_by_css_selector(".api_txt_lines")
        for news_num in news_contents:
            title = news_titles[tcnt].text
            content = news_num.text
            href = news_num.get_attribute('href')
            print("{ 순서 :", cnt, "\n제목 :", title, "\n내용: ", content, "\n주소: ", href, " }")
            jsonResult.append({"cnt":cnt, "title":title, "content":content , "href":href})
            cnt += 1
            tcnt += 1
        if tcnt >= 9:
            tcnt = 0

        
        # next 요소 위치 
        btn_next = wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]') 
        
        # 한 페이지당 주소를 크롤링 한 후, next 활성화 여부            
        if btn_next.get_attribute('aria-disabled') == "false":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            # 만약 next 버튼이 활성화 되어있다면 클릭...
            wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]').click()
        # next 페이지가 비활성화 되어있으면 리스트 저장을 종료  
        elif btn_next.get_attribute('aria-disabled') == "true":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            print("존재하는 페이지가 없으므로 종료합니다.")
            break
        # 예외적인 사항은 모르겠으나 오류로 강제 종료 시킴
        else:
            print("알수없는 오류")
            break
        
    return jsonResult, cnt

# [CODE 1-3]
def Naver_news_link_Crowling_donga(cnt):
    jsonResult = []
    tcnt = 0
    cnt += 1
    Naver_news_URL = "https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2022.01.01&de=2022.06.12&docid=&related=0&mynews=1&office_type=1&office_section_code=1&news_office_checked=1020&nso=so%3Ar%2Cp%3Afrom20220101to20220612&is_sug_officeid=0"
    wd_op = webdriver.ChromeOptions()
    
    # 웹드라이버 설정
    wd_op.add_argument("--incognito")
    wd_op.add_argument("--headless")
    wd_op.add_argument("--no-sandbox")
    wd_op.add_argument("--disable-setuid-sandbox")
    wd_op.add_argument("--disable-dev-shm-usage")
    wd_op.add_experimental_option('chromedriver', ['enable-logging'])
    
    # 웹드라이버 호출 (현재 버전 102.x)
    wd = webdriver.Chrome(executable_path='C:/Users/user/Documents/인천재능대학교/2학년/AI파이썬머신러닝/WebDriver/chromedriver.exe')
    
    # '코로나' 관련 뉴스 페이지 호출 (동아일보, 2022.01.01 ~ 2022.06.xx)
    wd.get(Naver_news_URL)
    time.sleep(2)
    
    while True:
        # 한 페이지 당 존재하는 페이징 수? 카운트
        news_titles = wd.find_elements_by_css_selector(".news_tit")
        news_contents = wd.find_elements_by_css_selector(".api_txt_lines")
        for news_num in news_contents:
            title = news_titles[tcnt].text
            content = news_num.text
            href = news_num.get_attribute('href')
            print("{ 순서 :", cnt, "\n제목 :", title, "\n내용: ", content, "\n주소: ", href, " }")
            jsonResult.append({"cnt":cnt, "title":title, "content":content , "href":href})
            cnt += 1
            tcnt += 1
        if tcnt >= 9:
            tcnt = 0

        
        # next 요소 위치 
        btn_next = wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]') 
        
        # 한 페이지당 주소를 크롤링 한 후, next 활성화 여부            
        if btn_next.get_attribute('aria-disabled') == "false":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            # 만약 next 버튼이 활성화 되어있다면 클릭...
            wd.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/a[2]').click()
        # next 페이지가 비활성화 되어있으면 리스트 저장을 종료  
        elif btn_next.get_attribute('aria-disabled') == "true":
            print("다음 페이지 여부 : ", btn_next.get_attribute('aria-disabled'))
            print("존재하는 페이지가 없으므로 종료합니다.")
            break
        # 예외적인 사항은 모르겠으나 오류로 강제 종료 시킴
        else:
            print("알수없는 오류")
            break
        
    return jsonResult

#[CODE 0]
def main():
    jsonResult = []
    # 중앙일보, 국민일보, 동아일보
    joongang_jsonResult, cnt = Naver_news_link_Crowling_joongang()
    kukmin_jsonResult, cnt = Naver_news_link_Crowling_kukmin(cnt)
    donga_jsonResult = Naver_news_link_Crowling_donga(cnt)
    
    with open('./joongang_News_links.json', 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(joongang_jsonResult, indent=2, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
        
    with open('./kukmin_News_links.json', 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(kukmin_jsonResult, indent=2, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
        
    with open('./donga_News_links.json', 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(donga_jsonResult, indent=2, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    
    # 리스트를 풀고 jsonResult 안에 값을 집어넣음
    for dict in joongang_jsonResult:
        jsonResult.append(dict)
    for dict in kukmin_jsonResult:
        jsonResult.append(dict)
    for dict in donga_jsonResult:
        jsonResult.append(dict)
    
    with open('./News_links.json', 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=2, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
        
if __name__ == '__main__':
    main()