for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
        A = not(a or not b and c) or c
        B = not (a and not b or c) and b
        C = not (not a or b and c) or a
            print(A, B, C)