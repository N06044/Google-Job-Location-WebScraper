"""
---
Searches a specified number of pages (20 jobs per page)
---
Extracts location data and presents it in a tree structure
---
"""

import webscraper
import data_tree

page_number = int(input("How many pages do you want to search? "))

print(f"\nGot it, searching the first {page_number} pages ...\n")

page_list = list(range(1, page_number + 1))

location_data = []

for page in page_list:
    url_list = webscraper.get_url_list(page)
    location_data.append(webscraper.get_location_data(url_list))

location_data_tree = data_tree.get_location_data_tree(location_data)

data_tree.show_location_data_tree(location_data_tree)
