from card import *

class FriendCard(Card):
    '''
    Class for scraping, organizing, and filtering friend cards from https://www.khguides.com/kh-com/friend-cards/.
    There should 10 unique friend cards.

    Attributes
    ----------

    Public:

        Inherited Card attributes...
    '''

    def __init__(self):
        '''
        Creates a new instance of ItemCard
        '''
                
        item_url = 'https://www.khguides.com/kh-com/friend-cards/'
        Card.__init__(self, item_url)

    def __get_name(self):
        '''
        Get the names of all friend cards
        '''

        soup = self.get_document()
        friends = soup.find_all('td', align='center')
        
        for tag in friends:
            self.name.append(tag.text.strip())

    def __get_description(self):
        '''
        Get the description of all friend cards
        '''

        soup = self.get_document()
        description = soup.find_all('td', align='center')
        
        for tag in description:
            next_tag = tag.find_next('td')
            self.description.append(next_tag.text.strip())

    def __get_obtained(self):
        '''
        Get the obtained description of all friend cards
        '''

        soup = self.get_document()
        obtained = soup.findAll('td', align='center')
        
        for tag in obtained:
            next_tag = tag.find_next('td').find_next('td')
            self.obtained.append(next_tag.text.strip())

    def generate_csv(self):
        '''
        Generate a csv file of friend card attributes
        '''

        self.__get_name()
        self.__get_description()
        self.__get_obtained()

        fields = ['name', 
                  'description', 
                  'obtained']
        
        data = zip(self.name, 
                   self.description, 
                   self.obtained)
        
        with open('data/friend_cards.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

            for row in data:
                writer.writerow(row)

test = FriendCard()
test.generate_csv()