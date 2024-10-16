3)write pgm to reverse on array without using another array
num_list = [3, 2, 8, 7, 5, 7, 8]
output = []

i = len(num_list) - 1  

while i >= 0:
    output.append(num_list[i])  
    i -= 1

print(output)
