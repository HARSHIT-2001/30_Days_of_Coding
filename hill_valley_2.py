def hillvalley_approach1(l):
    # Check if the list has at least 3 elements
    if len(l) < 3:
        return False

    is_hill = False
    is_valley = False
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if is_valley:  # If valley found before hill
                return False
            is_hill = True
        elif l[i] < l[i-1]:
            if is_hill:  # If hill found before valley
                return False
            is_valley = True

    return is_hill or is_valley


def hillvalley_approach2(l):
    # Check if the list has at least 3 elements
    if len(l) < 3:
        return False

    is_hill = False
    is_valley = False
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if is_valley:  # If valley found before hill
                return False
            is_hill = True
        elif l[i] < l[i-1]:
            if is_hill:  # If hill found before valley
                return False
            is_valley = True

    return is_hill and is_valley



def hillvalley_approach3(l):
    # Check if the list has at least 3 elements
    if len(l) < 3:
        return False

    # Check for hill
    is_hill = False
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            is_hill = True
        elif l[i] < l[i-1]:
            break
    if not is_hill:
        return False

    # Check for valley
    is_valley = False
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            is_valley = True
        elif l[i] > l[i-1]:
            break
    if not is_valley:
        return False

    return True


# Test cases
tests = [
    [1, 2, 3, 5, 4, 3, 2, 1],  # True (hill)
    [1, 2, 3, 4, 5, 3, 2, 4, 5, 3, 2, 1],  # False
    [9, 5, 4, -1, -2, 3, 7],  # True (valley)
    [5, 4, 3, 2, 1, 0, -1, -2, -3],  # False
    [1, 2, 3, 2, 1],  # True (hill)
    [5, 4, 3, 4, 5],  # True (valley)
    [1, 2, 3],  # False
    [3, 2, 1],  # False
    [1, 2, 2, 1],  # False
]

# Execute all approaches
for test in tests:
    print(f"Input: {test}")
    print(f"Approach 1: {hillvalley_approach1(test)}")
    print(f"Approach 2: {hillvalley_approach2(test)}")
    print(f"Approach 3: {hillvalley_approach3(test)}")
    print()
