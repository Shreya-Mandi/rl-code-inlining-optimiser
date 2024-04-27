import numpy as np
import pathRewardCalc as pathReward

def reward_function(done, path):
    if done:
        return pathReward.calculate_reward(path)
    else:
        return 0

def train(env, epochs, learning_rate=0.1, discount_factor=0.95):
    # Initialize Q-table with zero
    Q = np.zeros((env.observation_space.n, env.action_space.n))

    for epoch in range(epochs):
        state = env.reset()
        done = False

        while not done:
            # Choose action from Q table (greedy)
            if np.random.rand() < 0.1:  # Exploration with epsilon=0.1
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state])

            # Take the action and observe the new state and reward
            next_state, reward, done, _ = env.step(action)

            # Update Q-table using the Bellman equation
            best_next_action = np.argmax(Q[next_state])
            td_target = reward + discount_factor * Q[next_state][best_next_action]
            td_error = td_target - Q[state][action]
            Q[state][action] += learning_rate * td_error

            # Update state
            state = next_state

        # Optionally, print the Q-table every epoch
        # print(f"Epoch {epoch}: Q-table \n{Q}")

    store_q_table(Q)

def store_q_table(Q):
    with open('q_table.txt','w') as file:
        file.write(Q)
# def test(Q,env, start_node='main'):
#     state=start_node
#     done=False
#     with open('output.txt', 'w') as file:
#         while not done:
#           action = np.argmax(Q[state])
#           next_state, reward, done, _ = env.step(action)
#           file.write(state+" "+action)
#           state = next_state


