#!/usr/bin/env python
import platform
from payload import exploit_library
from pyfiglet import Figlet
from beautifultable import BeautifulTable
import sys

def manual_search_check(user_input): #If user wants to use manual search feature
    # Check if user entered an index or 's' or something completely different
    try:
        return int(user_input)
    except:
        if user_input == "s":
            return "s"
        else:
            print("Wrong input!!!")
            user_input = input("Enter the number of the exploit you want to use or enter s to make a new call: ")
            manual_search_check(user_input)

if __name__ == '__main__':
    '''Variables'''
    exploit = exploit_library.Exploit_Library()
    exploit_lib = exploit.exploit_lib

    '''Banner'''
    custom_figlet = Figlet(font="doh", width=200)
    print(custom_figlet.renderText("MacPER"))
    custom_figlet = Figlet(font="digital", width=80)
    print(custom_figlet.renderText("        ....MacOS Priv. Esc Research....        "))



    '''Gather Current MacOS Version'''
    print("Gathering OS version...")
    version = platform.mac_ver()
    print("Target OS Version: " + str(version[0]))
    e = exploit.is_target_vulnerable(version[0], exploit_lib[0])

    '''Suggest Feasible Exploits & Search Feature '''
    print("Searching for Feasible Exploits...")
    feasible_exploits = exploit.search_exploit(version[0])
    print("Suitable Exploits: ")

    table = BeautifulTable()
    table.columns.header = ["#", "cve", "name"]
    exp_index = 1
    for i in feasible_exploits:
        table.rows.append([exp_index, str(i[1]["cve"]), i[1]["name"]])
        exp_index = exp_index +1
    print(table)
    print("\n")
    user_input = input("Enter the number of the exploit you want to use or enter s to make a new call (0 to exit!!): ")
    if user_input == "0":
        print("Exiting...")
        sys.exit()
    else:
        exploit_index = manual_search_check(user_input)

    # Manual search
    if exploit_index == 's':
        user_input = input("Enter cve, exploit name, or an application: ")
        feasible_exploits = exploit.search_exploit(user_input)
        # Table View
        table = BeautifulTable()
        table.columns.header = ["#", "cve", "name"]
        exp_index = 1
        for i in feasible_exploits:
            table.rows.append([exp_index, str(i[1]["cve"]), i[1]["name"]])
            exp_index = exp_index + 1
        print(table)
        print("\n")
        user_input = input("Enter the number of the exploit you want to use or enter s to make a new call (0 to exit!!): ")
        exploit_index = manual_search_check(user_input)
        if user_input == "0":
            print("Exiting...")
            sys.exit()
        else:
            exploit_index = manual_search_check(user_input)



    '''Execute Selected Exploit'''
    result = exploit.run_exploit(version[0], feasible_exploits[int(exploit_index)-1][1])

    '''Process Completion'''
    print("Process Completed !!!")
