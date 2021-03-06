# Maximum Sub-Array Problem

Implementation of different algorithms around the maximum subarray problem.

## def kadane(inputarray):

Kadane's algorithm for calculating the sum of the largest subarray.
Copied from http://en.wikipedia.org/wiki/Maximum_subarray_problem on June 22, 2013
Returns the sum of the subarray
Runs in O(n) time

## def kadaneWithSubarray(inputarray):

Calculates the sum of the largest subarray and the subarray itself
Modified from code in http://en.wikipedia.org/wiki/Maximum_subarray_problem on June 22, 2013
Returns the starting index of the subarray, the size of the subarray, and the sum of the subarray
Runs in O(n) time

Returns index_of_subarray, length_of_subarray, sum_of_values_in_subarray

## def bruteForce(inputarray):

Brute force method for solving the maximum subarray problem
Returns the starting index of the subarray, the size of the subarray, and the sum of the subarray
Runs in O(n^2) time

Returns index_of_subarray, length_of_subarray, sum_of_values_in_subarray
