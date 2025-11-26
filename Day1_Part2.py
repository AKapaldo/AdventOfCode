def twoSum(num_arr, pair_sum):
    for i in range(len(num_arr) - 1):
        for j in range(i + 1, len(num_arr)):
            for k in range(j + 1, len(num_arr)):
                if num_arr[i] + num_arr[j] + num_arr[k] == pair_sum:
                    print("Pair with sum", pair_sum, "is: ", num_arr[i], num_arr[j], num_arr[k])


num_arr = []
pair_sum = 2020


twoSum(num_arr, pair_sum)
