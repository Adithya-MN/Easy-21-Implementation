import numpy as np



class State():

	def __init__(self):

		self.dealer_card = Environment.get_card(force_black = True)
		self.player_sum = Environment.get_card(force_black = True)
		self.terminal = False



class Environment(object):

	def __init__(self):


		self.state = State()
		self.dealer_sum = self.state.dealer_card
		self.last_reward = 0
		self.reward = 0



	def dealer(self, player_action):


		if(player_action == 'stick'):
			while(self.dealer_sum > 0 and self.dealer_sum < 17):
				self.dealer_sum += Environment.get_card()
			if(self.dealer_sum < 0 or self.dealer_sum > 21 or self.state.player_sum > self.dealer_sum):
				self.reward('won')
			elif(self.dealer_sum == self.state.player_sum):
				self.reward('draw')
				self.last_reward = 0
			else:
				self.reward('lost')
		elif(player_action == 'hit'):
			if(self.status.dealer_score > 16):
				self.dealer_sum += Environment.get_card()
			if(self.dealer_sum < 0 or self.dealer_sum > 21):
				self.reward('won')


	@classmethod
	def get_card(cls,force_black = False):

		colour = 'black' if np.random.rand() > (1.0/3) or force_black else 'red'

		card= np.random.randint(1,14)
		if card > 10:
			 card = 10

		return(-1*card if colour == 'red' else card)


	def step(self, action):


		dealer_card  = self.state.dealer_card
		player_sum = self.state.player_sum

		if action == 'hit':

			self.state.player_sum += Environment.get_card()

			if (self.state.player_sum > 21 or self.state.player_sum < 1):
				self.reward('loss')
			else:
				self.dealer(action)
		elif(action == 'stick'):
			self.dealer(action)


	def reward(self, player_result):

		self.state.terminal = True
		if(player_result == 'won'):
			self.reward = self.reward + 1
			self.last_reward = 1

		elif(player_result == 'lost'):
			self.reward = self.reward - 1
			self.last_reward = -1

		elif(player_result == 'draw'):
			self.last_reward = 0
