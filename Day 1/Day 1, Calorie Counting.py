print('\n\n\n')


largest_count = 0
largest_count_2 = 0
largest_count_3 = 0
index = 0
temp = 1
temp_index = 1
with open('Elf Calorie Count.txt', 'r') as file:
    for line in file:
        if line == '\n':
            if temp >= largest_count:
                largest_count_3 = largest_count_2
                largest_count_2 = largest_count
                largest_count = temp
                index = temp_index
            elif temp >= largest_count_2:
                largest_count_3 = largest_count_2
                largest_count_2 = temp
                index = temp_index
            elif temp >= largest_count_3:
                largest_count_3 = temp
                index = temp_index
            temp_index += 1
            temp = 0
            #print(line)
        elif line.strip() == False:
            print('end')
        else:
            temp += int(line)
        print(largest_count, index, temp, temp_index)
            #print("bingus")
    #print(file.read())

print(largest_count,largest_count_2,largest_count_3)
print(largest_count + largest_count_2 + largest_count_3)


print('\n\n\n')