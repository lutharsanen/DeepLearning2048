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

### SARSA test series: experimental design &amp; results

Analogous to Q-Learning, our SARSA agents vary along two dimensions. There are two epsilon schemes; whereas one is a monotonously linearly decreasing epsilon, floored at 0.01, whereas the other scheme is a discontinuous epsilon development with multiple discontinuous resets of epsilon to a higher level. This should reduce the risk of ending up at a non-optimal solution by continuously varying exploration and exploitation. The other varying dimension are the alphas, chosen at 0.1, 0.5 and 0.8. After 5000 training episodes, there are performance tests with 500 episodes. Results are mostly expressed in percentiles, thus the average result over the percentiles (100 datapoints, in test mode 5 episodes are pooled to one datapoint) are presented2.

Analogous to Q-Learning we also specified 2 random agents with alpha = 0.5 and 0.8 respectively to evaluate performance of the different parametrizations&#39; effectiveness. Thus, there are 2x3 +2\*2=10  specifications for testing and comparison.

SARSA summary table of parametrizations and main performance measures after 5000 training episodes3

| alpha | epsilon | Win percentage | Avg max tile | Avg reward |
| --- | --- | --- | --- | --- |
| Alpha = 0.5
random agent | 1, training | 0.046 | 95.72 | 964.91 |
| Test with eps=0 | 0.08 | 101.01 | 1184.7 |
| Alpha = 0.8
random agent | 1, training | 0.045 | 95.77 | 966.65 |
| Test with eps=0 | error | 105.54 | 1234.28 |
| Alpha = 0.1 | Monotonous | 0.034 | 87.73 | 996.02 |
| Alpha = 0.1 | Nonmonotonous | 0.046 | 95.07 | 1030.42 |
| Alpha = 0.5 | Monotonous | 0.105 | 111.10 | 1299.20 |
| Alpha = 0.5 | Nonmonotonous | 0.151 | 115.94 | 1332.19 |
| Alpha = 0.8 | Monotonous | 0.076 | 110.00 | 1266.85 |
| Alpha = 0.8 | Nonmonotonous | 0.090 | 105.29 | 1233 |

### SARSA test series: comparison

Considering the alpha, which is the learning rate, agents with alpha = 0.1, irrespective of the epsilon decay, failed to beat the random agent across all measures. Only for average reward, those models slightly outperformed the random strategy. The model with alpha 0.5 and 0.8 managed to beat the random agent across all measures and outperformed most of the SARSA models learning off the random agent. With alpha=0.8 the results were comparable to the learning off random agents. The agents with alpha = 0.5 outperformed with respect to all measures. So, we expect the globally optimal value of alpha for the SARSA model around that value. Given that alpha 0.8 does not perform much worse, the actual optimal value might be somewhere between, i.e. in the range (0.5, 0.8). Further testing is needed to specify the optimal range.

Comparing the results of the non-monotonous epsilon decay and the monotonous epsilon decay, non-monotonous epsilon decay outperforms monotonous epsilon decay, where learning state is increasing and, in a state, where the learning state is decreasing the monotonous epsilon decays the non-monotonous epsilon. It is difficult to make a conclusion about the alpha level 0.5. In our experiment it is the best performing, but if there was more time, there is a possibility that the global maximum is at an intermediate level the varying decay schemes effect is unclear. In our case, the non-monotonous scheme appears marginally superior Due to time restrictions we unfortunately couldn&#39;t test this hypothesis, but this would be our best guess.

Thus, we can conclude that the learning rate alpha has a much bigger influence on the result of the model than the decay scheme of epsilon.

### Q-Learning test series: conclusion

Analogous to the Q-Learning models, tabular SARSA is challenging due to the vast state space. Nevertheless, we gained some insight about suitable alpha levels and possible scopes of epsilon schemes for SARSA. Very low alphas tend to perform poorly, failing to beat a random agent after 5000 episodes of learning. Epsilon schemes might even decrease at very low rates and still obtain good results, as the test performance from learning off random agents suggest decent results from pure exploration as a start. As a comparison for DQN we will later on take the best performing agent (alpha = 0.5, non-monotonous epsilon scheme) as additional baseline for performance evaluation.

### Comparing Q-Learning and SARSA

Neglecting the specifications with alpha =0.1, which performed poorly with both methods, there is little evidence for actual superiority of one. The results from SARSA and Q-Learning are very similar. Asa a tendency, SARSA seems more challenged by high alphas in the range of 0.8 and might therefore have a lower optimal alpha level than Q-Learning. SARSA is a somewhat richer model that takes into consideration the momentaneous exploration rate when building its expectations of future reward (i.e., Q Value). This can also be seen by the slight outperformance of SARSA when learning off a random agent. Q-Learning seems less successful for the problem at hand. To our surprise, the best test performance resulted when learning with a=0.8 off the random agent. This result might be driven by our earlier observation that observing and learning from random strategies might be a good starting point for initial learning.

### DQN test series: experimental design &amp; results

We vary our specifications along three dimensions: neural architecture, epsilon decay scheme, and alpha. The neural architecture is always two-layered, where the specifications are (256,256), (64,32), and (8,4). We therefore compare a big symmetric network to two smaller funnelled layers. Epsilon decay is always linearly decreasing and floored at 0.1, but two different rates are applied: 0.096 as suggested by Phil and our specification 1/5000 where the floor will only be hit after 4500 episodes, i.e. 90% of our training episodes. We therefore have 3\*2\*2=12 DQN specification for direct comparison and evaluation. Furthermore, we include the model with the best performance from Q Learning, SARSA, and random agent.

