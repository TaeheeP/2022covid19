import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# [CODE 1-1]
def j_date():
    cnt = 0
    jsonResult = []
    # 데이터를 가져온다
    with open('./joongang_News_links.json', 'r', encoding='utf-8') as nl:
        json_data = json.load(nl) # 리스트 타입
    
    for links in json_data:
        try:
            # links 안에 date가 이미 존재한다면,
            #  or (links['date'] != None) 조건문에 추가하려 했는데 모른댄다 어휴,..
            if ('date' in links) and (links['date'] != None):
                print("날짜가 미표시 된 자료 로딩중... : ", cnt)
                cnt += 1
                print("다음 표시 될 번호 :", cnt)
                pass
            # 만약 date에 None이 출력되었거나 요소가 존재하지 않는다면,
            if ('date' not in links) or (links['date'] == '') or (links['date'] == None):      
                getdate = getDate(links['href'])
                print("뭐지? : ", getdate)
                links['date'] = getdate
                # 실제 파일 n번째에 있는 'date' 에 날짜를 넣는다
                json_data[cnt]['date'] = getdate
                print("파일 결과 : \n", json_data[cnt]['date'])
                print("결과 : \n", links)
                # 보험으로 jsonResult 에도 넣는다
                jsonResult.append(links)
                with open('./joongang_News_links.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, indent="\t", ensure_ascii=False)
                cnt += 1
        except KeyError:
            print("date가 없는 값을 찾음 :", cnt)
            pass
    return cnt
            
              
# [CODE 1-2]
def k_date(cnt):
    cnt += 1
    kcnt = 0
    jsonResult = []
    # 데이터를 가져온다
    with open('./kukmin_News_links.json', 'r', encoding='utf-8') as nl:
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
            if ('date' not in links) or (links['date'] == '') or (links['date'] == None):      
                getdate = getDate(links['href'])
                links['date'] = getdate
                # 실제 파일 n번째에 있는 'date' 에 날짜를 넣는다
                print("순서 : ", cnt)
                json_data[kcnt]['date'] = getdate
                print("파일 결과 : \n", json_data[kcnt]['date'])
                print("결과 : \n", links)
                # 보험으로 jsonResult 에도 넣는다
                jsonResult.append(links)
                with open('./kukmin_News_links.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, indent="\t", ensure_ascii=False)
                cnt += 1
                kcnt += 1
        except KeyError:
            print("date가 없는 값을 찾음 :", cnt)
            pass
    return cnt
            
               
# [CODE 1-3]
def d_date(cnt):
    cnt += 1
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
    wd_op.add_argument("headless")
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
        getUrl = wd.current_url
        if "joongang.co.kr" in getUrl:
            news_date = wd.find_elements_by_xpath(f'//*[@id="container"]/section/article/header/div[2]/div/p[1]')
            print("날짜 수집 중...") 
            for i in news_date:
                date = i.text
            # '입력 ' 이라는 불필요한 단어가 존재하므로 제거함
            sec_date = date.strip("입력 ")
            # 20xx.01 이 아닌 20xx-01 로 바꿈
            fin_date = sec_date.replace(".", "-")
            print("중앙일보 결과 : ", fin_date)
            wd.quit()
        elif "kmib.co.kr" in getUrl:
            news_date = wd.find_elements_by_xpath(f'//*[@id="sub"]/div[1]/div/div[2]/div/div[1]/span[1]')
            print("날짜 수집 중...") 
            for i in news_date:
                date = i.text
            fin_date = date
            print("국민일보 결과 : ", fin_date)
            wd.quit()
        elif "donga.com" in getUrl:
            news_date = wd.find_elements_by_xpath(f'//*[@id="container"]/div[1]/div[3]/span[1]')
            print("날짜 수집 중...")
            for i in news_date:
                date = i.text
            # 다른 구조를 가지고 왔다면 거기에 맞춰서 수집
            if '글자크기' in date:
                print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                news_date = wd.find_elements_by_xpath(f'//*[@id="container"]/div[1]/div[2]/span[1]')
                for i in news_date:
                    date = i.text
            # '입력 ' 이라는 불필요한 단어가 존재하므로 제거함
            fin_date = date.strip("입력 ")
            print("동아일보 결과 : ", fin_date)
            wd.quit()
    except:
        pass
    
    return fin_date

# [CODE 0]
def main():
    cnt = 0
    jsonResult = []
    # 데이터를 가져온다
    
    # [CODE 1]
    print("중앙일보 날짜 자료 수집 중 >>>>>>>>>>>>>>>>>>>>>>")
    cnt = j_date()
    
    print("국민일보 날짜 자료 수집 중 >>>>>>>>>>>>>>>>>>>>>>")
    cnt = k_date(cnt)
    
    print("동아일보 날짜 자료 수집 중 >>>>>>>>>>>>>>>>>>>>>>")
    d_date(cnt)
    
    
    # 전체를 모아서 정리 파일을 내는 것이지만 json 요청 특성상 일정 크기가 넘어가면 오류를 일으키는 것으로 알고있다...
    # [CODE 4]
    try:
        print("모든 자료 집계 중 >>>>>>>>>>>>>>>>>>>>>>")   
        with open('./joongang_News_links.json', 'r', encoding='utf-8') as jd:
            joongang_json_data = json.load(jd) # 리스트 타입
        with open('./kukmin_News_links.json', 'r', encoding='utf-8') as kd:
            kukmin_json_data = json.load(jd) # 리스트 타입
        with open('./donga_News_links.json', 'r', encoding='utf-8') as dd:
            donga_json_data = json.load(dd) # 리스트 타입
        
        for data in joongang_json_data:
            jsonResult.append(data)
        for data in kukmin_json_data:
            jsonResult.append(data)
        for data in donga_json_data:
            jsonResult.append(data)
                
        # 보험으로 jsonResult 에도 넣는다
        # jsonResult.append(links)
            
        with open('./News_links_date.json', 'w', encoding='utf-8') as outfile:
            jsonFile = json.dumps(jsonResult, indent=2, sort_keys=True, ensure_ascii=False)
            outfile.write(jsonFile)
    except:
        print("자료 양이 너무 많거나 오류가 발생했습니다.")
        
        
    
if __name__ == '__main__':
    main()