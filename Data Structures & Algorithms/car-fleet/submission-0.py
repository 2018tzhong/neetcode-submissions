class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        s = []

        cars = []
        for i, car in enumerate(position):
            cars.append((speed[i], position[i]))
        sorted_cars = sorted(cars, key=lambda x: x[1], reverse=True)

        for i in sorted_cars:
            if s and s[-1][0] < i[0]:
                # check if it will catch up
                turns = (target - s[-1][1]) / s[-1][0]
                if turns * i[0] + i[1] <  s[-1][1] + turns * s[-1][0]:
                    #it'll not pass
                    s.append(i)
            else:
                s.append(i)

        return len(s)