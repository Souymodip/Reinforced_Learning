import random
import discrete


class MDP:
    def __init__(self, S, A):
        self.S = S
        self.A = A
        random.seed(1)
        self.dynamics = [[(random.uniform(0, self.S-1), random.uniform(1, 10)) for a in range(self.A)] for s in range(self.S)]
        self.reward = [[(random.uniform(0, self.S-1), random.uniform(1, 10)) for a in range(self.A)] for s in range(self.S)]

    def next_state(self, s, a):
        m, d = self.dynamics[s][a]
        return discrete.get_normal_choice(self.S, m, d)

    def next_reward(self, s, a):
        m, d = self.reward[s][a]
        return discrete.get_normal_choice(self.S, m, d)
