import numpy as np

from environment import *

class Policy(object):

	def __init__(self, value_function, freq, initialize = True):

		dealer_card_states = np.arange(1,11)
		num_dealer_states = 10

		player_sum_states = np.arange(1, 22)
		num_player_states = 21

		self.actions = ['hit', 'stick']
		num_actions = 2


		if  initialize == True:
			self._value_function = np.zeros((num_dealer_states, num_player_states, num_actions))
			self._freq = np.zeros((num_dealer_states, num_player_states, num_actions))
		else:
			self._value_function = value_function
			self._freq = freq

		self.environment = Environment()

	def return_params(self):

		params = {value_function: self._value_function,
				  counter: self._freq}

		return params


class Monte_Carlo_Policy(Policy):

	def __init__(self,initialize, value_function, freq):

		super().__init__(initialize,value_function, freq)
		self.n0 = 100
		self.visits = []


	def policy(self):
		while (self.environment.state.terminal == False):

			dealer_card  = self.environment.state.dealer_card
			player_sum = self.environment.state.player_sum


			_epsilon =  self.n0 / (self.n0 + np.sum(self._freq[dealer_card][player_sum]) )

			if(np.random.rand() < _epsilon):
				 action = np.random.randint(0,2)
			else:
				 action = np.argmax(self._value_function[dealer_card][player_sum])

			self.visits.append([dealer_card, player_sum, action])

			self._freq[dealer_card, player_sum, action] += 1

			self.environment.step(self.actions[action])

		self.update_value_function()

	def update_value_function(self):

		reward = self.environment.last_reward

		for visit in visits:
			[ dealer_card, player_sum, action ]= visit
			_value_function[dealer_card][player_sum][action] = __value_function[dealer_card][player_sum][action] + reward/self._freq[dealer_card][player_sum][action]
