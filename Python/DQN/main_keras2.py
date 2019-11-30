from dqn2 import Agent
import numpy as np
import gym
import gym_2048
import functions as f

if __name__ == '__main__':
    env = gym.make('2048-v0')
    n_games = 500
    agent = Agent(gamma = 0.99, epsilon = 1.0 , alpha = 0.0005, input_dims = 16, n_actions = 4, mem_size = 10_000_000, batch_size = 64, epsilon_end=0.01)

    scores = []
    eps_history = []

    for i in range(n_games):
        done = False
        score = 0
        observation = env.reset()
        observation_trans = list(f.numpy_transformer(observation))
        print(type(observation_trans))
        while not done:
            action = agent.choose_action(observation_trans)
            observation_ , reward, done, _ = env.step(action)
            score += reward
            observation_trans_ = f.numpy_transformer(observation_)
            agent.remember(observation_trans, action, reward, observation_trans_, done)
            observation_trans = observation_trans_
            agent.learn()

        eps_history.append(agent.epsilon)
        scores.append(score)

        avg_score = np.mean(scores[max(0, i-100):(i+1)])
        print('episode', i , 'score%.2f'%score, 'average score %.2f'%avg_score)

        if i %10 == 0 and i>0:
            agent.save_model()

    filename = '2048.png'

    x = [i+1 for i in range(n_games)]
    f.plotLearning(x,scores, eps_history, filename)