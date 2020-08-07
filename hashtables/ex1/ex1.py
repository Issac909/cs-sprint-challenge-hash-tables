def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    
    if length <= 1:
        return None

    for i in range(length):
        current = weights[i]
        
        if current in dictionary:
            prev = dictionary[current]
            return (i, prev)
        
        dictionary[limit - weights[i]] = i

    return None
