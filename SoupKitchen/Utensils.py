# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def MakeSoup(ref_page):
    '''
    Makes a BeautifulSoup object from a url.
    '''

    page = urlopen(ref_page)
    soup = BeautifulSoup(page, 'html.parser')

    return soup
