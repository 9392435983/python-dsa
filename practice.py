from array import *
from cgi import print_arguments
#creation and traverse of array
arr = array('i',[1,2,3,4,5])
for i in arr:
    print(i)
#acces array elements through indexes
print("step 2")
print(arr[0])
#add an element using append method
print("step 3")
arr.append(6)
print(arr)
#insert value in an array using insert method
print("step 4")
arr.insert(6,8)
print(arr)
#extend array using extend method
print("step 5")
arr1 = array('i',[7,9,10])
arr.extend(arr1)
print(arr)
#add items from list into array using fromList method
print('step 6')
temp_list = [11,12,13]
arr.fromlist(temp_list)
print(arr)
#remove an element by using remove method
print("step 7")
arr.remove(2)
print(arr)
#remove last array element using pop() method
print("step 6")
arr.pop()
print(arr)
#fetch any elements index using index method
print("step 7")
print(arr.index(12))
#revese a python array using reverse() method
print("step 10")
arr.reverse()
print(arr)
#get array buffer informatuon through buffer_info method
print("step 11")
print(arr.buffer_info())
#check for no.of accrances of an element
print("step 12")
print(arr.count(1))
#conver array to a python list with same elements using tolist() mthod
print("step 13")
print(arr.tolist())
# slice elements from an array
print("step 14")
print(arr[1:4])#[including:exluding]
#length of the array
print(len(arr))
