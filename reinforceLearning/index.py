import numpy as np
import random
import gym

random.seed(1234)

# Çevreyi oluştur
streets = gym.make('Taxi-v3', render_mode="ansi")

# Taksi (2,3), yolcu Y'de (2), hedef R'de (0)
initial_state = streets.encode(2, 3, 2, 0)
streets.reset(seed=1234)  # Rastgeleliği önlemek için seed kullan
streets.unwrapped.s = initial_state  # Başlangıç durumunu zorla

q_table = np.zeros([streets.observation_space.n, streets.action_space.n])

learning_rate = 0.1
discount_factor = 0.6
exploration = 0.1
epochs = 10000

for taxi_run in range(epochs):
    state = streets.reset()  # Gym 0.25.2 için yalnızca int döner (tuple değil)
    done = False

    while not done:
        random_value = random.uniform(0, 1)
        if random_value < exploration:
            action = streets.action_space.sample()  # Rastgele hamle
        else:
            action = np.argmax(q_table[state])  # En iyi bilinen hamle

        next_state, reward, done, info = streets.step(action)  # Gym 0.25.2 için uygun
        
        prev_q = q_table[state, action]
        next_max_q = np.max(q_table[next_state])
        new_q = (1 - learning_rate) * prev_q + learning_rate * \
            (reward + discount_factor * next_max_q)
        q_table[state, action] = new_q

        state = next_state  # Yeni duruma geçiş
