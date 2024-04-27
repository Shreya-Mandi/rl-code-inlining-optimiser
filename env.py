import gym
from gym import spaces
import numpy as np
import pathRewardCalc as pathReward
class GraphEnv(gym.Env):

    def __init__(self, graph, start_node):
        super(GraphEnv, self).__init__()
        self.graph = graph
        self.path=graph
        self.current_node = start_node
        self.action_space = spaces.Discrete(len(self.graph[start_node]+1))
        self.observation_space = spaces.Discrete(len(graph))

    def step(self, action):
        # if action is a number greater than the possible calls from a graph-> no action/ no inlining
        if action!=self.graph[self.current_node]+1:
            self.current_node = self.graph[self.current_node][action]
            # inline by removing the edge in call graph
            self.path.remove(self.path[self.current_node][action])

        # done when the current node is not connected in the call graph
        done = self.graph[self.current_node] not in self.graph.keys()

        # redefine the action space at every step
        self.action_space=spaces.Discrete(len(self.graph[self.current_node]+1))

        # reward is calculated on the graph that has been inlined
        reward=0
        if done:
            reward=pathReward.calculate_reward(self.path)
        return self.current_node, reward, done, {}

    def reset(self):
        self.current_node = 0
        self.path=self.graph
        return self.current_node

