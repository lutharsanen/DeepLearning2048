# MA: own retry to understand code...
# #MA: needed imports/environments
import gym
import gym_2048
import random
import numpy as np
import json

env = gym.make('2048-v0')


# MA: Auto seeding. ok?
env.seed()
prev_state = env.reset()
done = False
moves = 0

#MA: create our dictionary of observed transitions (like lecture 2, slide 5)
#Ide: Whenever new State is observed, add element to S list and then update this, possibly a count of SA combinations?
SARS={}

#Unless absorbing state reached, play...
while not done:
    action = env.action_space.sample()
    env.render()
    next_state, reward, done, info = env.step(action)
    while np.all(prev_state == next_state): # loop that only "active" moves get counted
        #problem: how to update state-specific action space? i.e. "in this state move i not available"
        # is env.action_space alrady state specific? check next lines
        # env.action_space.remove(action) does not work, since discrete object. mutate to integer to change?
        # print(env.action_space)
        # create not_action_space(observation_space) += action or so and then chose from "in action_space&not in not_action_space(observation_space)"?
      print("\nPlease note that ", prev_state, action, " IS NON FEASIBLE COMBINATION & should give a reward of ", reward - 100)
      
      #MA: idea:add negative reawrd of -100 if this happens. should disincentivize "unfeasible moves" quickly
      #update SARS tuple. to be implemented:
      #   only 1 observation is needed to exlude it from future exploration. bigger negativ reward?
      #   alternative idea to disincentives, define proper action sets (env.action_space is always discrete(4) and anyway needs mutation. reconstruct?): 
      #     e.g. add state specific action set to SARS dictionary and update accordingly
      key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
      if key in SARS:
        value_string = SARS[key]
        value = json.loads(value_string)
        value[1] += 1
        SARS[key] = json.dumps(value)
      else:
        value = json.dumps({'reward': int(reward)-100, 'count': 1})
        #json did not support initial format of reward (int64).
        #no fear of overflow. python 3 int is limitless, liek long in python 2. (e.g. https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints)
        SARS[key] = json.dumps(value)

      action = env.action_space.sample() #chose random action, could be maintained to avoid dead ends (but not optimal strategy)
      next_state, reward, done, info = env.step(action)

    
    #update SARS tuple of successfull move.
    key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
    if key in SARS:
      value_string = SARS[key]
      value = json.loads(value_string)
      value[1] += 1
      SARS[key] = json.dumps(value)
    else:
      value = json.dumps({'reward': int(reward), 'count': 1})
      SARS[key] = json.dumps(value)
    moves += 1
    prev_state = next_state
    # above "tolist" from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    # reverse function: prev_state = np.array(key[0])

    print('Next Action: "{}"\n\nReward: {}'.format(
      gym_2048.Base2048Env.ACTION_STRING[action], reward)) #dont save action as string, but as discrete number. (just action?)
    #env.render() #only render here? not needed earlier to check prev_state ==next_state?

print('\nTotal Moves: {}'.format(moves))
print(SARS)
