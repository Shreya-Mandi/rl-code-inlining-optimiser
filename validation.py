import rewardFunctionCalculator as rewardFunc

# input file
file_path_ip = 'input/demo1.py'
print('Input performance:')
rewardFunc.printMetric(file_path_ip)

# output file
file_path_op = 'rl-output/op1.py'
print('Output performance:')
rewardFunc.printMetric(file_path_op)
