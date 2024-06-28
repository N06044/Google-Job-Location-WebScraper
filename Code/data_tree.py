"""
---
Receives location data from the WebScraper and transforms it into a tree structure using dictionaries
---
Prints the tree structure in the terminal
---
"""


def get_location_data_tree(location_data):
    location_data_tree = {}
    for list_element_01 in location_data:
        for list_element_02 in list_element_01:
            for string_element in list_element_02:
                location_list = string_element.split(", ")
                location_list_length = len(location_list)
                if location_list_length >= 3:
                    key1 = location_list[location_list_length - 1]  # Expected -> "USA"
                    key2 = location_list[location_list_length - 2]  # Expected -> "CA"
                    key3 = location_list[location_list_length - 3]  # Expected -> "San Francisco"
                    if key1 not in location_data_tree:
                        location_data_tree.update({key1: {key2: {key3: 1}}})
                    elif key2 not in location_data_tree[key1]:
                        location_data_tree[key1].update({key2: {key3: 1}})
                    elif key3 not in location_data_tree[key1][key2]:
                        location_data_tree[key1][key2].update({key3: 1})
                    else:
                        location_data_tree[key1][key2][key3] += 1
                elif location_list_length == 2:
                    key1 = location_list[location_list_length - 1]  # Expected -> "Germany"
                    key2 = location_list[location_list_length - 2]  # Expected -> "Berlin"
                    if key1 not in location_data_tree:
                        location_data_tree.update({key1: {key2: 1}})
                    elif key2 not in location_data_tree[key1]:
                        location_data_tree[key1].update({key2: 1})
                    else:
                        location_data_tree[key1][key2] += 1
                else:
                    key1 = location_list[location_list_length - 1]  # Expected -> "Singapore"
                    if key1 not in location_data_tree:
                        location_data_tree.update({key1: 1})
                    else:
                        location_data_tree[key1] += 1
    return location_data_tree


def show_location_data_tree(location_data_tree):
    d1_length = len(location_data_tree.keys())
    d1_counter = 0
    for key1 in location_data_tree:
        d1_counter += 1
        if isinstance(location_data_tree[key1], dict):
            print(f"{'\033[91m'}{key1}{'\033[0m'}")
            d2_length = len(location_data_tree[key1].keys())
            d2_counter = 0
            for key2 in location_data_tree[key1]:
                d2_counter += 1
                if isinstance(location_data_tree[key1][key2], dict):
                    if d2_length == d2_counter:
                        print(f"└── {'\033[92m'}{key2}{'\033[0m'}")
                    else:
                        print(f"├── {'\033[92m'}{key2}{'\033[0m'}")
                    d3_length = len(location_data_tree[key1][key2].keys())
                    d3_counter = 0
                    for key3 in location_data_tree[key1][key2]:
                        d3_counter += 1
                        if d1_length == d1_counter and d2_length == d2_counter and d3_length == d3_counter:
                            print(f"    └── {'\033[94m'}{key3} {'\033[95m'}({location_data_tree[key1][key2][key3]}){'\033[0m'}")
                        elif d2_length == d2_counter and d3_length == d3_counter:
                            print(f"    └── {'\033[94m'}{key3} {'\033[95m'}({location_data_tree[key1][key2][key3]}){'\033[0m'}\n")
                        elif d3_length == d3_counter:
                            print(f"│   └── {'\033[94m'}{key3} {'\033[95m'}({location_data_tree[key1][key2][key3]}){'\033[0m'}")
                        elif d2_length == d2_counter:
                            print(f"    ├── {'\033[94m'}{key3} {'\033[95m'}({location_data_tree[key1][key2][key3]}){'\033[0m'}")
                        else:
                            print(f"│   ├── {'\033[94m'}{key3} {'\033[95m'}({location_data_tree[key1][key2][key3]}){'\033[0m'}")
                else:
                    if d1_length == d1_counter and d2_length == d2_counter:
                        print(f"└── {'\033[92m'}{key2} {'\033[95m'}({location_data_tree[key1][key2]}){'\033[0m'}")
                    elif d2_length == d2_counter:
                        print(f"└── {'\033[92m'}{key2} {'\033[95m'}({location_data_tree[key1][key2]}){'\033[0m'}\n")
                    else:
                        print(f"├── {'\033[92m'}{key2} {'\033[95m'}({location_data_tree[key1][key2]}){'\033[0m'}")
        else:
            if d1_length == d1_counter:
                print(f"{'\033[91m'}{key1} {'\033[95m'}({location_data_tree[key1]}){'\033[0m'}")
            else:
                print(f"{'\033[91m'}{key1} {'\033[95m'}({location_data_tree[key1]}){'\033[0m'}\n")
