import gym
import gym_2048
import random
import numpy as np
import json
import functions as func


env = gym.make('2048-v0')
env.seed()
prev_state = env.reset()
done = False
moves = 0


SARS={}

while not done:
    action = env.action_space.sample()
    env.render()
    next_state, reward, done, info = env.step(action)
    while np.all(prev_state == next_state): 
        
      print("\nPlease note that ", prev_state, action, " IS NON FEASIBLE COMBINATION & should give a reward of ", reward - 100)
      
      key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
      if key in SARS:
        value_string = SARS[key]
        value = json.loads(value_string)
        print(value['count'])
        SARS[key] = json.loads(value)
      else:
        value = json.dumps({'reward': int(reward)-100, 'count': 1, 'invalid': True, 'Q^': 0})
        SARS[key] = json.loads(value)

      action = env.action_space.sample() 
      next_state, reward, done, info = env.step(action)

    key = json.dumps({'prev_state': prev_state.tolist(), 'action': action, 'next_state': next_state.tolist()})
    if key in SARS:
      value_string = SARS[key]
      value = json.dumps(value_string)
      print(value['count'])
      SARS[key] = json.loads(value)
    else:
      value = json.dumps({'reward': int(reward), 'count': 1, 'invalid': False, 'Q^': 0})
      SARS[key] = json.loads(value)
    moves += 1
    prev_state = next_state

    print('Next Action: "{}"\n\nReward: {}'.format(
      gym_2048.Base2048Env.ACTION_STRING[action], reward))
  

print('\nTotal Moves: {}'.format(moves))

with open('sars.json',"w") as f:
  f.write(SARS)

print(type(SARS))
print(type(value))