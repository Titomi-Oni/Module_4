# 1) Create a class named `pair_elements`.
class pair_elemets:
# 2) Inside the class, define a method `twoSum(self, nums, target)`:
#    (This method finds two numbers in `nums` whose sum equals `target`
#     and returns their index positions.)
     def twoSum(self, nums, target):
# 3) Create an empty dictionary `lookup = {}`.
#    (This will store numbers as keys and their indexes as values for quick searching.)
        lookup = {}
# 4) Use a loop with `enumerate(nums)` to iterate through `nums`:
#    a) `i` gives the index of the current element.
#    b) `num` gives the value at that index.
        for i, num in enumerate(nums):     
# 5) For each number, check if the required pair exists:
#    a) Compute `target - num`.
#    b) If `target - num` is already present in `lookup`,
#       return a tuple containing:
#       - the index of the matching number from `lookup`
#       - the current index `i`
            if target - num in lookup:
             return (lookup[target - num], i)
# 6) If the pair is not found yet, store the current number and its index:
#    a) `lookup[num] = i`
            lookup[num] = 1
# 7) Take an integer input from the user and store it in `value`.
#    (This is the target sum to search for.)
value = int(input("Enter sum for which you want to make this search: " ))
# 8) Call the method `twoSum()` using:
#    a) the tuple `(10, 20, 30, 40, 50, 60, 70)` as `nums`
#    b) `value` as the `target`
print("index1=%d, index2=%d" %
    pair_elemets().twoSum((10, 20, 30, 40, 50, 60, 70),value))
# 9) Print the two indexes returned by `twoSum()` in the format:
#    "index1=..., index2=..."