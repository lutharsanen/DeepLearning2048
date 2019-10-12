import gym_2048
import gym


if __name__ == '__main__':
  env = gym.make('2048-v0')

  ########edited from Lu#############
  max = 0
  for i in range(1):
  ###################################  
    env.seed(i)
    env.reset()
    #env.render()

    done = False
    moves = 0
    while not done:
      action = env.np_random.choice(range(4), 1).item()
      print(action)
      next_state, reward, done, info = env.step(action)
      moves += 1

      #print('Next Action: "{}"\n\nReward: {}'.format(
      #  gym_2048.Base2048Env.ACTION_STRING[action], reward))
      #env.render()

    ########edited from Lu#############
    if moves > max :
      max = moves
    ###################################
    
  #print('\nTotal Moves: {}'.format(max))

  print('\nTotal Moves: {}'.format(moves))