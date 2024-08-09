import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Number of iterations for the simulation
iterations = 1000

# Transition probabilities
transition_matrix = np.array([
    [0.5, 0.3, 0.2],  # S1 to S1, S2, S3
    [0.4, 0.5, 0.1],  # S2 to S1, S2, S3
    [0.3, 0.4, 0.3]   # S3 to S1, S2, S3
])

# Initialize state counts
state_counts = np.zeros(3)

# Start in state S1
current_state = 0

# Run the simulation
state_history = []
for _ in range(iterations):
    state_history.append(current_state)
    state_counts[current_state] += 1
    current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])

# Normalize state counts to probabilities
state_probabilities = state_counts / iterations

# Visualize the results
states = ['S1', 'S2', 'S3']
colors = ['r', 'g', 'b']
fig, ax = plt.subplots()

bars = ax.bar(states, state_probabilities, color=colors)
ax.set_xlabel('States')
ax.set_ylabel('Probability')
ax.set_title('Markov Chain State Probabilities')

# Add the probabilities as text on the bars
for bar, prob in zip(bars, state_probabilities):
    height = bar.get_height()
    ax.annotate(f'{prob:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# Draw transition graph
G = nx.DiGraph()
for i, state in enumerate(states):
    for j, prob in enumerate(transition_matrix[i]):
        if prob > 0:
            G.add_edge(state, states[j], weight=prob)

pos = nx.spring_layout(G)
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

plt.figure()
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=16, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]:.1f}' for u, v, d in edges})
plt.title('Markov Chain Transition Graph')
plt.show()
