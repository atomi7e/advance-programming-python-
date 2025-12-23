'''Condition
At the input we have a list of strings of different lengths.
It is necessary to write the all_eq(list) function, which will return a new list of
strings of the same length.
The length of the final line is determined based on the largest of them.
If a particular line is shorter than the longest, add underscores from the right edge
to the required number of characters.
Do not change the location of the elements of the initial list.
First you need to determine the length of each row in the list and find the
maximum. Next, we add the characters "_" to the strings whose length is less.'''

def all_eq(lst):
    if not lst:
        return []
    max_len = max(len(s) for s in lst)
    
    return [s.ljust(max_len, "_") for s in lst]

if __name__ == '__main__':
    n = int(input())
    
    data = [input() for _ in range(n)]
    
    result = all_eq(data)

    print(*result, sep='\n')