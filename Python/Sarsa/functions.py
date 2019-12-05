import numpy as np
import matplotlib.pyplot as plt
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
    return tuple(lst)

def numpy_transformer_light(matrix):
    lst = []
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    lst.append(int(matrix[i][j]))
    return lst


def get_max(state):
    max_value = max(state)
    return max_value


def plotLearning(x, y):
    plt.scatter(x,y, label = 'skitscat', color = 'k', s=25 , marker = 'o')
    plt.xlabel('episodes')
    plt.ylabel('reward')
    plt.title('Sarsa')
    plt.legend


