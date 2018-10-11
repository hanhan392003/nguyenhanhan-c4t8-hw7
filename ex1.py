# ex 1
colors = ["blue", "red", "green"]
print(colors)

# ex 2
print("Our color list:")
print(*colors, sep = ", ")

# ex 3
new_color = input("Enter a new color: ")
colors.append(new_color)
print("Our color list:")
print(*colors, sep = ", ")

# ex 4
pos = int(input("Enter the position: "))
print("Color at position", pos, ":", colors[pos - 1])

# ex 5
del_item = input("Enter the color or the position you want to delete: ")
if del_item.isalpha():
    if del_item in colors:
        colors.remove(del_item)
        for i, color in enumerate(colors):
            print(i + 1, ".", color)
else: 
    print("This color is not in the list")

if del_item.isdigit():
    try:
        del_item = int(del_item)
        colors.pop(del_item-1)
        for i, color in enumerate(colors):
            print(i + 1, ".", color)
    except IndexError:
        print("The list has only", len(colors),"item(s)")