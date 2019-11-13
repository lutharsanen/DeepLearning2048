# Dear Rob, we hope our "2048-project"-report won't be too troublesome...

# First, we import all the packages we will need for the non-deep part, where we try to calculate Q values by tabular form.
import gym
import gym_2048
import random
import numpy as np
import json
import functions as func

# We chose an environment, that is made available on github by 'activatedgeek': https://github.com/activatedgeek/gym-2048
env = gym.make('2048-v0')

#idea to repeat multiple times.... here only 10 episodes per batch
episode = 0
while episode < 10:
# We do not save the actual seeds, since all probabilities are drawn from the same distribution
# see: 'env.py' by activatedgeek, 47-49 for random seeding, 81ff. and 94ff. for random generation of tiles, (prob=0.9 that a 2-tile is generated, prob=0.1 that 4-tile is generated 
	env.seed()
# generate intila state. to check whether a move was succesfull (i.e. something changed) we will save the initial state (will be updated after eachs succesfull step)
	prev_state = env.reset()
# if done = True --> absorbing state has been reached (i.e. episode finished), plus count succesfull moves of the episode, set as 0 to start
	done = False
	moves = 0
# do we actually need to count moves in an episode?
#MA: create our dictionary of observed transitions (like lecture 2, slide 5)
#Ide: Whenever new State is observed, add element to SARS list and then update this, possibly a count of SAS' combinations?
	SARS={}
#Unless absorbing state reached, play...
	while not done:
		action = env.action_space.sample()
# env.render() could be dropped, if not needed to generate output for user. (sone so below)
		env.render()
		next_state, reward, done, info = env.step(action)
# if "nothing changed", i.e. unfeasible move denoted "invalid", add line to table and chose new action
		while np.all(prev_state == next_state):
			key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
			value = json.dumps({'reward': int(reward)-100, 'count': 1, 'invalid': True, 'Q^': 0})
			SARS[key] = json.loads(value)
#chose random action, could be maintained to avoid dead ends (but not optimal strategy)
			action = env.action_space.sample()
			next_state, reward, done, info = env.step(action)
#update SARS tuple of successfull move in table (add if necessary)
		key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
		if key in SARS:
			value_string = SARS[key]
			value = json.dumps(value_string)
			value['count'] += 1
			SARS[key] = json.loads(value)
		else:
			value = json.dumps({'reward': int(reward), 'count': 1, 'invalid': False, 'Q^': 0})
			SARS[key] = json.loads(value)
#do wee need moves-count?
		moves += 1
		prev_state = next_state
# above "tolist" from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
# reverse function: prev_state = np.array(key[0])
# "invalid" added to later define state specific action_spaces --> then, negativ reward for unfesaible moves not needed
# Q^ added as zero, arbitrary pessimistic start
	episode += 1
	env.reset()
with open('sars.json',"w") as f:
  f.write(str(SARS))

















 
