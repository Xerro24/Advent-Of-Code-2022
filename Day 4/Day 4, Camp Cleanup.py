

print('\n\n\n')


num_of_tasks = 0
with open('Elf Task Assignment.txt', 'r') as file:
    for line in file:
        temp = line.split(',')
        Task_range = []
        for i in temp:
            Task_range.append(i.split('-'))
        Task_range[1][1] = Task_range[1][1].split("\n")[0]
        for i,x in enumerate(Task_range):
            for j in range(2):
                Task_range[i][j] = int(x[j])
        

        if ((Task_range[0][0] >= Task_range[1][0] and Task_range[0][0] <= Task_range[1][1]) or (Task_range[1][0] >= Task_range[0][0] and Task_range[1][0] <= Task_range[0][1])) or ((Task_range[0][0] <= Task_range[1][0] and Task_range[0][1] >= Task_range[1][1]) or (Task_range[1][0] <= Task_range[0][0] and Task_range[1][1] >= Task_range[0][1])):
            num_of_tasks += 1
        #if (Task_range[0][0] <= Task_range[1][0] and Task_range[0][1] >= Task_range[1][1]) or (Task_range[1][0] <= Task_range[0][0] and Task_range[1][1] >= Task_range[0][1]):
        
        print(Task_range)
        print(num_of_tasks)
        



print('\n\n\n')