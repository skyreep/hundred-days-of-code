class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set initial left and right search bounds
        left_bound = 0
        right_bound = (len(nums) - 1)
        # search until only one element remains 
        while left_bound <= right_bound:
            # find middle element
            pivot_point = int(((left_bound + right_bound) / 2))
            guess = nums[pivot_point]
            # if the pivot is the target return the pivot point
            if guess == target:
                return pivot_point
            # if pivot point is too high, set new high search bound
            if guess > target:
                right_bound = pivot_point - 1
            # else the pivot point is too low; set new low search bound
            else:
                left_bound = pivot_point + 1
        # triggered if the list is searched and the target element is not found by the while loop
        return -1