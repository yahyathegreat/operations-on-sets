my_set = {1,2,3}
print(my_set)
my_set = {1.0, "HELLO", (1,2,3)}
print(my_set)
num_set = set([0, 1, 3, 4, 5])
print("oringinal set:")
print(num_set)
num_set.pop()
print("after removing the first element from the said set")
print(num_set,"\n")
yahya1 = {"green", "blue"}
yahya2 = {"green", "red"}
print("oringinal set elements:")
print(yahya1)
print(yahya2)
print("\nintersection of two said sets:")
setz = yahya1.intersection(yahya2)
print(setz)
print(yahya1.union(yahya2))
import array as arr
array_num = arr.array('i', [1,3,5,4,5,7,5])
print("original array: "+str(array_num))
print("number of occurrences of the number 5 in the said array:"+str(array_num))
array_num.reverse()
print("reverse the order of the items:")
print(str(array_num))