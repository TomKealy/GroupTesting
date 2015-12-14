def genab(lower_bound, upper_bound):
    combinations = []
    for a in range(lower_bound, upper_bound+1):
        for b in range(lower_bound, upper_bound+1):
            combinations.append(a**b)
    return combinations
