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

The objective is to find the first true value.

To start I would check the middle floor. If the egg breaks, I would move on to check the halfway point of the floors below. If it doesn't break I would move on to check from the halfway point of the floors above and so on.

Once I find a "true" I would still need to keep checking because I want to find the lowest floor with a value of "true". So when I find a "true" I would temporarily store that index in "f". Whenever I find a "true" with a lower index/floor value I would update the value of "f", until there are no more floors to check.

true
true
true
true
true
true    <-    <-
true                <-
false         <-
false
false   <-