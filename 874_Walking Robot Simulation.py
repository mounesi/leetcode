"""
A robot on an infinite XY-plane starts at point (0, 0) 
and faces north. The robot can receive one of three possible 
types of commands:

-2: turn left 90 degrees,
-1: turn right 90 degrees, or
1 <= k <= 9: move forward k units.
Some of the grid squares are obstacles. The ith obstacle is at
 grid point obstacles[i] = (xi, yi).

If the robot would try to move onto them, the robot stays on the 
previous grid square instead (but still continues following the 
rest of the route.)

Return the maximum Euclidean distance that the robot will be from
the origin squared (i.e. if the distance is 5, return 25).

Input: commands = [4,-1,3], obstacles = []
Output: 25

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
"""


class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0

        global obstacleSet
        # to eliminate duplicates 
        # map to apply tuple operation on all lists
        obstacleSet = set(map(tuple, obstacles))

        # ans is the maxximum value at every position
        ans = 0

        for cmd in commands:
            # set the orientation of the global frame
            # remaintder of by 4 
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                # to move one step at a time
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans



my_solution = Solution()
output = my_solution.robotSim([4,-1,4,-2,4], [[2,4], [1,6]])
print (output)


    


    





