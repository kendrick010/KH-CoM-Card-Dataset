from bs4 import BeautifulSoup
import requests
import re

class Card:
    '''
    Base class for battle cards

    Attributes
    ----------

    Public:

        name : list, card name
        description : list, description of card
        obtained : list, where/how to obtain card
    '''

    def __init__(self, url):
        '''
        Creates a new instance of Card
        '''

        self.name = []
        self.description = []
        self.obtained = []
        self.url = url

    def get_document(self):
        '''
        Method that returns BeautifulSoup object representing document

        :return: BeautifulSoup object
        '''
    
        document_html = requests.get(self.url).text
        soup = BeautifulSoup(document_html, 'html.parser')

        return soup

