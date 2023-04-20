from card import *

class AttackCard(Card):
    '''
    Class for scraping, organizing, and filtering attack cards from https://www.khguides.com/kh-com/attack-cards/.
    There should 27 unique attack cards.

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

    def __get_name(self):
        '''
        Get the names of all attack card keyblades
        '''

        soup = self.get_document()
        keyblades = soup.find_all('td', align='center', rowspan='6')
        
        for tag in keyblades:
            self.name.append(tag.text.strip())

    def __get_description(self):
        '''
        Default description to attack card description
        '''

        description = '''Attack cards will usually fill the majority of your deck, as these cards deal physical 
        (and sometimes, elemental) damage to enemies. Each attack card has unique properties that determines its 
        effectiveness in battle.
        '''
        
        self.description = [description] * 27

    def __get_obtained(self):
        '''
        Get the obtained description of all attack card keyblades
        '''

        soup = self.get_document()
        obtained = soup.findAll('td', align='center', text='Strike')
        
        for i in obtained:
            i = i.find_previous('td', rowspan='6')
            self.obtained.append(i.text.strip())

    def __get_element(self):
        '''
        Get the element type of all attack card keyblades
        '''

        soup = self.get_document()
        elements = soup.findAll('td', align='center', text='Element')

        self.__get_rank('element', elements)
        
    def __get_strike(self):
        '''
        Get the strike rank of all attack card keyblades
        '''

        soup = self.get_document()
        strikes = soup.findAll('td', align='center', text='Strike')

        self.__get_rank('strike', strikes)

    def __get_thrust(self):
        '''
        Get the thrust rank of all attack card keyblades
        '''

        soup = self.get_document()
        thrusts = soup.findAll('td', align='center', text='Thrust')

        self.__get_rank('thrust', thrusts)

    def __get_combo_finish(self):
        '''
        Get the combo finish rank of all attack card keyblades
        '''

        soup = self.get_document()
        finishes = soup.findAll('td', align='center', text='Combo Finish')

        self.__get_rank('combo_finish', finishes)

    def __get_break_recovery(self):
        '''
        Get the break recovery rank of all attack card keyblades
        '''

        soup = self.get_document()
        recoveries = soup.findAll('td', align='center', text='Break Recovery')

        self.__get_rank('recovery', recoveries)

    def __get_card_point(self):
        '''
        Get the card point rank of all attack card keyblades
        '''   

        soup = self.get_document()
        card_points = soup.findAll('td', align='center', text='Required CP')

        self.__get_rank('card_point', card_points)

    def __get_rank(self, stat, tags):
        '''
        Looks at the adjacent tag to obtain the rank
        '''

        rankings = []
        for i in tags:
            rank = i.findNext('td', align='center')
            rank = rank.text.strip()
            rankings.append('star' if rank == '☆' else rank)

        setattr(self, stat, rankings)

    def generate_csv(self):
        '''
        Generate a csv file of attack card attributes
        '''

        self.__get_name()
        self.__get_description()
        self.__get_obtained()
        self.__get_element()
        self.__get_strike()
        self.__get_thrust()
        self.__get_combo_finish()
        self.__get_break_recovery()
        self.__get_card_point()

        fields = ['name', 
                  'description', 
                  'obtained', 
                  'element', 
                  'strike',
                  'thrust',
                  'combo_finish',
                  'recovery',
                  'card_point']
        
        data = zip(self.name, 
                   self.description, 
                   self.obtained, 
                   self.element,
                   self.strike,
                   self.thrust,
                   self.combo_finish,
                   self.recovery,
                   self.card_point)
        
        with open('data/attack_cards.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

            for row in data:
                writer.writerow(row)