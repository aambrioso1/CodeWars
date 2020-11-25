def longest_repetition(chars):
    #  We are going to iterate through the characters in chars.
    #  We initialize a few variables.
    c = '' # Letter associated with maximum count.
    l = 0 # Maximum count.
    last_let = '' # Last letter
    current_let = ''  # Current letter
    current_count = 0 # Current count
    for i in chars:
        # If the last letter is the same current one, increment the count.
        if i == last_let:
            current_count += 1
        # Otherwise start all over.
        else:
            current_count = 1
            last_let = i
        # If the current count is bigger than the max so far
        # make it the new max.
        if current_count > l:
            l = current_count
            c = i
    return (c, l)