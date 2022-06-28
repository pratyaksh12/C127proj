from re import M
from turtle import distance
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('.\chromedriver')

browser.get(START_URL)

time.sleep(10)

soup = BeautifulSoup(browser.page_source, "html.parser")

star_table = soup.find('table')

temp_list = []

table_row = star_table.find_all('tr')

for tr in table_row:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


star_name = []
Distance = []
Mass = []
Radius = []
Luminosity = []


for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])



df = pd.DataFrame(list(zip(star_name,Distance,Mass,Radius,Luminosity)),columns = ['star_name','Distance','Mass','Radius','Luminosity'])

df.to_csv('bright_star.csv')