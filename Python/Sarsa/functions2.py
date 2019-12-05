import numpy as np
import matplotlib as plt
import ast



def maxAction(Q, state):
    values = np.array([Q[state,a] for a in range(4)])
    action = np.argmax(values)
    return action

def choseandcheck(Q, a, observation, EPSILON, env, s):
    rand = np.random.random()
    if rand < (1-EPSILON):
        a = maxAction(Q,s)
    else:
        a = np.random.randint(0,4)
   # print(env.step(a), a)
    new_state, reward, done, _ = env.step(a)
    observation_ = numpy_transformer_light(new_state)
    #print(observation_, '\n\n', observation)
    while observation==observation_:
        #print("REACHED)")
        Q[s,a] = float(-1000000)
        rand = np.random.random()
        if rand < (1-EPSILON):
            a = maxAction(Q,s)
        else:
            a = np.random.randint(0,4)
            
        new_state, reward, done, _ = env.step(a)
        observation_ = numpy_transformer_light(new_state)
        
    return a, observation_, reward, done




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


def plotLearning(x, scores, epsilons, filename, lines=None):
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)

    ax.plot(x, epsilons, color="C0")
    ax.set_xlabel("Game", color="C0")
    ax.set_ylabel("Epsilon", color="C0")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C0")

    N = len(scores)
    running_avg = np.empty(N)
    for t in range(N):
	    running_avg[t] = np.mean(scores[max(0, t-20):(t+1)])

    ax2.scatter(x, running_avg, color="C1")
    #ax2.xaxis.tick_top()
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()
    #ax2.set_xlabel('x label 2', color="C1")
    ax2.set_ylabel('Score', color="C1")
    #ax2.xaxis.set_label_position('top')
    ax2.yaxis.set_label_position('right')
    #ax2.tick_params(axis='x', colors="C1")
    ax2.tick_params(axis='y', colors="C1")

    if lines is not None:
        for line in lines:
            plt.axvline(x=line)

    plt.savefig(filename)

#f1 = open('states.txt', 'r')
#mylist = ast.literal_eval(f1.read())





