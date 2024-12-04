# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

# open file
with open(file_path, "r") as file:
    lst = [line.rstrip() for line in file.readlines()]
    ans = 0

    # search algorithm - recursion
    def search(row, col, i, dir):
        global lst
        print(len(lst), row)
        if i==4:
            return True
        elif row<0 or row>=len(lst) or col<0 or col>=len(lst[0]) or 'XMAS'[i]!=lst[row][col]:
            return False
        bool = False
        bool = search(row + dir[0], col + dir[1], i + 1, dir)
        return bool
    
    for row in range(len(lst)):
        for col in range(len(lst[row])):
            if lst[row][col]=='X':
                # check every direction
                if search(row+1, col, 1, [1,0]):
                    ans+=1
                if search(row+1, col+1, 1, [1,1]):
                    ans+=1
                if search(row+1, col-1, 1, [1,-1]):
                    ans+=1
                if search(row+0, col+1, 1, [0,1]):
                    ans+=1
                if search(row+0, col-1, 1, [0,-1]):
                    ans+=1
                if search(row-1, col, 1, [-1,0]):
                    ans+=1
                if search(row-1, col+1, 1, [-1,1]):
                    ans+=1
                if search(row-1, col-1, 1, [-1,-1]):
                    ans+=1
print(ans)