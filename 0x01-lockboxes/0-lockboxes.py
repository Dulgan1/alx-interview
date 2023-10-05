#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked = [boxes[0]]
    print(boxes)
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
        print(unlocked)
    if len(unlocked) >= len(boxes):
        return True
    return False


if __name__ == "__main__":
    print(canUnlockAll([[1], [2], [3], [4], []]))
    print(canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]))
    print(canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))
