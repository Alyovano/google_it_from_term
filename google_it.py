#!/usr/bin/python3
import webbrowser
import sys

def google_it(requests):
    toSearch = iter(requests)
    next(toSearch)
    request = ""
    for asked in toSearch:
        request += str(asked + ' ')
    try:
        webbrowser.open("https://google.com/search?q={}".format(request))
        print("Google open : {}".format(request))
    except:
        print("Don't you have a browser ? wtf")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        google_it(sys.argv)
    else:
        print("Usage error : ./google <search_name>")
    exit()
