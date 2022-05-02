# CMPS 2200 Assignment 5
## Answers

**Name:** Keith J Mitchell


Place all written answers from `assignment-05.md` here for easier grading.


- **1a.** Given a $N$ dollars, state a greedy algorithm for producing as few coins as possible that sum to $N$. Please discuss if this algorithm is optimal or not.
  - A greedy algorithm that yields to fewest coins possible would be one which takes the largest valued coins first. The value input would reduce by each coin taken away while greater than 0 and printing out the result once 0 is attained. This would not be an optimal solution as it is too close and slow as a linear search.
    

- **1b.** What is the work and span of your algorithm?
  - The work and span of my algorithm would be O(n) 


- **2a.** You realize the greedy algorithm you devised above doesn't work in Fortuito. Give a simple counterexample that shows that the greedy algorithm does not produce the fewest number of coins. Please discuss why greedy algorithm cannot work optionally.
  - A counter example would be with coins = [1, 6, 8, 9, 10] and the input amount being 14. The algorithm used in question 1a would yield (10, 1, 1, 1, 1) while the optimal solution would be (8, 6).

  
- **2b.** Use this optimal substructure property to design a dynamic programming algorithm for this problem. If you used top-down or bottom-up memoization to avoid recomputing solutions to subproblems, what is the work and span of your approach?
  - A dynamic approach would be to iterate through every possible combination of coins and finding the one that results in the least total coins used. In doing so the work and span would be increased to O(n^2) as the algorithm now exponentially searches through coin arrangements. 