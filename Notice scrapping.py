from bs4 import BeautifulSoup
import re


def read_file():
    file = open('vssut_notice.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')
tags=soup.find_all(class_='table')
for tag in tags:
    print(tags)

