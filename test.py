from collections import defaultdict

def restoreArray(adjacentPairs):
    adjacency_dict = defaultdict(list)
    # Build the adjacency dictionary
    for pair in adjacentPairs:
        adjacency_dict[pair[0]].append(pair[1])
        adjacency_dict[pair[1]].append(pair[0])
    # Find the start of the array
    start = None
    for key, value in adjacency_dict.items():
        if len(value) == 1:
            start = key
            break
    # Reconstruct the array
    n = len(adjacentPairs) + 1
    nums = [0] * n
    nums[0] = start
    for i in range(1, n):
        next_element = adjacency_dict[start][0]
        nums[i] = next_element
        adjacency_dict[next_element].remove(start)
        start = next_element
    return nums

if __name__ == "__main__" : 
    res = restoreArray([[1,2],[-3,7],[2,7],[-3,12]])
    print(res)