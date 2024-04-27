def find_max(nums):
    max_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_min(nums):
    min_num = nums[0]
    for num in nums[1:]:
        if num < min_num:
            min_num = num
    return min_num

def find_range(nums):
    return find_max(nums) - find_min(nums)

def main():
    numbers = [5, 2, 8, 1, 9, 3]
    print("Maximum value:", find_max(numbers))
    print("Minimum value:", find_min(numbers))
    print("Range of values:", find_range(numbers))

if __name__ == "__main__":
    main()
