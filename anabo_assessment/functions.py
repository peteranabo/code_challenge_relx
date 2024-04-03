from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import external_variables
import select
import requests
import html
import csv
import essentials
import time

def open_html():
    essentials.instanced_selenium_package.driver.get('https://idbop.mylicense.com/verification/Search.aspx')

    license_type_dropdown = essentials.instanced_selenium_package.driver.find_element("id", "t_web_lookup__license_type_name")

    select_dropdown = Select(license_type_dropdown)

    license_type_dropdown_options = select_dropdown.options

    for index, option in enumerate(license_type_dropdown_options):
        print(f"{index}.{option.text}")

    input_search_last_name = str(input("Enter Search Key for Last Name: "))
    input_dropdown_license_type = int(input("Enter Option Number: "))

    select_dropdown.select_by_index(input_dropdown_license_type)

    last_name_input = essentials.instanced_selenium_package.driver.find_element("id", "t_web_lookup__last_name")
    last_name_input.send_keys(input_search_last_name)

    search_button = essentials.instanced_selenium_package.driver.find_element("id", "sch_button")
    search_button.click()

def parse_table():
    
    table_data = essentials.instanced_selenium_package.driver.find_element("xpath", '//*[@id="datagrid_results"]/tbody')

    rows = table_data.find_elements("xpath", ".//tr")
    header = rows[0].find_elements("xpath", ".//th")
    columns = [header.text for header in header]
    data = []
    for row in rows[1:]:
        columns_data = row.find_elements("xpath", ".//td")
        row_data = [column.text for column in columns_data]
        data.append(row_data)

    clean_data = []
    counter = 0
    print(len(data))
    for i in range(0,(len(data) - 6)):
        if i == counter:
            for x in range(0,4):
                data[i].pop(2)
            data[i].pop(0)

            clean_data.append(data[i])
            counter += 6
    
    for element in clean_data:
        print(element)

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(clean_data)

    print("CSV file saved successfully!")

    essentials.instanced_selenium_package.driver.quit()