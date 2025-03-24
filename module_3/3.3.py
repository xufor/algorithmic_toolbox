distance = int(input())
distance_per_refill = int(input())
pumps_count = int(input())
pumps = list(map(int, input().split()))
pumps = {value: True for value in pumps}
last_pump_location = -1
current_tank_level = distance_per_refill
current_distance = 0
total_refills = 0

while True:
    # print(current_distance, current_tank_level, total_refills, last_pump_location)
    current_distance += 1
    current_tank_level -= 1
    if pumps.get(current_distance) != None:
        last_pump_location = current_distance
    if current_distance >= distance:
        print(total_refills)
        break
    if current_tank_level == 0:
        # print(current_distance, current_tank_level, total_refills, last_pump_location)
        if last_pump_location == -1:
            print(-1)
            break
        dist_from_last_pump = current_distance - last_pump_location
        current_tank_level = distance_per_refill - dist_from_last_pump
        total_refills += 1
        last_pump_location = -1
        # print(current_distance, current_tank_level, total_refills, last_pump_location)