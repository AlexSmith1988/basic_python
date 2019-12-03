from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 1))

for i, val in enumerate([5, 3, 7, 1]):
    print(f"val {i} is {val}")

testLine = ':'.join(map(lambda x: f"Test{x}", range(10)))
split = testLine.split(":")

file = open("test.txt", "w")
file.writelines(['\n'.join(split), '\n'])
file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
file.close()

file = open("test.txt", "r")
print(file.readlines())
