from card import *

class EnemyCard(Card):
    '''
    Class for scraping, organizing, and filtering enemy cards from https://www.khguides.com/kh-com/enemy-cards/.
    There should 59 unique enemy cards.

    Attributes
    ----------

    Public:

        Inherited Card attributes...
    '''

    def __init__(self):
        '''
        Creates a new instance of EnemyCard
        '''
                
        item_url = 'https://www.khguides.com/kh-com/enemy-cards/'
        Card.__init__(self, item_url)

        self.ability = []
        self.card_point = []

    def __get_name(self):
        '''
        Get the names of all enemy cards
        '''

        soup = self.get_document()
        enemies = soup.find_all('td', align='center')
        
        for tag in enemies:
            self.name.append(tag.text.strip())

    def __get_ability(self):
        '''
        Get the ability of all enemy cards
        '''

        soup = self.get_document()
        abilities = soup.find_all('td', align='center')
        
        for tag in abilities:
            next_tag = tag.find_next('td')
            self.ability.append(next_tag.text.strip())

    def __get_desription(self):
        '''
        Get the obtained description of all enemy cards
        '''

        soup = self.get_document()
        obtained = soup.find_all('td', align='center')
        
        for tag in obtained:
            next_tag = tag.find_next('td').find_next('td')
            self.description.append(next_tag.text.strip())

    def __get_card_point(self):
        '''
        Get the obtained description of all enemy cards
        '''

        soup = self.get_document()
        card_points = soup.find_all('td', align='center')
        
        for tag in card_points:
            next_tag = tag.find_next('td').find_next('td').find_next('td')
            self.card_point.append(next_tag.text.strip())

    def generate_csv(self):
        '''
        Generate a csv file of enemy card attributes
        '''

        self.__get_name()
        self.__get_ability()
        self.__get_desription()
        self.__get_card_point()

        fields = ['name', 
                  'ability',
                  'description', 
                  'card_point']
        
        data = zip(self.name,
                   self.ability,
                   self.description, 
                   self.card_point)
        
        with open('data/enemy_cards.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

            for row in data:
                writer.writerow(row)

test= EnemyCard()
test.generate_csv()