import numpy as np


class Env(object):

    def __init__(state):
        self.state = {}
        self.dealer_score = self.state['dealer_card']
        self.reward = 0

    def dealer(self, status):

        player_sum = self.state['player_sum']

        if(status == 'player_bust'):
            self.reward('dealer')
        elif(status == 'stick'):
            while(self.dealer_sum > 0 and self.dealer_sum < 17):
                dealer_policy()
            if(self.dealer_sum < 0 or self.dealer_sum > 21 or player_sum > dealer_sum):
                reward('player')
            elif(self.dealer_sum = player_sum):
                reward('draw')
            else:
                reward('dealer')
        elif(status == 'hit'):
            dealer_policy()
            if(self.dealer_sum < 0 or self.dealer_sum > 21 or player_sum > dealer_sum):
                reward('player')
            else:
                player_policy()



    def dealer_policy(self):

        if self.dealer_score > 17:
            return('stick')
        else:
            colour = 'red' if np.random.rand() > (1.0/3) else 'black'
            card = np.random.randint(1,14)
            if card > 10:
                card = 10
        if colour == 'red':
            self.dealer_sum = self.dealer_sum - card
        elif colour = 'black':
            self.dealer_sum = self.dealer_sum + card







    def step(self):

    dealer_card  = self.state ['dealer_card']
    player_sum = self.state['player_sum']
    action = self.state['action']

    if action = 'hit':

        colour = 'red' if np.random.rand() > (1.0/3) else 'black'
        card = np.random.randint(1,14)
        if card > 10:
            card = 10

        if colour == 'red':
            player_sum = player_sum - card
        elif colour = 'black':
            player_sum = player_sum + card

        if (player_sum > 21 or player_sum < 1):
            return('player_bust')
        else:
            return('hit')
    else:
        return('stick')

    def reward(self, winner):1
        if(winner = 'player'):
            self.reward = self.reward + 1
        elif(winner = 'dealer'):
            self.reward = self.reward - 1


    def player_policy(self, type = 'monte_carlo'):

        pass
