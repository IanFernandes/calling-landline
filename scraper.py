#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from random import randint
from bs4 import BeautifulSoup
from settings import INITIAL_URL, DRIVER
from selenium.webdriver.common.keys import Keys


def wait():
    random_number = randint(2, 5)
    time.sleep(random_number)


def get_countries_from_json():
    with open('countries.json') as countries_file:
        data = json.load(countries_file)
        return data['Countries']

DRIVER.get(INITIAL_URL)
assert "International" in DRIVER.title
inputElement = DRIVER.find_element_by_id("countryName")


def get_calling_landlines(content):
    soup = BeautifulSoup(content, "html.parser")
    land_line = soup.find("td", {"id": "landLine"})
    if land_line:
        return land_line.strong.text


for country in get_countries_from_json():
    inputElement.clear()
    inputElement.send_keys(country)
    inputElement.send_keys(Keys.ENTER)
    wait()
    DRIVER.find_element_by_id("paymonthly").click()
    print get_calling_landlines(DRIVER.page_source)
    wait()




