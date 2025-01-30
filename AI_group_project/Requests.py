import requests
res  = requests.get('http://www.google.com')
res.raise_for_status()
#print("응답코드 : ", res.status_code) # 200이면 정상
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)