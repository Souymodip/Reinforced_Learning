import MDP


def estimate(mdp, start, gamma, episode_length, episode_num, policy):
    v = dict()
    curr_state = start
    alpha = 0.5
    for i in range(episode_num):
        #s = str(i)+": " + str(curr_state)
        for j in range(episode_length):
            act = policy(curr_state)
            reward = mdp.next_reward(curr_state, act)
            next_state = mdp.next_state(curr_state, act)
            v_next_state = v[next_state] if next_state in v else 0
            if curr_state in v:
                v[curr_state] = v[curr_state] + alpha*(reward - v[curr_state] + gamma*v_next_state)
            else:
                v[curr_state] = alpha * (reward + gamma*v_next_state)
            curr_state = next_state
            #s = s + " -> " + str(curr_state)
        #print(s + " := " + str(v[0]))
    return v
