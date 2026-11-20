#Unit-3C_Task-3_Remove_Duplicates_Using_Sets.py
# Example solution: remove duplicates using sets
list_data = [1, 3, 2, 5, 6, 6, 4, 4, 2, 1, 9]

unique_set = set(list_data)
unique_list = list(unique_set)

print("Original:", list_data)
print("Unique set:", unique_set)
print("Unique list:", unique_list)