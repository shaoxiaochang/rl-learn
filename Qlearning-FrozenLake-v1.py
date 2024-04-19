import gymnasium as gym
import numpy as np 

# Create the environment
env = gym.make("FrozenLake-v1")

# Q-learning parameters
alpha = 0.1  # learning rate
gamma = 0.9  # discount factor
epsilon = 0.1  # exploration rate

# Initialize Q table
num_states = env.observation_space.n
num_actions = env.action_space.n
Q = np.zeros((num_states, num_actions))

# Q-learning algorithm
num_episodes = 1000
for episode in range(num_episodes):
    state, info = env.reset()
    done = False
    
    while not done:
        # Choose action using epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Exploration
        else:
            action = np.argmax(Q[state])  # Exploitation
        
        # Take action and observe the next state and reward
        next_state, reward, done, truncated, info = env.step(action)
        
        # Update Q value
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        
        state = next_state

# Evaluate the learned policy
total_reward = 0
num_episodes_eval = 100
for _ in range(num_episodes_eval):
    state, info = env.reset()
    done = False
    
    while not done:
        action = np.argmax(Q[state])  # Greedy policy
        next_state, reward, done, truncated, info = env.step(action)
        total_reward += reward
        state = next_state

average_reward = total_reward / num_episodes_eval
print("Average reward over", num_episodes_eval, "episodes:", average_reward)
