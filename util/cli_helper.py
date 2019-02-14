"""Util functions for the script"""
import sys
import csv


def get_all_user_names():
    """Returns all the usernames given as parameter"""
    usernames = []
    if len(sys.argv) < 2:
        sys.exit('- Please provide at least one username!\n')
    if str(sys.argv[2]).__contains__('.'):
        with open(str(sys.argv[2]), newline='') as csvfile:
            usernames = csv.reader(csvfile, delimiter = ',')
    else:
        for username in sys.argv[1:]:
            usernames.append(username)
    return usernames