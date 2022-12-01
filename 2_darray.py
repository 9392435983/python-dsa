import numpy as np
twode = np.array([[11,23,45,26],[10,22,44,27]]) 
print(twode)

newtd = np.insert(twode, 0, [[56,12,47,56]], axis=0)
print(newtd)