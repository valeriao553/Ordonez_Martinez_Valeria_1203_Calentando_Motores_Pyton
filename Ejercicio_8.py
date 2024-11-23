print(" ")
print(" Ordonez Martinez Valeria")
print(" ")
def sPos(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return True
            else:
                return False
print(sPos([1,2,3,4,5],[6,7,8,9,0]))
print(sPos([1,2,3,4],[1,6,7,8,8]))
print(" ")