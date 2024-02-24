def top_n(items, n):
    """Returns the n items in an array-like object in descending order

    Args:
        items (array): list or array-like object
        n (int): number of items to return
        
    Returns:
        array: top n items in descending order
        
    Examples:
        
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
        
        >>> top_n([10, 1, 12, 9, 3], 2)
        [12, 10]
        
        >>> top_n([1, 2, 3, 4, 5], 4)
        [5, 4, 3, 2]
    """
    
    for i in range(n): # keep sorting until we have the top n items
        for j in range(0, len(items)-1-i):
            
            if items[j] > items[j+1]: # if this item is bigger than the item..
                items[j], items[j+1] = items[j+1], items[j] # swap the two items!
    
    top_n = items[-n:]
    return top_n[::-1]
    
    
print(top_n([8, 3, 2, 7, 4], 3))
print(top_n([10, 1, 12, 9, 3], 2))
print(top_n([1, 2, 3, 4, 5], 4))
