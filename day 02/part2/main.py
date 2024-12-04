# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

# open file
with open(file_path, "r") as file:
    ans = 0
    lst = [line.rstrip() for line in file.readlines()]
    for line in lst:
        # parse input
        my_line = list(map(int, line.split()))
        my_bool = None
        sorted_line = my_line.copy()
        sorted_line.sort()
        # check if initial conditions are met
        if my_line == sorted_line or my_line[::-1] == sorted_line:
            my_bool = True
            for i in range(1, len(my_line)):
                if abs(my_line[i]-my_line[i-1])>3 or abs(my_line[i]-my_line[i-1])<1:
                    my_bool = False
        
        # popping and checking again - unoptimized
        if my_bool!=True:
            my_bool = None
            for x in range(len(my_line)):
                new_line = my_line.copy()
                new_line.pop(x)
                new_sorted_line = new_line.copy()
                new_sorted_line.sort()
                if new_line == new_sorted_line or new_line[::-1] == new_sorted_line:
                    my_bool = True
                    for a in range(1, len(new_line)):
                        if abs(new_line[a]-new_line[a-1])>3 or abs(new_line[a]-new_line[a-1])<1:
                            my_bool = False
                if my_bool:
                    break
        if my_bool:
            ans+=1
    print(ans)