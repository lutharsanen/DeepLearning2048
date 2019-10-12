import gym_2048
import gym
import random 
import numpy as np

if __name__ == '__main__':
  env = gym.make('2048-v0')

  ########edited from Lu#############
  #max = 0
  #for i in range(1):
  ###################################  
  env.seed(random.randint(0,100))
  env.reset()
  #env.render()

  next_state = 0
  done = False
  moves = 0
  action_set = [0,1,2,3]
  while not done:
    action = 0
    prev_state = next_state
    next_state, reward, done, info = env.step(action)
    ########edited from Lu#############
    temp_action_set = action_set
    while np.array_equal(prev_state,next_state):
      action = (action + 1)%4
      next_state, reward, done, info = env.step(action)
       ###################################  
    moves += 1

    print('Next Action: "{}"\n\nReward: {}'.format(
      gym_2048.Base2048Env.ACTION_STRING[action], reward))
    env.render()

    ########edited from Lu#############
    #if moves > max :
    #  max = moves
    ###################################
    
  #print('\nTotal Moves: {}'.format(max))

  print('\nTotal Moves: {}'.format(moves))