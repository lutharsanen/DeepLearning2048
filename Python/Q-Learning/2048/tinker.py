import gym
import gym_2048
import random
import numpy as np
import functions as func

env = gym.make('2048-v0')
env.reset()

LEARNING_RATE = 0.001
DISCOUNT = 0.95
EPISODES = 25000000
GOAL = 256

SHOW_EVERY = 2000

epsilon = 0.5


#should tinker with 20
DISCRETE_OS_SIZE = [70] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high-env.observation_space.low)/ DISCRETE_OS_SIZE


#should tinker with -2 and 0
q_table = np.random.uniform(low = -1,high = 2, size = (DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return func.totuple(discrete_state.astype(np.int))

myenv = env.reset()
discrete_state = get_discrete_state(myenv)

done = False

for episode in range(EPISODES):
    
    while not done:

        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])

        else:
            action = np.random.randint(0, env.action_space.n)
        
        
        new_state, reward, done, _ = env.step(action)
        
        
        new_discrete_state = get_discrete_state(new_state)
        
        
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
           
           
            current_q = q_table[discrete_state]
           
            new_q = (1-LEARNING_RATE)* current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state] = new_q
           
        
        elif func.matrix_checker(GOAL,new_state):
            q_table[discrete_state] = 0
            env.render()
            print("You won")
        discrete_state = new_discrete_state
  