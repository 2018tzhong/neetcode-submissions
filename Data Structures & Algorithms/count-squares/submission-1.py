from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.y_coords = defaultdict(list)
        self.x_coords = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.y_coords[point[1]].append(point[0])
        self.x_coords[point[0]].append(point[1])

    def count(self, point: List[int]) -> int:
        # query our points structure to see if we can find 3 points that create a square

        # need one point sharing x coordinate, with temp y
        # need one point sharing y coordinate (equal length). with temp x
        # need one point with the other coordinates temp x and temp y
        total_results = 0
        print("y", self.y_coords)
        print("x", self.x_coords)
        for i in self.y_coords[point[1]]:
            side = abs(point[0] - i)
            if side == 0:
                continue
            # print(i, side, point, point[0]-side)
            if point[1] - side in self.x_coords[point[0]]:
                # print("checking", point[1]-side, self.y_coords)
                if i in self.y_coords[point[1]-side]:
                    # print("adding", (self.x_coords[point[0]].count(point[1]-side)), (self.y_coords[point[1]-side].count(i)))
                    total_results += (self.x_coords[point[0]].count(point[1]-side)) * (self.y_coords[point[1]-side].count(i))
            if point[1] + side in self.x_coords[point[0]]:
                # print("checking", point[1]+side, self.y_coords)
                if i in self.y_coords[point[1]+side]:
                    # print("adding", (self.x_coords[point[0]].count(point[1]+side)), (self.y_coords[point[1]+side].count(i)))
                    total_results += (self.x_coords[point[0]].count(point[1]+side)) * (self.y_coords[point[1]+side].count(i))


        return total_results
