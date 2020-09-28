# the list "students" is already defined
print([student for grade in students for student in grade if grade[1] == "A"][::2])
