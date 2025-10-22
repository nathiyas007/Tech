# Activity 1: Tuples Basics
# 1. Determine the length of the fruits tuple.
fruits = ("apple", "banana", "cherry", "mango")
print(len(fruits))
# 2.Identify the index of the initial occurrence of "banana".
print(fruits.index("banana"))
# 3.Attempt to modify "cherry" to "grape" within the tuple. Explain the outcome and the reason behind it.
fruits = ("apple", "banana", "cherry", "mango")
kk = list(fruits)
kk[1] = 'Pomogranate'
fruits = tuple(kk)
print(fruits)
# 4.Transform the tuple into a list, make a modification, and then convert it back to a tuple.
fruits = ("apple", "banana", "cherry", "mango")
so = list(fruits)
so.append("Jackfruit")
fruits = tuple(so)
print(fruits)
# Activity 2: Tuples Grouping
# 1. Combine colors and shapes to create a new tuple called art.
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
print(art)
# 2.Demonstrate how to repeat a tuple, specifically colors three times.
# 3.Add an art element called “Diamond” to the art tuple.
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
kk = list(art)
kk.append("Diamond")
art = tuple(kk)
print(art)
# 4.Extract and print the middle element from the art tuple using slicing.
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors +  shapes
middle_index = len(art) // 2
middle_index_end = middle_index + 1
print(art[middle_index:middle_index_end])
# 5.Verify if the string "square" exists within the art tuple.
colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors +  shapes
print("square" in art)