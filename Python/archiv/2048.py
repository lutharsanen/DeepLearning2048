import gym_2048
import gym
import random 
import numpy as np



if __name__ == '__main__':
  env = gym.make('2048-v0')

  ########edited from Lu#############
  max = 0
  state_nr = 0
  for i in range(280):
  ###################################  
    env.seed(i)
    env.reset()
    #env.render()

    next_state = 0
    done = False
    moves = 0
    action_set = [0,1,2,3]
    while not done:
      ## Cmt Ma: Verstehe den code nicht...Output scheint inkonsistent
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

    ########edited from Lu#############
    if moves > max :
      max = moves
      state_nr = i
    ###################################
    
  print('\nTotal Moves: {}'.format(max))
  print(state_nr)

  #print('\nTotal Moves: {}'.format(moves))