print('\n\n\n')


priority_sum = 0
grouping = 0
Compartments = [0,0,0]
with open('Rucksack.txt', 'r') as file:
    for line in file:
        Compartments[grouping] = line
        grouping += 1
        if (grouping == 3):
            grouping = 0
            for i,x in enumerate(Compartments):
                Compartments[i] = set(x)
                Compartments[i].discard('\n')
            Common_item =  Compartments[0] & Compartments[1] & Compartments[2]
            for i in Common_item:
                Common_item = i
            print(Common_item)
            if (ord(Common_item)-96 < 0):
                priority_sum += ord(Common_item)-38
            else:
                priority_sum += ord(Common_item)-96
            print(priority_sum)

        '''
        Compartment_1 = line[0:len(line)//2]
        Compartment_2 = line[len(line)//2:len(line)]
        Compartment_1 = set(Compartment_1)
        Compartment_2 = set(Compartment_2)
        Common_item =  Compartment_1 & Compartment_2
        #print(Common_item)
        for i in Common_item:
            Common_item = i
        print(Common_item)
        if (ord(Common_item)-96 < 0):
            priority_sum += ord(Common_item)-38
        else:
            priority_sum += ord(Common_item)-96

        print(priority_sum)

        #print(Compartment_1 + "    " + Compartment_2)
        '''



print('\n\n\n')