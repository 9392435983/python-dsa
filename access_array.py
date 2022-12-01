from array import *
arr = array('i',[9,8,7,6])
def access_array(arr,index):
    if index>len(arr):
        print("there is no element in the above array")
    else:
        print(arr[index])
access_array(arr,3)#.................time complex..o(1)