# directory of the script
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

import re

ans = 0
# open file
with open(file_path, "r") as file:
    lst = [line.rstrip() for line in file.readlines()]
    items = []
    dos = []
    donts = []
    for item in lst:
        # use regex to find all mul(num, num), do() or don't()
        items+=re.findall("mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", str(item))
    # toggle boolean for do() or don't()
    bool = True
    for a in items:
        if str(a)=='do()':
            bool = True
        elif str(a)=='don\'t()':
            bool = False
        elif bool:
            # isolating number
            nums = re.findall("[0-9]+,[0-9]+", str(a))
            if len(nums)>0:
                a, b = list(map(int, nums[0].split(',')))
                ans+=a*b
    print(ans)