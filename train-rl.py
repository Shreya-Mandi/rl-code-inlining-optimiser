import rl as rl
import env as Env
import callGraphGen
import os

def process_files_in_directory(directory_path, process_function=callGraphGen.genCallGraph):
    results = []
    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Check if the path is a file
        if os.path.isfile(file_path):
            # Apply the process_function to the file
            result = process_function(file_path)
            results.append(result)
    return results
def run_train(trainingGraphs):
    for graph in trainingGraphs:
        env = Env.GraphEnv(graph, 0)
        rl.train(env, epochs=10000)

def train_rl(directory_path):
    processed_results = process_files_in_directory(directory_path)
    run_train(processed_results)

if __name__=='__main__':
    directory_path="placeholder" #TODO
    train_rl(directory_path)