class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_el = max(piles)

        def bs(low_el, high_el, piles, h):
            if high_el == low_el:
                return high_el
            if high_el - low_el == 1:
                return low_el if self.checkPossible(piles, low_el, h) else high_el

            half = math.ceil((high_el - low_el)/ 2)
            rate = low_el + half
            if self.checkPossible(piles, rate, h):
                return bs(low_el, rate, piles, h)
            else:
                return bs(rate, high_el, piles, h)

        return bs(1, max_el, piles, h)
    
    def checkPossible(self, piles, rate, h):
        total_hours = 0
        for i in piles:
            total_hours += math.ceil(i/rate)
        return total_hours <= h