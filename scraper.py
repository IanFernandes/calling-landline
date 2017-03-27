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


def find_country_input():
    DRIVER.get(INITIAL_URL)
    assert "International" in DRIVER.title
    return DRIVER.find_element_by_id("countryName")


def get_calling_landlines(content):
    soup = BeautifulSoup(content, "html.parser")
    rates_table = soup.find("table", {"id": "standardRatesTable"})
    if rates_table:
        grey_box = rates_table.find("tr", "greyBox")
        return grey_box.find_all("td")[1].text


def insert_term_input(term, input_text):
    input_text.clear()
    input_text.send_keys(term)
    input_text.send_keys(Keys.ENTER)


def main():
    country_input = find_country_input()
    for country in get_countries_from_json():
        insert_term_input(country, country_input)
        wait()
        DRIVER.find_element_by_id("paymonthly").click()
        print get_calling_landlines(DRIVER.page_source)
        wait()
    DRIVER.quit()

if __name__ == "__main__":
    main()




