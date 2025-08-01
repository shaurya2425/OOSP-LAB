students = ("Amit", "Bhavna", "Chetan", "Divya", "Esha")
print("All students:", students)

new_student="Shaurya"

students+=(new_student,)

print("After adding new student:",students)

# we can't delete any item in tuple directly first we need to convert it into the list 
students_list=list(students)
students_list.remove("Chetan")
students=tuple(students_list);
print("After deleting a student", students)



print("Names from 1st to 3rd: ",students[1:4])


# we can't directly modify the tuple first we need it to convert to the list and then only we can modify the item

students_list=list(students)
students_list[2]="Vansh"
students=tuple(students_list)
print("After modifying the index 2", students)




































