class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        m = {}
        for i in range(len(numbers)):
            if numbers[i] in m.keys():
                return [m[numbers[i]], i+1]
            else:
                m[target - numbers[i]] = i+1
        return 0