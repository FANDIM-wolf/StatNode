# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import bs4
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')
soup = bs4.BeautifulSoup(source,'lxml')
js_test =soup.find('p',class_='jstest')

print(js_test.text)