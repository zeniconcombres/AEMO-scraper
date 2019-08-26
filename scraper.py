import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint
import json
import re
import os 
import zipfile

url = "http://www.nemweb.com.au/Reports/Current/Causer_Pays/"
dataLinks = []
cwd = os.getcwd()

def unzipFile(filename):
    with zipfile.ZipFile(cwd + "/files/" + filename, 'r') as zip_ref:
        zip_ref.extractall(cwd + "/files/CSV")

def downloadFile(filename):
    print("Downloading file: " + filename)
    try:
        uri = url + filename
        urllib.request.urlretrieve(url + filename, cwd + "/files/" + filename)
        unzipFile(filename)
    except urllib.error.HTTPError as e:
        print("Http error on " + filename)

def getALinks(url):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    # get text
    links = soup.findAll("a")
    for a in links:
        item = a['href'].rsplit('/', 1)[-1]
        dataLinks.append(item)

def driver():
    print("Gathering URLS...")
    getALinks(url)
    print("Completed")
    print("Starting download...")
    dataLinks.pop(0)
    downloaded = 0
    for uri in dataLinks:
        downloadFile(uri)
        downloaded += 1
        print("{:.2%} completed".format((downloaded/len(dataLinks))))

driver()