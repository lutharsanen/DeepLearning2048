import gym
import gym_2048
import random
import numpy as np
import functions as func

env = gym.make('2048-v0')
env.reset()

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000
GOAL = 2048


#print(env.observation_space.high)
#print(env.observation_space.low)
#print(env.action_space.n)

#should tinker with 20
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high-env.observation_space.low)/ DISCRETE_OS_SIZE


#should tinker with -2 and 0
q_table = np.random.uniform(low = -2,high = 0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))

print(len(env.observation_space.high))
#print(len(q_table[0][0][0][0]))


def get_discrete_state(state):
    return func.totuple(state.astype(np.int))


print(np.random.random())

#env.close()