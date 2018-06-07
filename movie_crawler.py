import requests
import json
from bs4 import BeautifulSoup  
import re

def get_pages(type,page_number):
	dict_url = json.load(open("url_dict.json","r"))
	page = requests.get(str(dict_url[type])+str(page_number)+".html")
	page.encoding = "gb2312"
	soup = BeautifulSoup(page.text,"lxml")
	item_list = soup.find_all("a", class_="ulink")
	for item in item_list:
		print(item["href"])
		pass
	pass

def movie_info(movie_url):
	info = requests.get(movie_url)
	info.encoding = "gb2312"
	soup = BeautifulSoup(info.text,"lxml")
	td = soup.find("div",id = "Zoom").td
	
	for x in td.contents:
		print(x)
	
	image_list = soup.find_all("img",src=re.compile("jpg"))

def loda_url():

	dict_url = json.load(open("url_dict.json","r"))

if __name__ == '__main__':
	movie_info("http://www.ygdy8.com/html/gndy/dyzz/20180429/56763.html")
