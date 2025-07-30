from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])      
            result.append(nums[i + n])   
        return result

# Run the solution with example inputs
if __name__ == "__main__":
    s = Solution()

    #1 
    nums = [2,5,1,3,4,7]
    n = 3
    print(s.shuffle(nums, n))  # expected: [2,3,5,4,1,7]

    #2
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(s.shuffle(nums, n))  # expected: [1,4,2,3,3,2,4,1]

    #3
    nums = [1,1,2,2]
    n = 2
    print(s.shuffle(nums, n))  # expected: [1,2,1,2]