from array import*
arr = array('i',[4,5,6,7,8])
def searching_element_in_arrray(arr,value):
    for i in arr:
        if i == value:
            return arr.index(value)
    return "the item does not exist in array"
print(searching_element_in_arrray(arr,6))#................o(n)