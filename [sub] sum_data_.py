import json

cnt = 0
news_data = []
data = []

with open("./joongang_News_links.json", "r", encoding="utf8") as j_nd:
    j_news = j_nd.read()
    joongang_news_data = json.loads(j_news)
with open("./kukmin_News_links.json", "r", encoding="utf8") as k_nd:
    k_news = k_nd.read()
    kukmin_news_data = json.loads(k_news)

for n_data in joongang_news_data:
    news_data.append(n_data)
for n_data in kukmin_news_data:
    news_data.append(n_data)
    
for i in news_data:
    i['cnt'] = cnt
    data.append(i)
    print(cnt, "번째 새로이 작업 중")
    cnt += 1
    
with open('./News_data.json', 'w', encoding='utf-8') as outfile:
    jsonFile = json.dumps(news_data, indent=2, sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)
    
print("완료")