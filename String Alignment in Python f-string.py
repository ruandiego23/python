result = 'nline 1nline 2n'.rstrip('n')
print(result)
result = 'nline 1nline 2n'.lstrip('n')
print(result)

# here 20 spaces are reserved for the
# particular output string. And the string
# is printed on the left side
print(f"{'Left Aligned Text' : <20}")

# here 20 spaces are reserved for the
# particular output string. And the string
# is printed on the right side
print(f"{'Right Aligned Text' : >20}")

# here 20 spaces are reserved for the
# particular output string. And the string
# is printed in the middle
print(f"{'Centered' : ^10}")

# assigning strings to the variables
left_alignment = "Left Text"
center_alignment = "Centered Text"
right_alignment = "Right Text"

# printing out aligned text
print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}")
print()

# assigning list values to the variables
names = ['Raj', 'Shivam', 'Shreeya', 'Kartik']
marks = [7, 9, 8, 5]
div = ['A', 'A', 'C', 'B']
id = [21, 52, 27, 38]

# printing Aligned Header
print(f"{'Name' : <10}{'Marks' : ^10}{'Division' : ^10}{'ID' : >5}")

# printing values of variables in Aligned manner
for i in range(0, 4):
    print(f"{names[i] : <10}{marks[i] : ^10}{div[i] : ^10}{id[i] : >5}")