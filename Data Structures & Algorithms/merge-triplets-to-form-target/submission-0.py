class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        eligible_trips_idxs = set()
        ta, tb, tc = target
        fa, fb, fc = False, False, False
        for idx, triplet in enumerate(triplets):
            ai, bi, ci = triplet
            check = self.checkEligible(ta, tb, tc, ai, bi, ci)
            if check:
                if ai == ta:
                    fa = True
                if bi == tb:
                    fb = True
                if ci == tc:
                    fc = True
            eligible_trips_idxs.add(idx)
        
        if not (fa and fb and fc):
            return False

        return True

    def checkEligible(self, ta, tb, tc, ca, cb, cc):
        if ca > ta or cb > tb or cc > tc:
            return False
        
        return ca == ta or cb == tb or cc == tc