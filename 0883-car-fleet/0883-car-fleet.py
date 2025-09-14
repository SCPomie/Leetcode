class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com_list = []
        for i in range(min(len(position), len(speed))):
            com_list.append((position[i], speed[i]))
        com_list.sort(reverse=True)
        car_fleet = []
        for pair in com_list:
            result = self.timer(target, pair)
            if not car_fleet:
                car_fleet.append(result)
            if (result > car_fleet[-1]):
                car_fleet.append(result)
        return len(car_fleet)
        

    def timer(self, target, pair):
        pos, spd = pair
        return (target - pos) / spd