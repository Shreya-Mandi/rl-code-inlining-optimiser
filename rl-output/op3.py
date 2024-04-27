def find_max_min(nums):
    max_num = min_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num

def find_range(nums):
    max_num, min_num = find_max_min(nums)
    return max_num - min_num

def main():
    numbers = [5, 2, 8, 1, 9, 3]
    max_num, min_num = find_max_min(numbers)
    print("Maximum value:", max_num)
    print("Minimum value:", min_num)
    print("Range of values:", find_range(numbers))

if __name__ == "__main__":
    main()
