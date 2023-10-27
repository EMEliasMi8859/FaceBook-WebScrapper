from WordList import WordList
import requests
from bs4 import BeautifulSoup
import random
import csv

def FaceBookLinkGenerator():
    link = ''.join(random.sample(WordList, random.randint(1,1)))
    link = "https://www.facebook.com/" + link + str(random.randint(1,1000))
    return link

def CheckFacebookLinkAddress(url):
    #these are local var diff from global
    print("extracting " + url)
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    check = soup.find('body', class_ = lambda value: value and all(class_name in value.split() for class_name in["_6s5d", "_71pn", "system-fonts--body"]))  
    return check is not None


def WriteValidLinksToCSV(link):
    with open('FacebookLinkDataBase.csv', 'a', newline= '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([link])
        print("[!]FaceBook account detected successfully!!!.....")


def findlinks():
    linkToCheck = FaceBookLinkGenerator()
    if(CheckFacebookLinkAddress(linkToCheck) is True):
        WriteValidLinksToCSV(linkToCheck)
    else:
        findlinks()
while True:
    findlinks()
