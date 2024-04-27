import graphToCode
from env import GraphEnv
import rl as rl
import callGraphGen as callGraphGen


def get_graph(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    return callGraphGen.genCallGraph(content)


def run_test(file_path):
    graph = get_graph(file_path)
    env = GraphEnv(graph, 0)

    rl.test(env, graph)

    code = graphToCode.extract_code(graph)
    with open(file_path[:-3] + "_output.py", 'w') as file:
        file.write(code)


if __name__ == '__main__':
    path = "input/demo1.py"
    run_test(path)
