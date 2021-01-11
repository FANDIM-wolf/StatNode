from bs4 import BeautifulSoup
import requests as req 

#function to  get information from jolybell
def joly_bell_information():
	resp = req.get("https://jolybell.com")                     #get site
	soup = BeautifulSoup(resp.text,'lxml') #create object 
	print(soup.title)
	print(soup.title.text)

joly_bell_information()

#write url and get title of site 
def get_site():
	site_site= input("Enter full url:")
	resp = req.get(site)
	soup = BeautifulSoup(resp.text,'lxml')
	print(soup.title)

def get_product():
	with open("index.html", "r") as f:
		contents = f.read()
		soup = BeautifulSoup(contents,'lxml')
		found_object = soup.find("div" , id="category-product")
		print(found_object.text)
    
get_product()    

#get some elements "li" in html file 
def get_list():
	with open("index.html", "r") as f:
		contents = f.read()
		soup = BeautifulSoup(contents,'lxml')
		for tag in soup.find_all("li"):
			print("{0}".format(tag.text))

get_list()

    
    #contents = f.read()
 
    #soup = BeautifulSoup(contents, 'lxml')
 
    #for tag in soup.find_all("li"):
        #print("{0}: {1}".format(tag.name, tag.text))



