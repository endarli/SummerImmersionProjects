List = [1, 2, 3]
print(List)

List.append([4, 5])
print(List)
#adds the list to the list

List.extend([6, 7])
print(List)
#adds the data from one list to another

obj_slice = slice(0, 6, 2)
print(List[obj_slice])
#first element in slice function is where slicing starts
#second element in slice function is where slicing ends
#third element in slice function is the increments in which it does so

vowels = ["a", "e", "i", "o", "u"]
index = vowels.index("o")
print("the index of e is:", index)
#index tells you the index of a #

List1 = [7, 10, 3, 8, 5, 6]
#has to be same data type for this function to work
List2 = ["cat", "dog", "cow", "PIG", "APPLE"]
List1.sort()
List2.sort(reverse = True)
print("sorted list:", List1)
print("sorted list (in descending):", List2)

#tuples
tup = ("python", "geeks")
print(tup)
tuple3 = ("python",)*3
print(tuple3)
#they are set lists
