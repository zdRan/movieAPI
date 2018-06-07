import requests
import json



def get_pages(type,page_number):
	page = requests.get("http://www.dytt8.net/html/gndy/dyzz/list_23_1.html")
	page.encoding = "gb2312"
	print(page.apparent_encoding)
	print(page.text)
	pass

def loda_url():

	f = open("url.json","r")
	dict_url = json.load(f)

	print(dict_url["2"])


if __name__ == '__main__':
	get_pages(1, 1)
