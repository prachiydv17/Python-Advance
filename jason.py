import jason

with open("student.jason","r")as file:
    data= jason.load(file)

print(data)    