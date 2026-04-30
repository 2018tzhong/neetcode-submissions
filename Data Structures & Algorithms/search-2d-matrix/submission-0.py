class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def vert_bs(nums, target):
            
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return -1 if target < nums[0] else 0
            
            pivot = math.ceil(len(nums)/2) - 1

            if nums[pivot] > target:
                return vert_bs(nums[:pivot], target)
            elif nums[pivot] <= target:
                return pivot + 1 + vert_bs(nums[pivot+1:], target)
            else:
                return -math.inf


        def horz_bs(nums, target):
            if len(nums) == 0:
                return False
            if len(nums) == 1:
                return nums[0] == target
            
            pivot = math.ceil(len(nums)/2) - 1

            if nums[pivot] > target:
                return horz_bs(nums[:pivot], target)
            elif nums[pivot] < target:
                return horz_bs(nums[pivot+1:], target)
            else:
                return True

        first_col = [i[0] for i in matrix]

        vert_idx = vert_bs(first_col, target)
        print("vert", vert_idx)

        horz_check = horz_bs(matrix[vert_idx], target)
        print("horz", horz_check)
        return horz_check