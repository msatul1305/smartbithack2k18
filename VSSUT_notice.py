from bs4 import BeautifulSoup
import re
import requests
from fake_useragent import UserAgent



url = 'http://www.vssut.ac.in/'                    # input your url here
file_name = 'notice.txt'              # output file name

user_agent = UserAgent()

page = requests.get(url,headers={'user-agent':user_agent.chrome})
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)
def read_file():
    file = open('vssut_notice.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')
tags=soup.find_all(class_='table')
for tag in tags:
    print(tags)
