import numpy as np

from environment import *

class Policy():

	def __init__(value_function = None, freq = None):

		dealer_card_states = np.arange(1,11)
		num_dealer_states = dealer_card_states.shape[0]

		player_sum_states = np.arange(1, 22)
		num_player_states = player_sum_states.shape[0]

		self.actions = ['hit', 'stick']
		num_actions = len(self.actions)


		if(value_function == None and freq == None):
			self._value_function = np.zeros((dealer_card_states, num_player_states, num_actions))
			self._freq = np.zeros((dealer_card_states, num_player_states, num_actions))
		else:
			self._value_function = value_function
			self._freq = freq

		self.environment = Environment()

	def return_params(self):

		params = {value_function: self._value_function,
				  counter: self._freq}

		return params


class Monte_Carlo_Policy(Policy):

	def __init__(self, value_function = None, freq = None):

		Policy.__init__(value_function, freq)
		self.n0 = 100
		self.visits = []


	def policy(self):
		while (self.environment.state.terminal == False):

			dealer_card  = environment.state.dealer_card
			player_sum = environment.state.player_sum


			_epsilon =  self.n0 / (self.n0 + _np.sum(freq[dealer_card][player_sum]) )

			if(np.random.rand() < _epsilon):
				 action = np.random.randint(1,3)
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
			self._value_function[dealer_card][player_sum][action]  =  _self._value_function[dealer_card][player_sum][action] + reward/self._freq[dealer_card][player_sum][action]
