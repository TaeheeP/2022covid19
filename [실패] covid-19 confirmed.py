import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64
import re
import time 


# [CODE 1]
def import_image(cnt):
    wd_op = webdriver.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    wd_op.add_argument("--no-sandbox")
    wd_op.add_argument("--disable-dev-shm-usage")
    wd = webdriver.Chrome(executable_path='C:/Users/user/Desktop/크롤링 파일/2022-06-12 뉴스 데이터/WebDriver/chromedriver.exe', chrome_options=wd_op)
    wd.set_window_position(0, 0)
    
    wd.get('https://www.incheon.go.kr/covid19/index')
    
    # 확진자 추이 창으로 이동함
    wd.execute_script('document.getElementById("tab1").setAttribute("style", "display: none;")')
    wd.execute_script('document.getElementById("tab3").setAttribute("style", "display: block;")')
    time.sleep(1)
    
    # 중복 클래스가 있으므로, 쿼리셀렉터로 날짜를 선택함
    wd.execute_script('document.querySelector("body > div:nth-child(8)").setAttribute("style", "display: block; position: absolute; left: 266.75px; top: 1686.1px;")')
    wd.execute_script('document.querySelector("body > div:nth-child(8) > div.xdsoft_datepicker.active > div.xdsoft_monthpicker > div.xdsoft_label.xdsoft_month > div").setAttribute("style", "display: block;")')
    
    wd.find_element_by_xpath(f'/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[%s]' % cnt).click()
    #wd.find_element_by_xpath(f'/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[1]').click()
    
    time.sleep(50)

# [CODE 0]
def main():
    
    for i in range(1, 7):
        import_image(i)
        
if __name__ == '__main__':
    main()