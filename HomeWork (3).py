import copy

my_list = [3,4,5,6,7,8,9,10]

sum = my_list[0] + my_list[7]

print (sum)

my_list1 = copy.deepcopy (my_list)
my_list1[6] = str(my_list1[6])
print (my_list1)


my_list2 = copy.deepcopy (my_list)
my_list2[3],  my_list2[4] = my_list2[4],  my_list2[3]
print (my_list2)