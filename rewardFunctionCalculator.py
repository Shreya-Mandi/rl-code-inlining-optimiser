import time
import psutil
import os
from functools import wraps


def performance_monitor(func):
    @wraps(func)
    def wrapper(file_path):
        # Start time and resource usage monitoring
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_mem = process.memory_info().rss  # rss is the Resident Set Size

        # Run the function with file handling
        with open(file_path, 'r') as file:
            content = file.read()
        result = func(content)

        # Calculate elapsed time and memory usage
        end_time = time.time()
        end_mem = process.memory_info().rss
        time_taken = end_time - start_time
        memory_used = (end_mem - start_mem) / (1024 * 1024)  # Convert bytes to megabytes

        # # Print results
        # print(f"Execution time: {time_taken:.6f} seconds")
        # print(f"Memory used: {memory_used:.6f} MB")

        return result, time_taken, memory_used

    return wrapper


# Example usage
@performance_monitor
def process_file_content(content):
    # Example processing: count the number of lines
    line_count = len(content.split('\n'))
    return line_count

def rewardCalc(file_path):
    result = process_file_content(file_path)
    return -(result[1]+result[2])

def printMetric(file_path):
        result = process_file_content(file_path)
        print("Result (Line Count, Execution Time, Memory Used):", result)