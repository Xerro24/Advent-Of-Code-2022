from collections import deque

Stacks = []
for i in range(9):
    Stacks.append(deque())
Stacks[0].extend(('[R]','[N]','[P]','[G]'))
Stacks[1].extend(('[T]','[J]','[B]','[L]','[C]','[S]','[V]','[H]'))
Stacks[2].extend(('[T]','[D]','[B]','[M]','[N]','[L]'))
Stacks[3].extend(('[R]','[V]','[P]','[S]','[B]'))
Stacks[4].extend(('[G]','[C]','[Q]','[S]','[W]','[M]','[V]','[H]'))
Stacks[5].extend(('[W]','[Q]','[S]','[C]','[D]','[B]','[J]'))
Stacks[6].extend(('[F]','[Q]','[L]'))
Stacks[7].extend(('[W]','[M]','[H]','[T]','[D]','[L]','[F]','[V]'))
Stacks[8].extend(('[L]','[P]','[B]','[V]','[M]','[J]','[F]'))


line_num = 0
temp = deque()
s = ''
with open('Crane instructions.txt', 'r') as file:
    for line in file:
        if line_num >= 10:
            for i in Stacks:
                print(i)
            print('\n')
            amount = int(line.split(' ')[1])
            from_col = int(line.split(' ')[3]) -1
            to_col = int(line.split(' ')[5]) -1
            print(amount,from_col,to_col)
            for i in range(amount):
                temp.append(Stacks[from_col].pop())
            for i in range(len(temp)):
                Stacks[to_col].append(temp.pop())
            for i in Stacks:
                print(i)
            print('\n\n\n')
        line_num += 1
    for i in Stacks:
        s += i[-1][1:2]
        print(s)
