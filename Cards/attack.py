from card import *

class AttackCard(Card):
    '''
    Class for scraping, organizing, and filtering attack cards from https://www.khguides.com/kh-com/attack-cards/.
    There shoudl 27 unique attack cards.

    Attributes
    ----------

    Public:

        Inherited Card attributes...

        element: list, element-type
        strike: list, strike rank
        thrust: list, thrust rank
        combo_finish: list, combo finish rank
        recovery: list, break recovery rank
        card_point: list, card point rank
    '''

    def __init__(self):
        '''
        Creates a new instance of AttackCard
        '''
                
        attack_url = 'https://www.khguides.com/kh-com/attack-cards/'
        Card.__init__(self, attack_url)

        self.element = []
        self.strike = []
        self.thrust = []
        self.combo_finish = []
        self.recovery = []
        self.card_point = []

    def get_name(self):
        '''
        Get the names of all attack card keyblades
        '''

        soup = self.get_document()
        keyblades = soup.find_all('td', align='center', rowspan='6')
        
        for tag in keyblades:
            self.name.append(tag.text.strip())

    def get_description(self):
        '''
        Default description to attack card description
        '''

        description = '''Attack cards will usually fill the majority of your deck, as these cards deal physical 
        (and sometimes, elemental) damage to enemies. Each attack card has unique properties that determines its 
        effectiveness in battle.
        '''
        
        self.description = [description] * 27

    def get_element(self):
        '''
        Get the element of all attack card keyblades
        '''

        soup = self.get_document()
        elements = soup.findAll('td', align='center', text='Element')

        for tag in elements:
            element = tag.findNext('td', align='center')
            self.element.append(element.text.strip())

        




test = AttackCard()
test.get_element()
print(test.element)