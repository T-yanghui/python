import requests

session = requests.session()
headers_1 = {
	'Connection': 'keep-alive',
	'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
headers_2 = {
	'Connection': 'keep-alive',
	'Referer': 'https://accounts.douban.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

data = {
	'ck':'', 
	'remember': 'true',
	'name': '15576886097',
	'password': 'cnm201501'
    }


def sign_in():
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    return(session.post(login_url, headers=headers_1, data=data))



def get_html():
    table_url = 'https://www.douban.com/'
    return (session.get(table_url, headers=headers_2))
    #以上9行代码，是发表评论。


if __name__ == '__main__':
	res1 = sign_in()
	print(res1.status_code)
	res2 = get_html()
	# print(res2.text)
	f = open("D:/code/python/table.html",'w',encoding='UTF-8')
	f.write(res2.text)
	f.close()

