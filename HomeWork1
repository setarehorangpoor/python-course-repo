#Achtung:For every function here you enter the element number NOT the index.


##################### TASK 1 ##################################

#function to sum the first and last elements in any list
def SumFirstLast(anylist):
            
    return anylist[0]+ anylist[len(anylist)-1]


#function to sum any two element in any list
def SumTwoElements(anylist,element1,element2):
    
    if ( (element2 - 1) > (len(anylist)-1 or (element1 - 1) > (len(anylist)-1 ))): 
        print('R u being clever? one of the damn elements is out of the list range')        
    return anylist[element1-1]+ anylist[element2-1]

##################### TASK 2 ##################################

# function is to convert any element to string in any list
def ConvertToString(anylist,element_number):
    if ( (element_number) > (len(anylist)-1 )):
        print('R u being clever? one of the damn elements is out of the list range')
    
    newlist = anylist.copy()
    newlist[element_number-1] = str(newlist[element_number-1])
    return newlist
        
##################### TASK 3 ##################################

#function is to swap any two element in any list
def SwapTwoElements(anylist,element1,element2):
    if ( (element2 - 1) > (len(anylist)-1 or (element1 - 1) > (len(anylist)-1 ))):    
        print('R u being clever? one of the damn elements is out of the list range')
    
    newlist = anylist.copy() 
    swap = newlist[element2-1]
    newlist[element2-1] = newlist[element1-1]
    newlist[element1-1] = swap
    return newlist

############################ Example ########################


ali = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

x = SumFirstLast(ali)
print('the sum of the first element and last element = ',x, '\n')
y = SumTwoElements(ali,1,12)
print('the sum of the two chosen elements = ',y , '\n')
z = ConvertToString(ali,11)
print('the list after converting the chosen element to string =')
print(z, '\n')
m = SwapTwoElements(ali, 1, 14)
print('the list after Swaping the chosen two elements =')
print(m, '\n')
print('the original list =')
print(ali, '\n')
