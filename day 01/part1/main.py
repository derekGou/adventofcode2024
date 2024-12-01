# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

# open file
with open(file_path, "r") as file:
    lst = file.readlines()

    # answer variable
    ans = 0

    # two lists
    lst1 = []
    lst2 = []

    # parse original list
    for item in lst:
        a, b = item.rstrip().split()
        lst1.append(int(a))
        lst2.append(int(b))

    # sort
    lst1.sort()
    lst2.sort()

    # adding distances
    for i in range(len(lst1)):
        ans+=abs(lst1[i]-lst2[i])

    # print answer
    print(ans)