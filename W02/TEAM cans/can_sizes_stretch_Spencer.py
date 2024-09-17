import math

def main():

    steel_cans = [
    ["#1 Picnic", 6.83, 10.16, 0.28],
    ["#1 Tall", 7.78, 11.91, 0.43],
    ["#2", 8.73, 11.59, 0.45],
    ["#2.5", 10.32, 11.91, 0.61],
    ["#3 Cylinder", 10.79, 17.78, 0.86],
    ["#5", 13.02, 14.29, 0.83],
    ["#6Z", 5.40, 8.89, 0.22],
    ["#8Z short", 6.83, 7.62, 0.26],
    ["#10", 15.72, 17.78, 1.53],
    ["#211", 6.83, 12.38, 0.34],
    ["#300", 7.62, 11.27, 0.38],
    ["#303", 8.10, 11.11, 0.42]
    ]
    
    max_storage = 0
    max_cost = 0
    best_storage = None
    best_cost = None

    for can in steel_cans:
        for i in can:
            name = can[0]
            radius = can[1]
            hight = can[2]
            cost = can[3]
            volume = compute_volume(r=radius, h=hight)
            surface_area = compute_surface_area(r=radius, h=hight)
            storage_efficiency = compute_storage_efficiency(v=volume, s=surface_area)
            cost_efficiency = compute_cost_efficiency(v=volume, c=cost)
            print(f"{name} {storage_efficiency:.2f} {cost_efficiency:.0f}")

            if storage_efficiency > max_storage:
                max_storage = storage_efficiency
                best_storage = name


            if cost_efficiency > max_cost:
                max_cost = cost_efficiency
                best_cost = name

            break
    
    print() # new line
    print(f"The can size with the best storage efficiency is: {best_storage}")
    print(f"The can size with the best cost efficiency is: {best_cost}")

def compute_volume(r, h):
    return math.pi * r**2 * h

def compute_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def compute_storage_efficiency(v, s):
    return v / s

def compute_cost_efficiency(v, c):
    return v / c

print() # new line

main()

print() # new line