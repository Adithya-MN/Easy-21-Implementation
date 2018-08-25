from Easy21 import *
import numpy as np


def monte_carlo_policy():

	card= np.random.randint(1,14)
	if card > 10:
		 card = 10

	state= {dealer_card : card,
			  player_sum : 0,
			  action : 'hit'}

	environment = Env(state)


	dealer_card_states = np.arange(1,14)
	num_dealer_states = dealer_card_states.shape[0]

	player_sum_states = np.arange(1, 22)
	num_player_states = player_sum_states.shape[0]

	actions = ['hit', 'stick']
	num_actions = len(actions)

	_value_function = np.zeros((dealer_card_states, num_player_states, num_actions))

	_freq = np.zeros((dealer_card_states, num_player_states, num_actions))

	N0 = 100

	visits = []

	while (environment.terminal_state == False):

		dealer_card  = environment.state ['dealer_card']
		player_sum = environment.state['player_sum']
		action = environment.state['action']


		_epsilon =  N0 / (N0 + _np.sum(freq[dealer_card][player_sum]) )

		if(np.random.rand() < _epsilon):
			 action = np.random.choice(['hit', 'stick'])
		else:
			 action = np.argmax(_value_function[dealer_card][player_sum])
			 environment.state['action'] = actions[action]

		visits.append([dealer_card, player_sum, action])

		environment.step()

	reward = environment.last_reward

	for visit in visits:
		[ dealer_card, player_sum, action ]= visit
		_value_function[dealer_card][player_sum][action]  =  __value_function[dealer_card][player_sum][action] + reward/_freq[dealer_card][player_sum][action]
