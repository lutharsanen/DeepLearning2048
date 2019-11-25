import random 
import numpy as np
import gym_2048
import gym

env = gym.make('2048-v0')

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 25000
GOAL = 2048


#should tinker with 20
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high-env.observation_space.low)/ DISCRETE_OS_SIZE



def matrix_checker(checker, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if checker == matrix[i][j]:
                return True
    return False

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

