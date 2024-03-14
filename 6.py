weight = float(input())
height = float(input())
weight_kg = weight / 2.205
height_meter = 2.54 * height / 100
IMT = weight_kg / height_meter ** 2
print(round(IMT, 2))