import random


def mod(q):
    return -1*q if q < 0 else q


class OneDRandomWalk:
    def __init__(self, states):
        self.states = states
        self.curr_state = 0

    def reset(self):
        self.curr_state = 0

    def next_state_reward(self):
        if mod(self.curr_state) == self.states:
            return self.curr_state, 0
        direction = 'L' if random.uniform(0,1) <= 0.5 else 'R'
        reward = 0
        if direction == 'R':
            self.curr_state = self.curr_state + 1
            if self.curr_state == self.states:
                reward = 1
        else:
            self.curr_state = self.curr_state - 1
        return self.curr_state, reward
