#!/usr/bin/python3
"""
 50-island_perimeter
 Technical interview practice:
 A grid containing 1s and 0s represents and island
 where 1 is a square cell of land with sides of length 1, and 0 of water.
 This function calculates the perimeter of the island.
 Use with  test file 5-main.py, default grid perimeter is 12,
 tweak grid for different perimeter.
"""
# v1.0
# def island_perimeter(space):
#    Function to get perimeter
#    pmetre = 0
#    for x in range(len(space)):
#        for y in range(len(space[x])):
#            if space[x][y] == 1:
#                if space[x - 1][y] == 0: # check cell above
#                    pmetre += 1
#                if space[x + 1][y] == 0: # check cell below
#                    pmetre += 1
#                if space[x][y - 1] == 0: # check cell by left
#                    pmetre += 1
#                if space[x][y + 1] == 0: # check cell by right
#                    pmetre += 1
#    return pmetre


def island_perimeter(space):
    """ Function to get parametre """
    pmetre = 0
    for x in range(len(space)):
        for y in range(len(space[0])):
            if space[x][y] == 1:
                if x == 0 or space[x - 1][y] == 0:
                    pmetre += 1
                if x == (len(space) - 1) or \
                        space[x + 1][y] == 0:
                    pmetre += 1
                if y == 0 or space[x][y - 1] == 0:
                    pmetre += 1
                if y == (len(space[0]) - 1) or \
                        space[x][y + 1] == 0:
                    pmetre += 1
    return pmetre
