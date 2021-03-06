'''
Created on Jun 22, 2013

@author: neverendingqs
'''

def kadane(inputarray):
    max_ending_here = max_so_far = 0

    for element in inputarray:
        max_ending_here = max(0, max_ending_here + element)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def kadane_with_subarray(inputarray):
    max_ending_here = 0
    meh_start_index = 0
    meh_subarray_length = 0

    max_so_far = 0
    msf_start_index = 0
    msf_subarray_length = 0

    for i, element in enumerate(inputarray):
        # max_ending_here = max(0, max_ending_here + element)
        if (max_ending_here + element) < 0:
            max_ending_here = 0

        else:
            if max_ending_here == 0:
                meh_start_index = i
                meh_subarray_length = 1

            else:
                meh_subarray_length += 1

            max_ending_here = max_ending_here + element

        # max_so_far = max(max_so_far, max_ending_here)
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            msf_start_index = meh_start_index
            msf_subarray_length = meh_subarray_length

    return msf_start_index, msf_subarray_length, max_so_far

def brute_force(inputarray):
    inputarraylength = len(inputarray)
    currmax = 0
    currmax_index = 0
    currmax_length = 0
    currsum = 0

    for i in range(inputarraylength):
        for j in range(i, inputarraylength):
            currsum += inputarray[j]

            if currsum > currmax:
                currmax = currsum
                currmax_index = i
                currmax_length = j - i + 1

        currsum = 0

    return currmax_index, currmax_length, currmax
