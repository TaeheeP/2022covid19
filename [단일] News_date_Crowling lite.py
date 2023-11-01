import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 후처리때문에 느려지는 관계로 하나만 동작하게 함
# [CODE 1-1]
def d_date():
    cnt = 8002
    dcnt = 0
    jsonResult = []
    # 데이터를 가져온다
    with open('./donga_News_links.json', 'r', encoding='utf-8') as nl:
        json_data = json.load(nl) # 리스트 타입
    
    for links in json_data:
        try:
            # links 안에 date가 이미 존재한다면,
            if ('date' in links) and (links['date'] != None):
                print("날짜가 미표시 된 자료 로딩중... : ", cnt)
                cnt += 1
                print("다음 표시 될 번호 :", cnt)
                pass
            # 만약 date에 None이 출력되었거나 요소가 존재하지 않는다면,
            if ('date' not in links) or (links['date'] == '') or (links['date'] == None) or ('글자크기' in links['date']):      
                getdate = getDate(links['href'])
                links['date'] = getdate
                # 실제 파일 n번째에 있는 'date' 에 날짜를 넣는다
                json_data[dcnt]['date'] = getdate
                print("파일 결과 : \n", json_data[dcnt]['date'])
                print("결과 : \n", links)
                # 보험으로 jsonResult 에도 넣는다
                jsonResult.append(links)
                with open('./donga_News_links.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, indent="\t", ensure_ascii=False)
                cnt += 1
                dcnt += 1
        except KeyError:
            print("date가 없는 값을 찾음 :", cnt)
            pass     
    return
            
            
# [CODE 2]
def getDate(url):
    wd_op = webdriver.ChromeOptions()
    # 웹드라이버 설정
    # 백그라운드 실행인데 작동이 안되는 것 같음...
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    # wd_op.add_argument("headless")
    wd_op.add_argument("--no-sandbox")
    wd_op.add_argument("--disable-dev-shm-usage")
    # 웹드라이버 호출 (현재 버전 102.x)
    wd = webdriver.Chrome(executable_path='C:/Users/user/Desktop/크롤링 파일/2022-06-12 뉴스 데이터/WebDriver/chromedriver.exe', chrome_options=wd_op)
    # wd.execute_script('window.open("google.co.kr", "_blank");')
    tabs = wd.window_handles
    wd.set_window_position(0, 0)
    # wd.set_window_size(300, 300)
    
    # '코로나' 관련 뉴스 페이지 호출 (중앙일보, 2022.01.01 ~ 2022.06.xx)
    wd.get(url)

    try:
        print("날짜 수집 중...")
        news_date = wd.find_elements_by_xpath(f'//*[@id="container"]/div[1]/div[3]/span[1]')
        for i in news_date:
            date = i.text
            # 다른 구조를 가지고 왔다면 거기에 맞춰서 수집
            if '글자크기' in date:
                print("잘못된 문자가 인식되었으므로 재수집을 합니다.")
                news_date = wd.find_elements_by_xpath(f'//*[@id="container"]/div[1]/div[2]/span[1]')
                for i in news_date:
                    date = i.text
        # '입력 ' 이라는 불필요한 단어가 존재하므로 제거함
        fin_date = date.strip("입력 ")
        print("동아일보 결과 : ", fin_date)
        wd.close()
    except:
        pass
    
    return fin_date

# [CODE 0]
def main():
   
    # [CODE 1]
    print("동아일보 날짜 자료 수집 중 >>>>>>>>>>>>>>>>>>>>>>")
    d_date()
           
    
if __name__ == '__main__':
    main()