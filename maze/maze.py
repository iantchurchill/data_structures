class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


file = open('maze.txt','r')
x = file.read()
y = x.split('\n')

def str_list(instr):
    return list(instr)

def list_str(inlist):
    return ''.join(inlist)

def start_maze(y):
    stack = Stack()
    current_lst,lst_position = 1,0
    surrounding_pos = ((-1,0),(0,1),(1,0),(0,-1))
    found = False

    while not found:
        for i in range(0,4):
            firstrange = current_lst + surrounding_pos[i][0] 
            second = lst_position + surrounding_pos[i][1] 
            if current_lst + surrounding_pos[i][0] in range(len(y)) and lst_position + surrounding_pos[i][1]  in range(len(y[current_lst])):
                next_pos = [current_lst + surrounding_pos[i][0] , lst_position + surrounding_pos[i][1]]
                test = y[next_pos[0]][next_pos[1]]
                if y[next_pos[0]][next_pos[1]] == '0':
                    stack.push(next_pos)
                elif y[next_pos[0]][next_pos[1]] == 'X':
                    stack.push(next_pos)
                    found = True
                    print("solution found! it's at ", end='')
    
        garbled_list = str_list(y[current_lst])
        garbled_list[lst_position] = '.'
        y[current_lst] = list_str(garbled_list)
        try:
            current_pos = stack.pop()
            current_lst,lst_position = current_pos[0], current_pos[1]
        except:
            print('no solution found')
            break
        if found:
            print(current_pos)

    
start_maze(y)