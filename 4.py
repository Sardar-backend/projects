import requests
x=requests.get("https://jsonplaceholder.typicode.com/posts")
y=x.json()
print(y[0]['body'])
print(y[0])
#برنامه گرفتن اطلاعت از یک ای پی ای و تبدیل آن به جیسون و انتخاب اطلاعت موجود در آن
