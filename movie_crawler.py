import requests
import json
from bs4 import BeautifulSoup  
import re
import operator
def init_pages(type,page_number):
	dict_url = json.load(open("url_dict.json","r"))
	page = requests.get(str(dict_url[type])+str(page_number)+".html")
	page.encoding = "gb2312"
	soup = BeautifulSoup(page.text,"lxml")
	item_list = soup.find_all("a", class_="ulink")
	result_list = []
	for item in item_list:
		name = re.search(r"《.*》",str(item.string))
		result = movie_info(dict_url["prefix"]+item["href"])
		result["name"] = name.group()
		result_list.append(result)
	json.dump(result_list, open(type+"_"+page_number+".json","w"))

def movie_info(movie_url):
	info = requests.get(movie_url)
	result = {}
	info.encoding = "gb2312"
	soup = BeautifulSoup(info.text,"lxml")
	image_list = soup.find_all("img",src=re.compile("jpg"))
	
	result["poster"] = image_list[0]["src"]

	bt_link = soup.find_all("a")
	for x in bt_link:
		if str(x.string).find("ftp") != -1:
			result["bt_link"] = x.string
	
	return result

def loda_url():
	dict_url = json.load(open("url_dict.json","r"))

def search_movie(key):
	data = {
		"kwtype":"0",
		"searchtype":"title",
		"keyword":encode(key) 
	}
	result = requests.get("http://s.ygdy8.com/plus/so.php",data = data)
	print()
	result.encoding = "gb2312"
	print(result.text)

def encode(s):  
    result = ''  
    index = 1  
    for c in s:  
        v = hex(ord(c)).replace('0x', '')  
        if len(v) == 1:  
            v = '0' + v  
        result += v  
        if index % 32 == 0:  
            result += '\n'  
        elif index % 4 == 0:  
            result += ' '  
        index += 1  
    print(result)  
    return result  

if __name__ == '__main__':
	search_movie("红海行动")
