# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

# open file
with open(file_path, "r") as file:
    ans = 0
    lst = file.readlines()
    for line in lst:
        my_line = list(map(int, line.split()))
        my_bool = True
        sorted_line = my_line.copy()
        sorted_line.sort()
        if my_line == sorted_line or my_line[::-1] == sorted_line:
            for i in range(1, len(my_line)):
                if abs(my_line[i]-my_line[i-1])>3 or abs(my_line[i]-my_line[i-1])<1:
                    my_bool = False
            if my_bool:
                ans+=1
    print(ans)