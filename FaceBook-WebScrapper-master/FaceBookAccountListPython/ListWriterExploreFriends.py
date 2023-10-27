from WordList import WordList
import requests
from bs4 import BeautifulSoup
import random
import csv

def FaceBookLinkGenerator():
    link = ''.join(random.sample(WordList, random.randint(1,3)))
    link = "https://www.facebook.com/" + link
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

def ExploreFriends(url):
    FriendsResponse = requests.get(url)
    FriendsSoup = BeautifulSoup(FriendsResponse.content, 'html.parser')
    FriendElement = FriendsSoup.find('span', class_ = lambda value: value and all(class_name in value.split() for class_name in["x1lbecb7", "x1s688f", "xzsf02u"]))
    #FriendElement = FriendsSoup.find_all('div', class_='x6s0dn4 x78zum5 x1iyjqo2')
    #FriendElement = FriendsSoup.find_all('div', class_='_2lek')
    #FriendNames = [friend.find('span', class_= "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u").text for friend in FriendElement]
    #x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u
    print(FriendElement)

ExploreFriends("https://www.facebook.com/isabelle.aubree/friends/")

#while True:
#    findlinks()