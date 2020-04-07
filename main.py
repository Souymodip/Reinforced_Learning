import random
import seaborn as sns
import matplotlib.pyplot as plt
import MDP
import Monte_Carlo
import Random_Walk
import Temporal_difference
#import numpy as np
#import pandas as pd
import util

random.seed(1)


def armed_bandit_reward(m, sd):
    return int(random.gauss(m, sd))


def k_armed_bandit(k):
    m = [(random.uniform(-2, 2), random.uniform(0, 10)) for i in range(k)]
    return m


def print_estimator(Q):
    s = "["
    for q in Q:
        s = s + "(" + str(q[0]) + ", " + str(q[1]) + ") "
    s = s + "]"
    print(" |_ " + s)


def play(model, Q, policy, k):
    reward = 0
    for i in range(k):
        choice = policy(model, Q)
        win = armed_bandit_reward(model[choice][0], model[choice][1])
        reward = reward + win
        Q[choice] = (Q[choice][0] + (win - Q[choice][0])/(Q[choice][1] + 1), Q[choice][1] + 1)
        #print(str(i + 1) + ". choice := " + str(choice) + ", Win := " + str(win) + ", Total win:= " + str(reward))
        #print(print_estimator(Q))
    #print("Reward := " + str(reward))
    return reward


def test_policy(model, Q):
    def random_policy(model, Q):
        return int(random.uniform(0, len(model) - 1))

    def greedy_policy(model, Q):
        return util.arg_max_random(Q)

    def e_greedy_policy(model, Q):
        e = 0.1
        if random.uniform(0,100)/100 <= e:
            return int(random.uniform(0, len(Q)))
        else:
            return util.arg_max_random(Q)
    return play(model, Q, e_greedy_policy, 1000)


def plot(ss):
    sns.set()
    plt.plot(ss)
    plt.ylabel('Reward')
    plt.show()


def test():
    print("Creating Model ...")
    model = k_armed_bandit(10)
    Q = [(2, 0)] * len(model)
    print("Starting test ...")
    ss = [test_policy(model, Q) for i in range(2000)]
    print("Plotting ...")
    plot(ss)


def evaluate_policy():
    print("Creating MDP.")
    mdp = MDP.MDP(10, 3)
    print("Running Monte Carlo State-Value Estimation.")
    TS = []

    for i in range(5, 8):
        print (str(i) + "...")
        v0 = Monte_Carlo.first_visit_eval(mdp, 0, 0.01, 10, i*10, lambda x: 1)[0]
        print (" " + str(v0))
        TS.append(v0[0])
    plot(TS)


def get_optimal_policy():
    print("Creating MDP.")
    mdp = MDP.MDP(10, 4)
    print("Running Monte Carlo State-Value Optimal Estimation.")
    p = Monte_Carlo.optimal_control_es(mdp, 0, 0.1, 10, 40)
    print(p)


def simulate_random_walk():
    rw = Random_Walk.OneDRandomWalk(3)
    random.seed(1)
    for j in range(20):
        rw.reset()
        s = str(j) +": 0"
        r = 0
        for i in range(10):
            next = rw.next_state_reward()
            r = r + next[1]
            s = s + " -> " + str(next[0])
        print (s + " := " +str(r))


def evaluate_TD():
    print("Creating MDP.")
    mdp = MDP.MDP(10, 3)
    print("Running TD State-Value Estimation.")
    ts =[]
    for i in range(1, 20):
        print(str(i) + "...")
        v = Temporal_difference.estimate(mdp, 0, 0.01, 30, 100, lambda x: 1)
        print("\t"+ str(v[0]))
        ts.append(v[0])
    plot(ts)


evaluate_TD()
#evaluate_policy()
#get_optimal_policy()
