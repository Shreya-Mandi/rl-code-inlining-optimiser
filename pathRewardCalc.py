def calculate_reward(call_graph):
    # Criteria 1: Efficiency of computation
    # We can define efficiency based on the depth of the call graph
    depth = compute_depth(call_graph)

    # Criteria 2: Redundancy of computation
    # We can penalize for functions calling other functions unnecessarily
    redundancy_penalty = compute_redundancy_penalty(call_graph)

    # Criteria 3: Utilization of functions
    # We can reward for functions being utilized effectively
    utilization_reward = compute_utilization_reward(call_graph)

    # Combine the criteria to compute the overall reward
    reward = depth - redundancy_penalty + utilization_reward

    return reward

def compute_depth(call_graph):
    # Depth of the call graph is the maximum depth of function calls
    def dfs(node, depth, max_depth):
        if not call_graph[node]:
            max_depth[0] = max(max_depth[0], depth)
        else:
            for child in call_graph[node]:
                dfs(child, depth + 1, max_depth)

    max_depth = [0]
    for node in call_graph:
        dfs(node, 1, max_depth)

    return max_depth[0]

def compute_redundancy_penalty(call_graph):
    # Redundancy penalty is the number of unnecessary function calls
    penalty = 0
    for node in call_graph:
        penalty += len(call_graph[node])
    return penalty

def compute_utilization_reward(call_graph):
    # Utilization reward is the number of functions being utilized
    reward = len(call_graph)
    return reward

# def main():
#     # Example call graph
#     call_graph = {
#         'calculate_fibonacci': set(),
#         'generate_fibonacci_sequence': {'range', 'calculate_fibonacci'},
#         'main': {'print', 'generate_fibonacci_sequence'}
#     }
#
#     reward = calculate_reward(call_graph)
#     print("Reward for the call graph:", reward)
#
# if __name__ == "__main__":
#     main()
