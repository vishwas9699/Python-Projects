blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 0
while layer < blocks:
    layer += 1
    blocks -= layer
    height += 1

print("The height of the pyramid:",height)    