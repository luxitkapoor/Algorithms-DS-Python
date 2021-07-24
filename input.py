data = []
with open('input.txt') as f:
    input = f.read()
    input = input.split('\n')

input.pop(-1)
data = [int(i) for i in input]
# print(data)
