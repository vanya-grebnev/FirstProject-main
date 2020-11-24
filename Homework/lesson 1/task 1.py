for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            A = not (a or not b and c) or c
            B = not (a and not b or c) and b
            C = not (not a or b and c) or a
            print("a=" + str(bool(a)) + " b=" + str(bool(b)) + " c=" + str(bool(c)))
            print("A = not(a or not b and c) or c")
            print("A=" + str(bool(A)))
            print("B = not (a and not b or c) and b")
            print("B=" + str(bool(B)))
            print("C = not (not a or b and c) or a")
            print("C=" + str(bool(C)))
            print()
