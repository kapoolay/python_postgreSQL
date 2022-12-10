l = ["Bob", "Rolf", "Anne"]    # a list uses square brackets. You can add/remove elements from a list. Orders stay the same.
t = ("Bob", "Rolf", "Anne")    # tuple uses regular brackets. CANNOT add/remove elements from a tuple. Orders stay the same.
s = {"Bob", "Rolf", "Anne"}    # Add/Remove elements, but CANNOT HAVE DUPLICATE elements. Order IS NOT guaranteed.

print(l[0])    # this is subscript notation. Elements in programming usually start at 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modify "Bob" to be "Smith" in the list
# l[0] = "Smith"
# print(l)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Add "Smith" to the end of the list
l.append("Smith")    # .append() adds an element to the end of the list
print(l)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Remove "Bob" from the list
l.remove("Bob")
print(l)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Add "Smith" into the set
s.add("Smith")    # append does not work for sets bc they do not have an order
print(s)