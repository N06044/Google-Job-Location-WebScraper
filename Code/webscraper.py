"""
---
Extracts a list of URLs from www.google.com/about/careers/applications/jobs/results?page={page_number}
---
Extracts data about the in-office locations of each job and stores it in a multidimensional list format
---
"""

import sys
import requests
import countries

from bs4 import BeautifulSoup


def get_url_list(page_number):
    url = f"https://www.google.com/about/careers/applications/jobs/results?page={page_number}"
    print(f"{'\033[94m'}Extracting data from {url} ...{'\033[0m'}\n")
    response = requests.get(url)
    if response.status_code == 200:
        url_list = []
        soup = BeautifulSoup(response.text, "lxml")
        for anchor_element in soup.find_all("a", class_="WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb"):
            url_list.append(f"https://www.google.com/about/careers/applications/{anchor_element.get("href")}")
        return url_list
    else:
        sys.exit(f"Request Failed - Status Code: {response.status_code}")


def get_location_data(url_list):
    location_data = []
    for url in url_list:
        print(f"Extracting data from {url} ...")
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            note = soup.find("div", class_="OJgC7b")
            execute = True
            if note and note.find_all("b"):
                for bold_element in note.find_all("b"):
                    for country in countries.aggregated_data:
                        if bold_element.string and "Remote" in bold_element.string:  # Discard Remote Locations
                            print("")
                            execute = False
                            break
                        if bold_element.string and country in bold_element.string:
                            element = bold_element.string.strip(".").replace("In-office locations: ", "").split("; ")
                            location_data.append(element)
                            print(f"{element}\n")
                            execute = False
                            break
                    if not execute:
                        break
            if execute:
                element = soup.find("span", class_="pwO9Dc vo5qdf").find("span", class_="r0wTof").string.split("; ")
                location_data.append(element)
                print(f"{element}\n")
        else:
            print(f"Request Failed - Status Code: {response.status_code}\n")
    return location_data
