class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def bs(nums_shortened, target):
            
            if len(nums_shortened) == 0:
                return -1
            if len(nums_shortened) == 1:
                return 0 if nums_shortened[0] == target else -1

            pivot = math.ceil(len(nums_shortened)/2) - 1
            print(nums_shortened, pivot)
            if target > nums_shortened[pivot]:
                recurse = bs(nums_shortened[pivot+1:], target)
                if recurse == -1:
                    return recurse
                else:
                    return pivot + 1 + recurse 
            elif target < nums_shortened[pivot]:
                return bs(nums_shortened[:pivot], target)
            else:
                return pivot
        
        return bs(nums, target)