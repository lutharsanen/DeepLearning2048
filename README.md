# DeepLearning2048

Our objective was to program an algorithm, which solves the game 2048 with Reinforcement Learning methods. The goal of the game 2048 is to combine two same-value numbered tiles, so that they merge and result in their sum, to finally attain the tile 2048. However, in the game it is possible to attain higher numbers. Nonetheless, after attaining 2048 the player has won the game. 

For our project, we have used three methods, namely Q-Learning, SARSA and Deep Q-learning to implement the learning. We used an open AI environment from gym and installed the version gym-2048. This environment has an output of a state space with a 4x4 matrix. We have mostly transformed this 4 x 4 matrix into a list with 16 elements to make it easier to use them in the model. The discrete action space consists of four elements for all the states, even if a particular action would be unfeasible in a specific state. We had to control for this in our tabular models, but the Deep-Q learning appeared to avoid this problem by itself. The four different actions possible were: swipe up, swipe right, swipe down and swipe left. The reward was given by the environment as the sum of merged cells in a step. The goal of our models is to maximize the sum of the rewards to solve the 2048 task. We ran multiple versions of code with very mixed results, even in terms of getting software and code to work. Unfortunately, we could not solve the problem to save agents’ progress, i.e. we were not able to import/export Q-tables or neural weightings during this project.

To visualize and interpret the learning process, we are using different graphs and plots. We will divide most of our episodes into groups corresponding to percentiles (always 100 groups). We expect to see an improvement from one batch to the next batch. With our plots we will analyse the win statistics. In each test-run we will define a winning rate - we are going to set a tile number as a goal and count how often the model has achieved this goal. The goal was set at 256 to obtain meaningful win statistics with tabular models. Other plotted statistic will present the maximum value tile reached, the average maximum tile reached, and the average rewards obtained by the interaction with the environment. In all plots, we expect an improvement of the calculated values, especially for the “average reward” statistic (which should be optimized by the models). As a comparison for performance we had an agent act randomly at any point. If they fail to outperform such an agent our models may not have learned much.

### Q-Learning test series: experimental design &amp; results

Our Q-Learning agents vary along two dimensions. There are two epsilon schemes; whereas one is a monotonously linearly decreasing epsilon, floored at 0.01 the other scheme is a discontinuous epsilon development with multiple discontinuous jumps of epsilon to a higher level. This should reduce the risk of ending up at a non-optimal solution by continuously varying exploration and exploitation. The other varying dimension are the alphas, chosen at 0.1, 0.5 and 0.8. After 5000 training episodes, there are performance tests with 500 episodes. Results are always expressed in percentiles, thus the average result over the percentiles (100 datapoints, in test mode 5 episodes are pooled to one datapoint).

As a comparison for the performance metrics we also specified 2 random agents, that randomly chose an action at any point for 5000 episodes. Those 2 agents still perform tabular computations of Q values with alpha = 0.5 and 0.8. The performance of these are again tested for 500 episodes with epsilon=0. Therefore, we can compare whether the other parametrizations outperform the ones learning off a random agent to evaluate the parametrizations&#39; effectiveness. Thus, there are 2x3 +2=8 specifications for testing and comparison.

Q-Learning summary table of parametrizations and main performance measures after 5000 training episodes1. The random agents&#39; performance is measured from 5000 training episodes.

| alpha | epsilon | Win percentage | Avg max tile | Avg reward |
| --- | --- | --- | --- | --- |
| Alpha = 0.5\* | 1, training | 0.047 | 94.97 | 955.65 |
| Test with eps=0 | 0.104 | 106.61 | 1213.52 |
| Alpha = 0.8\* | 1, training | 0.045 | 94.40 | 959.35 |
| Test with eps=0 | 0.086 | 107.60 | 1281.7 |
| Alpha = 0.1 | Monotonous | 0.044 | 86.99 | 1017.93 |
| Alpha = 0.1 | Nonmonotonous | 0.067 | 93.18 | 1037.97 |
| Alpha = 0.5 | Monotonous | 0.094 | 108.61 | 1256.05 |
| Alpha = 0.5 | Nonmonotonous | 0.115 | 107.11 | 1240.44 |
| Alpha = 0.8\* | Monotonous | 0.126\*\* | 109.64 | 1273.13 |
| Alpha = 0.8\* | Nonmonotonous | 0.100\*\* | 109.42 | 1260.52\*\* |

\*The automatic average performance calculations have been added in time for the models with alpha = 0.8 and the random agents. Those numbers do not contain compounded rounding errors.
\*\*These estimates differ from the manual calculations, by -0.024 (monotonous win %) and +0.01 / -0.23 (non-monotonous win % / avg reward). The effect on the main variable avg reward is negligible, whereas the win % may have lost some comparative power as statistic.

### Q-Learning test series: comparison

Agents with alpha = 0.1 fail to clearly outperform the random agent (epsilon=1, training) and only slightly outperform randomness by the average reward measure. Nevertheless, Q learning off the random agent outperformed those low alpha models. Alpha = 0.5 and Alpha= 0.8 performed comparably well and both outperformed random agent and Q learning off random agent in all measures. Tabular Q learning does not seem suitable to low levels of alpha, like 0.1, at least early in the learning process.

There does not seem to be a clear favourite among the epsilon schemes. The non-monotonous schemes tend to perform better in low alpha specifications. whereas the monotonous scheme seems superior at alpha = 0.8. At alpha = 0.5, there is conflicting evidence: the monotonous scheme slightly outperforms regarding average max tile and average reward but falls short of the non-monotonous scheme in the probability to reach the tile 256 (win %). Nevertheless, the differences are rather small and further testing would be needed for conclusive results.

Rather surprisingly to us, Q Learning off a random agent is quite successful and with alpha=0.8 is the best performing Q-Learning model. This might suggest that an epsilon decay scheme at a slower rate might be a successful alternative specification, as high epsilons only seem to decrease training performance, but affects less the testing performance with full exploitation.

### Q-Learning test series: conclusion

The main problem of Q Learning (or tabular learning in general) in the 2048-game is the vast state space that needs quite some computational power, especially as the game progresses, to keep track of the tabular information. If agents were to reach higher tiles, the possible state space increases exponentially, and our hardware would probably reach its limit.

Nevertheless, we gained some insight about suitable alpha levels and possible scopes of epsilon schemes for tabular Q-Learning. Very low alphas tend to perform poorly, failing to beat a random agent after 5000 episodes. Epsilon schemes might even decrease at very low rates and still obtain good results, as the test results from learning off random agents suggest decent results from pure exploration as a start. Our specifications with alpha = 0.5 and 0.8 fared comparably well. As a comparison for DQN we will later on take the best performing agent (alpha = 0.8, monotonous epsilon scheme) as additional baseline for performance evaluation.
