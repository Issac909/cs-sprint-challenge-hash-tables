def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    results = []
    
    for little_arr in arrays:
        for x in little_arr:
            if x not in dictionary:
                dictionary[x] = 1
                
            else:
                results.append(x)
                
    result = list(dict.fromkeys(results))

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
