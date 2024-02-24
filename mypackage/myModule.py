def top_n (items, n):
    """ return the top n items in array  , in desc order
    Args:
        items array: list  or aarray lie - list
        n (int):  num of items to return

    return: 
        array: top n items . in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
        
    """

    for i in range(n): # keep sorting untile we have top n items

        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j] , items[j+1] = items[j+1] , items[j]


    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]

