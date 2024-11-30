import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    
    # Loop through both lists and compare each element
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1  # Increment a's score
        elif a[i] < b[i]:
            b_score += 1  # Increment b's score
    
    # Return the final scores as a list
    return [a_score, b_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
