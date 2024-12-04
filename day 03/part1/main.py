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
    for item in lst:
        # use regex to find all mul(num, num)
        items+=re.findall("mul\([0-9]+,[0-9]+\)", str(item))
    for a in items:
        # isolating both number
        nums = re.findall("[0-9]+,[0-9]+", str(a))
        a, b = list(map(int, nums[0].split(',')))
        ans+=a*b
    print(ans)