import gym
import gym_2048
import random
import numpy as np

env = gym.make('2048-v0')
env.reset()


def numpy_transformer(matrix):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lst.append(int(matrix[i][j]))
    return lst



done = False

    
while not done:
    list
    new_state, reward, done, _ = env.step(1)
    print(new_state)
    new = numpy_transformer(new_state)
    print(type(new[0]))
    break
