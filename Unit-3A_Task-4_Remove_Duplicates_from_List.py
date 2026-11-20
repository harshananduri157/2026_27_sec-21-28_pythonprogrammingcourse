#Unit-3A_Task-4_Remove_Duplicates_from_List.py
# Example solution: remove duplicates from a list
list_data = [1, 2, 3, 2, 4, 1, 5]
print("Original:", list_data)

list_data = list(set(list_data))
print("After removing duplicates:", list_data)