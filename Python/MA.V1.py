# MA: own retry to understand code...
# #MA: needed imports/environments
import gym
import gym_2048
import random
import numpy as np

env = gym.make('2048-v0')

#MA: for random generator
i = random.randint(0,100)
# MA: print not needed, but maybe save/log the generated seed for each episode? 
print(i)
env.seed(i)
state_init = env.reset()
#MA: note, not always same start 
# (sometimes only 1x "2", sometimes 2x "2", sometimes 1x"2" & 1x"4")
# for moves_check at end
sum_init = np.sum(state_init)


done = False
moves = 0
while not done:
    print(env.action_space)
    action = env.np_random.choice(range(4), 1).item()
    next_state, reward, done, info = env.step(action)
    moves += 1

    print('Next Action: "{}"\n\nReward: {}'.format(
      gym_2048.Base2048Env.ACTION_STRING[action], reward))
    env.render()

print('\nTotal Moves: {}'.format(moves))
#MA check "sum of all tiles: np.sum(next_state)), sum_init line 19
print("Sum at beginning : ",sum_init)
sum_end = np.sum(next_state)
print("Sum at end: ", sum_end)
sum_diff = np.subtract(sum_end,sum_init)
print(sum_diff)
moves_check = sum_diff/2
print("There have been ", moves_check," successful moves")
#MA: to check that sum_init is correct
# print(state_init)