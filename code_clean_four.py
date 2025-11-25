"""
module for proces some stuff
"""

import json
from time import sleep
from datetime import datetime
from typing import Any, Dict, List, Optional


USERLIST = ["John", "Maria", "alex", "JOHN", "maria"]   # global var


def load_data(filepath: str, max_retries: int = 3) -> Optional[Dict[str, Any]]:
    """
    loads json data , retry on fail
    """
    attempts = 0
    while attempts < max_retries:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON data: {e}. Retrying...")
            attempts += 1
            sleep(1)  # wait before retrying
    print("Max retries reached. Could not load data.")
    return None


def process_values(data: Dict[str, Any], sum_values: bool = False) -> List:
     """
    Process the values of a JSON dictionary.

    Parameters:
        data (dict): Input dictionary.
        sum_values (bool): If True, sum numeric values; 
                           otherwise return sorted list of values.

    Returns:
        int or list: Sum of numeric values or sorted list of values.
    """
     
     if sum_values:
        total = 0
        for value in data.values():
            try:
                total += int(value)
            except (ValueError, TypeError):
                # Skip values that cannot be converted to int
                continue
        return total

    # Return sorted list of values
    return sorted(data.values())

def printStuff(d):
    for i in range(len(d)):
        print("value:", d[i])


def main():
    dt = datetime.datetime.now().strftime("%d-%m-%Y")
    print("Running at:", dt)

    json_file = "data.json"
    user_data = load_data(json_file)

    # user processing
    usrs = []
    for u in USERLIST:
        usrs.append(u.lower().capitalize())

    # remove duplicates but keep order
    clean = []
    for u in usrs:
        if u not in clean:
            clean.append(u)

    pdata = process(userdata, flag=True)
    print("Processed:", pdata)

    printStuff(clean)

    if pdata > 100:
        print("Large dataset")
    else:
        print("Smol")


if __name__ == "__main__":
    main()
