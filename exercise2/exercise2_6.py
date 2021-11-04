import math

cherry = (2 + 2 * 2 + 2 - 2 - 2) / 2
apple = (math.sqrt(3 + 10 - 4) / 3) + ((5 ** 3) - 5) / 20 + 3
orange = apple - 9
banana = (cherry + 10) / 3
pear = (banana * 3) - 8
answer = apple - (banana * 2) + orange * (pear + cherry)

print(int(answer))
