class Solution:
    def checkValidString(self, s: str) -> bool:
        star_count = 0
        left_count = 0
        right_count = 0
        for i in s:
            if i == "(":
                left_count += 1
            elif i == ")":
                right_count += 1
            elif i == "*":
                star_count += 1
            else:
                # throw error
                continue

            if right_count-left_count > star_count:
                return False

        if not abs(right_count - left_count) <= star_count:
            return False

        star_count = 0
        left_count = 0
        right_count = 0
        for i in s[::-1]:
            if i == "(":
                left_count += 1
            elif i == ")":
                right_count += 1
            elif i == "*":
                star_count += 1
            else:
                # throw error
                continue

            if left_count-right_count > star_count:
                return False

        # print(right_count, left_count, star_count)
        return abs(right_count - left_count) <= star_count