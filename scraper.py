#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from random import randint
from bs4 import BeautifulSoup
from settings import INITIAL_URL, DRIVER
from selenium.webdriver.common.keys import Keys


def wait():
    """Sleeps the script, for the time defined at random"""
    random_number = randint(2, 5)
    time.sleep(random_number)


def get_countries_from_json():
    """Returns the countries listed in countries.json file"""
    with open('countries.json') as countries_file:
        data = json.load(countries_file)
        return data['Countries']


def find_country_input():
    """Returns the input text element where country will be located"""
    DRIVER.get(INITIAL_URL)
    assert "International" in DRIVER.title
    return DRIVER.find_element_by_id("countryName")


def get_calling_landlines(content):
    """Converts the content passed as argument in BeautifulSoup object and extracts landine price"""
    soup = BeautifulSoup(content, "html.parser")
    rates_table = soup.find("table", {"id": "standardRatesTable"})
    if rates_table:
        landine_tag = rates_table.find("tr", "greyBox")
        return landine_tag.find_all("td")[1].text


def insert_term_input(term, input_text):
    """Inserts the term on input_text both defined as argument"""
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




