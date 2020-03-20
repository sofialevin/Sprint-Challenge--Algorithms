#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

The runtime will increase linearly in proportion to the size of n.

b) O (n log n)

The for loop is running a O(n) (the run time will increase as n increases). The while loop is running at log n, because n has to increase from n to n + 2 for the while loop to run 1 more time, i.e. the time complexity doesn't increase at the same rate as n.

c) O(n)

Even though the function is recursive, it still will only runs based on how many bunnies there are, so the runtime will also increase linearly in proportion to the size of n.

## Exercise II

Assuming the building is an array, where each floor is a boolean for whether "egg gets broken" is true or false. The egg will not break on the first few floors, but it will definitely break on the top floors.

So the building array would be something like: 

n = [false, false, false, ..., true, true, true]

To determine the value of f I would loop through the building floors, starting at 0, checking if the floor is false or true. If false, I would increase the floor (f += 1) and try again until I found the first floor where it returns true.

This is a runtime complexity of O(n), since the runtime will increase linearly as n (the number of floors) increases.


