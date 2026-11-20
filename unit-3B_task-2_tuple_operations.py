#Unit-3B_Task-2_Tuple_Operations.py
# # Example solution: tuple operations
tuple_data = (1, 4, 3)
tuple_extra = (2, 5)

joined = tuple_data + tuple_extra
print("Joined:", joined)

print("Slice first two:", tuple_data[:2])

a, b, c = tuple_data
print("Unpacked:", a, b, c)	