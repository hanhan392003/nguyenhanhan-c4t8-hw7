import math
# ex 12
name = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
population = [150300, 247100, 333300, 266800, 420900, 318000]

# ex 13
population_min = min(population)
minimum = population.index(population_min)
print(minimum+1)
population_max = max(population)
maximum = population.index(population_max)
print(maximum+1)

# ex 14
print(name[minimum])
print(name[maximum])

# ex 15
area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
MDDC = []
for i in area:
    for j in population:
        if area.index(i) == population.index(j):
            per_area = j/i
            per_area = round(per_area, 2)
            MDDC.append(per_area)
print(MDDC)

# ex 16
MDDC_sum = 0
for mddc_of_district in MDDC:
    MDDC_sum += mddc_of_district
numbers_of_districts = len(name)
average_mddc = MDDC_sum/numbers_of_districts
average_mddc = round(average_mddc, 2)
print(average_mddc)