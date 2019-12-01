import numpy as np
import matplotlib as plt
import ast



def maxAction(Q, state):
    values = np.array([Q[state,a] for a in range(4)])
    action = np.argmax(values)
    return action

def numpy_transformer(matrix):
    lst = []
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    lst.append(int(matrix[i][j]))
    return lst

def largest_number(env):
    value = env.observation_space.high[0][0]
    return int(value)

def get_max(state):
    max_value = max(state)
    return max_value




#f1 = open('states.txt', 'r')
#mylist = ast.literal_eval(f1.read())





