import cPickle as pickle

def rotations(L):
    """takes in a 3x3 grid and returns a list of all 4 possible outcomes from rotation"""
    def rotate(In):
        """returns a copy of the 3x3 2-d array rotated once counter-clockwise"""
        #copies In
        L = [In[i][:] for i in range(3)]
        # rotate the corners once
        temp = L[0][0]
        L[0][0] = L[0][2]
        L[0][2] = L[2][2]
        L[2][2] = L[2][0]
        L[2][0] = temp
        # rotate the edges once
        temp = L[1][0]
        L[1][0] = L[0][1]
        L[0][1] = L[1][2]
        L[1][2] = L[2][1]
        L[2][1] = temp
        return L
    out = []
    out.append(L)
    for i in range(3):
        out.append(rotate(out[-1]))
    return out

OLL_1 = [[1, 1, 2],
         [0, 0, 0]
         [2, 1, 2]]


if __name__ == "__main__":
    exit()
    test =[[1,2,3],
           [4,5,6],
           [7,8,9]]
    out = rotations(test)

    for value in out:
        for line in value:
            print line
        print '\n'