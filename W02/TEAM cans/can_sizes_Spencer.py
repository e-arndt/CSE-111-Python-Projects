import math

def main():

    can = "#1 Picnic"
    radius = 6.83
    hight = 10.16
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#1 Tall"
    radius = 7.78
    hight = 11.91
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#2"
    radius = 8.73
    hight = 11.59
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#2.5"
    radius = 10.32
    hight = 11.91
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#3 Cylinder"
    radius = 10.79
    hight = 17.78
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#5"
    radius = 13.02
    hight = 14.29
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#6Z"
    radius = 5.40
    hight = 8.89
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#8Z short"
    radius = 6.83
    hight = 7.62
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#10"
    radius = 15.72
    hight = 17.78
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#211"
    radius = 6.83
    hight = 12.38
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#300"
    radius = 7.62
    hight = 11.27
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

    can = "#303"
    radius = 8.10
    hight = 11.11
    volume = compute_volume(r=radius, h=hight)
    surface_area = compute_surface_area(r=radius, h=hight)
    print(f"{can} {compute_storage_efficiency(v=volume, s=surface_area):.2f}")

def compute_volume(r, h):
    return math.pi * r**2 * h

def compute_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def compute_storage_efficiency(v, s):
    return v / s

print() # new line

main()

print() # new line