Given that we do not have access to a personal GPU, we did the calculations for our DQN on Google Colab. In the workspace folder shared below you will find 12 specifications of Jupyter notebooks, varying along three dimensions: epsilon decay, alpha and the dimensions of the neural network.

DQN summary table of parametrizations and main performance measures after 5000 training episodes

| Model | Training | Neural dims | Epsilon decay | Alpha | Win % | Avg max tile | Avg reward |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q, a=0.8, mono | 5000 | - | - | - | 0.126 | 109.64 | 1273.13 |
| SARSA, a= 0.5, nonmono | 5000 | - | - | - | 0.151 | 115.94 | 1332.19 |
| Best random performance\* | 5000 |   |   |   | 0.047 | 95.77 | 966.65 |
| DQN1 | 5000 | 256,256 | 0.096 | 0.001 | 0.078 | 103.14 | 1127.57 |
| DQN2 | 5000 | 256,256 | 1/5000 | 0.0001 | 0.563 | 204.25 | 2120.86 |
| DQN3 | 5000 | 256,256 | 0.096 | 0.0001 | 0.572 | 159.04 | 2218.79 |
| DQN4 | 5000 | 256,256 | 1/5000 | 0.001 | 0.064 | 96.47 | 1054.54 |
| DQN5 | 5000 | 64,32 | 1/5000 | 0.0001 | 0.326 | 156.41 | 1694.18 |
| DQN6 | 5000 | 64,32 | 0.096 | 0.0001 | error | 156.74 | 1703.26 |
| DQN7 | 5000 | 64,32 | 0.096 | 0.001 | 0.062 | 93.33 | 1039.31 |
| DQN8 | 5000 | 64,32 | 1/5000 | 0.001 | 0.096 | 102.66 | 1107.65 |
| DQN9 | 5000 | 8,4 | 0.096 | 0.0001 | 0.198 | 133.01 | 1479 |
| DQN10 | 5000 | 8,4 | 1/5000 | 0.0001 | 0.216 | 132.15 | 1499.11 |
| DQN11 | 5000 | 8,4 | 0.096 | 0.001 | 0.016 | 75.02 | 841.13 |
| DQN12 | 5000 | 8,4 | 1/5000 | 0.001 | 0.064 | 91.36 | 1041.59 |

\*Best performance measures across all random agent training sets

Given our finding above that alpha= 0.001 tends to do better, we incorporated a further reduced alpha equal to 0.0001 which even tended to do better. After 5000 training episodes, the further reduced alpha seems to be superior in terms of our performance measures. Maybe this decrease by a factor of 10 could slow down the learning too much and result in underfitting, as presented in class. Nevertheless, the strong performance of this parametrizations does not support this idea yet. Maybe this could become more evident after more training.

### DQN test series: comparison

The neural architecture seems quite important for the performance of the DQN: bigger networks with more nodes tend to perform better. The deviation to the rule is DQN8 that outperformed DQN4, ceteris paribus, with a sparser network. At the same time, bigger networks needed more time for the computations. The question, which one is most efficient remains open.

The further reduced alpha seems to be superior in terms of our performance measures, compared to the a=0.001 after pre-test runs. Maybe this decrease by a factor of 10 could slows down the learning too much and results in underfitting, as presented in class. Nevertheless, the strong performance of this parametrizations does not support this idea yet. Maybe this could become more evident after more training. Even with the sparsest architectures, agents performed quite well when alpha=0.0001 (see DQN9&amp;10). All the alpha specifications, even with the smallest neural network, outperformed all of the previous tabular agents. As a caveat, those very small alphas increased the runtime considerably, such that we ran into backend problems with google colab. Multiple restarts where needed.

Regarding the epsilon decay, the effect seems to depend on the specification of the neural architecture. Whereas faster decay outperforms in case of the densest architectures (see DQN 1-4), the reduced decay is slightly superior for most of the rest (DQN 7-12). In the case of DQN&#39;s 5 &amp; 6 there is hardly any difference.

Comparing the results to the best performing tabular agents&#39;, one can see the superiority of most DQN specifications to Q-Learning and SARSA. Only the worst few agents underperform compared to the best random agent result from previous chapters, with very sparse architecture (8,4) and relatively high alpha of 0.001.

### DQN test series: conclusion

For a game like 2048 with its very vast state space, neural approximation seems to fare much better in terms of performance compared to the tabular approaches. Nevertheless, quite some computational power is needed to implement a DQN. Performance differential to the random agent increased considerably, compared to the tabular models, and as such we conclude that the learning process is more pronounced. Having said that, with additional training and better performance, the tabular storage of information should also increase exponentially. This might eventually become a computational problem itself that might surpass the need of DQNs.

In conclusion, for 2048, we would suggest a rather large neural architecture, possibly denser than (256,256), with low alpha. The epsilon decay does not seem to have such a big influence, but above results rather suggests a faster epsilon decay when coupled with dense neural architecture. The problem with such a model will be the great need computational capacities needed.

### Overall conclusion

DQN seems vastly superior in our case with very extensive state spaces, where the game dynamics are not purely deterministic and the average reward results are very promising since they doubled in the best performing specifications compared to the random agent performance. Prolonged training should continue to increase the performance, such that these models should eventually reach the tile of 2048, provided enough training.

In the end, our performance is limited by our inability to store observations and learning progress. We tried to implement &quot;a save&quot; of the agents as to let them continue to learn rather than starting from the beginning. Coupled with the computational requirements of (deep) reinforcement learning our progress was quite slow. Most of the project time was actually needed for creating an executable code and as such, relatively little time was left in the end for &quot;meta-troubleshooting&quot;.
