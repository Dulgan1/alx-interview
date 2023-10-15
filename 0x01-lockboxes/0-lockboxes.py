#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to
the other boxes.

Write a method that determines if all the boxes can be opened.

1. Prototype: def canUnlockAll(boxes)
2. boxes is a list of lists
3. A key with the same number as a box opens that box
4. You can assume all keys will be positive integers
5. There can be keys that do not have boxes
6. The first box boxes[0] is unlocked
8. Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Unlock all check function
    """
    unlocked = [boxes[0]]
    for box in boxes:
        key_box = unlocked[-1]
        if len(key_box) == 1:
            unlocked.append(boxes[key_box[0]])
        elif len(key_box) == 0:
            unlocked.append(list())
        else:
            for i in range(len(key_box) - 1):
                if len(key_box) < key_box[i]:
                    unlocked.append(key_box[i])
                unlocked.append(boxes[key_box[i]])
    if len(unlocked) >= len(boxes):
        return True
    return False
