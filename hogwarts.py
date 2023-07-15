#students = ["Hermione", "Harry", "Ron"]

#print(students[0])
#print(students[1])
#print(students[2])

#for student in students:
   # print(student)

#for i in range(len(students)):
 #   print(i + 1, students[i])

#students = {
#    "Hermione": "Gryffindor",
#    "Harry": "Gryffindor",
#    "Ron": "Griffindor",
#    "Draco": "Slytherin",
 #}

#print(students["Hermione"])
#for student in students:
#    print(student, students[student], sep=" | ")

students = [
    {"name": "Hermione", "house": "Gryffindor","patronus": "Otter" },
    {"name": "Harry", "house": "Gryffindor","patronus": "Stag" },
    {"name": "Ron", "house": "Gryffindor","patronus": "Jack Russel terrier" },
    {"name": "Draco", "house": "Slytherin","patronus": "None" },        
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" | ")