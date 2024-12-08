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
