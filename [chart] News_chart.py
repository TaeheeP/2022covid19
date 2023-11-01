import json
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

import pandas as pd
import numpy as py
from PIL import Image

# [CODE 1]
# 날짜별 데이터 추출 (2022-01-01 ~ 2022-06-12)
def getMonth(data, m_1, m_2, m_3, m_4, m_5, m_6):

    # 뉴스 데이터 갯수 추출 (4000)
    news_data_index = len(data)
    print("데이터 총 갯수 : %s" % news_data_index)
    
    try:
        for dict_data in data:
            if "2022-01" in dict_data['date']:
                #print("1월 데이터 수집중...")
                m_1.append(dict_data)
            if "2022-02" in dict_data['date']:
                #print("2월 데이터 수집중...")
                m_2.append(dict_data)
            if "2022-03" in dict_data['date']:
                #print("3월 데이터 수집중...")
                m_3.append(dict_data)
            if "2022-04" in dict_data['date']:
                #print("4월 데이터 수집중...")
                m_4.append(dict_data)
            if "2022-05" in dict_data['date']:
                #print("5월 데이터 수집중...")
                m_5.append(dict_data)
            if "2022-06" in dict_data['date']:
                #print("6월 데이터 수집중...")
                m_6.append(dict_data)
        print("월별 데이터 분리")
    except:
        pass

    return m_1, m_2, m_3, m_4, m_5, m_6

# [CODE 2]
def getChart(month, cnt):
    text = ""
    Result = []
    for text_pocket in month:
        Result.append(text_pocket['title'])
        Result.append(text_pocket['content'])

    # txt 형태로 변환
    for data in Result:
        text += data

    # 명사만 추출, 그 외 필요없는 단어 제외
    nouns = Okt().nouns(text)
    words = [n for n in nouns if len(n) > 1 and n != '감염증' and n != '코로나' and n != '코로나바이러스' and n != '진자' 
             and n != '명대' and n != '이후' and n != '가운데' and n != '때문' and n != '관련' and n != '통해' and n != '대해'
             and n != '위해' and n != '수가' and n != '세로' and n != '가장' and n != '지난' and n != '라며' and n != '면서'
             and n != '개월' and n != '이번' and n != '동안' and n != '자영' and n != '경우' and n != '다만' and n != '신종'
             and n != '닷새' and n != '이틀' and n != '너희' and n != '대부분' and n != '확산' and n != '확진' and n != '오후']
    # 워드 클라우드용
    fav_words = Counter(words)
    
    # 막대 그래프용    
    rate_words = fav_words.most_common(10)
    x_label = []
    y_label = []
    
    for rate_word in rate_words:
        x_label.append(rate_word[1])
        y_label.append(rate_word[2])
    
    # 워드 클라우드
    print("워드 클라우드 작업 중")
    wc = WordCloud(font_path='malgun', width=400, height=400, background_color='white', scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(fav_words)
    plt.figure()
    plt.imshow(gen)
    
    wc.to_file('./Word_Image/워드클라우드_%s.png' % cnt)
    #print("단어 카운트 결과, ", c)
    return

# [CODE 0]
def main():
    # 데이터 불러오는 중...
    m_1, m_2, m_3, m_4, m_5, m_6 = [], [], [], [], [], []
    j_data = []
    k_data = []
    d_data = []
    with open("./joongang_News_links.json", "r", encoding="utf8") as nd:
        news = nd.read()
        j_data = json.loads(news)
    with open("./kukmin_News_links.json", "r", encoding="utf8") as nd:
        news = nd.read()
        k_data = json.loads(news)
    with open("./donga_News_links.json", "r", encoding="utf8") as nd:
        news = nd.read()
        d_data = json.loads(news)
    
    
    # 6월까지 카운트 시켜준다
    cnt = 0
    m_1, m_2, m_3, m_4, m_5, m_6 = getMonth(j_data, m_1, m_2, m_3, m_4, m_5, m_6)
    print("합산된 데이터 총 갯수 : ", len(m_1)+len(m_2)+len(m_3)+len(m_4)+len(m_5)+len(m_6))
    m_1, m_2, m_3, m_4, m_5, m_6 = getMonth(k_data, m_1, m_2, m_3, m_4, m_5, m_6)
    print("합산된 데이터 총 갯수 : ", len(m_1)+len(m_2)+len(m_3)+len(m_4)+len(m_5)+len(m_6))
    m_1, m_2, m_3, m_4, m_5, m_6 = getMonth(d_data, m_1, m_2, m_3, m_4, m_5, m_6)
    print("합산된 데이터 총 갯수 : ", len(m_1)+len(m_2)+len(m_3)+len(m_4)+len(m_5)+len(m_6))
    # getChart(m_1)
    for i in [m_1, m_2, m_3, m_4, m_5, m_6]:
        cnt += 1
        getChart(i, cnt)
if __name__ == '__main__':
    main()
    