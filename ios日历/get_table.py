import requests, json
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

data = {
    'username':'x20485qt', 
    'password':'123TQB0920YH!',
    }


def sign_in():
    url = 'https://login.manchester.ac.uk/cas/login'
    session.post(url, headers=headers, data=data)
    print(session.cookies)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('D:/code/python/cookies.txt', 'w')
    f.write(cookies_str)
    f.close()
    # 以上5行代码，是cookies存储。

def cookies_read():
    cookies_txt = open('D:/code/python/cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return (cookies)
    # 以上4行代码，是cookies读取。

def get_html():
    url_2 = 'https://my.manchester.ac.uk/uPortal/f/home/p/timetable.u23l1n3101/max/render.uP?pP_view=list'
    return (session.get(url_2, headers=headers))
    #以上9行代码，是发表评论。

try:
    session.cookies = cookies_read()
    print(session.cookies)
except FileNotFoundError:
    sign_in()
    session.cookies = cookies_read()

num = get_html()
if num.status_code == 200:
    table = open('D:/code/python/table.html', 'w')
    table.write(num.text)
    table.close()
    # print(num.text)
else:
    sign_in()
    session.cookies = cookies_read()
    num = get_html()