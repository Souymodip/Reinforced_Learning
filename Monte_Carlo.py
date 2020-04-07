import random
import MDP
import policy

def get_episode(mdp, start, episode_length, policy):
    trace = []
    rewards = []
    actions = []
    current_state = start
    for j in range(episode_length):
        trace.append(current_state)
        next_action = policy(current_state)
        actions.append(next_action)
        current_reward = mdp.next_reward(current_state, next_action)
        rewards.append(current_reward)
        current_state = mdp.next_state(current_state, policy(current_state))
    return trace, rewards, actions


def first_visit_eval(mdp, start, gamma, episode_length, episode_num, policy):
    V = dict()
    for i in range(episode_num):
        episode, rewards, actions = get_episode(mdp, start, episode_length, policy)
        G = 0
        for i in reversed(range(episode_length)):
            G = gamma * G + rewards[i]
            if i == 0 or (episode[i] not in set(episode[:i])):
                if episode[i] not in V:
                    V[episode[i]] = (G, 1)
                else:
                    V[episode[i]] = ((V[episode[i]][1]*V[episode[i]][0] + G) / (V[episode[i]][1] + 1), V[episode[i]][1] + 1)
    return V


def optimal_control_es(mdp, start, gamma, episode_length, iterations):
    p = policy.Policy()
    for i in range(iterations):
        # Need to completly Randomize the Initial State action of the trajectory
        exploring_act0 = int(random.uniform(0, mdp.A-1))
        next_state0 = mdp.next_state(start, exploring_act0)
        exploring_act1 = int(random.uniform(0, mdp.A-1))
        next_state1 = mdp.next_state(start, exploring_act1)

        episode, rewards, actions = get_episode(mdp, next_state1, episode_length, p)
        episode = [start, next_state0 ] + episode
        rewards = [mdp.next_reward(start, exploring_act0), mdp.next_reward(next_state0, exploring_act1)] + rewards
        actions = [exploring_act0, exploring_act1] + actions

        Q = dict()
        G = 0
        #print(str(episode) + " " + str(actions))
        print (str(i) + "...")
        def contains(l, a):
            for i in l:
                if a == i:
                    return True
            return False

        state_actions = list(zip(episode, actions))
        for i in reversed(range(1, len(state_actions))):
            G = gamma * G + rewards[i]
            if not contains(state_actions[:i-1], (episode[i], actions[i])):
                Q[(episode[i], actions[i])] = (Q[(episode[i], actions[i])][0] + G, Q[(episode[i], actions[i])][1] + 1) if (episode[i], actions[i]) in Q else (G, 1)
                rewards_action = []
                for a in range(mdp.A):
                    if (episode[i], a) in Q:
                        rewards_action.append(Q[(episode[i], a)][0]/Q[(episode[i], a)][1])
                    else:
                        rewards_action.append(0)
                p.update(episode[i], rewards_action.index(max(rewards_action)))
    return p

