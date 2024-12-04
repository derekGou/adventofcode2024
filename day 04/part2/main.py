# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

# open file
with open(file_path, "r") as file:
    lst = [line.rstrip() for line in file.readlines()]
    ans = 0
    
    for row in range(1, len(lst)-1):
        for col in range(1, len(lst[row])-1):
            # find all 'A'
            if lst[row][col]=='A':
                # find 'M' in adjacent corners, then 'S'
                if lst[row-1][col-1]=='M':
                    if lst[row+1][col-1]=='M':
                        if lst[row+1][col+1] == 'S' and lst[row-1][col+1] =='S':
                            ans+=1
                    if lst[row-1][col+1]=='M':
                        if lst[row+1][col+1] == 'S' and lst[row+1][col-1] =='S':
                            ans+=1
                if lst[row+1][col+1]=='M':
                    if lst[row+1][col-1]=='M':
                        if lst[row-1][col+1] == 'S' and lst[row-1][col-1] =='S':
                            ans+=1
                    if lst[row-1][col+1]=='M':
                        if lst[row+1][col-1] == 'S' and lst[row-1][col-1] =='S':
                            ans+=1
print(ans)