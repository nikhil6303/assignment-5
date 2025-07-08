dict={'Alice':85,'bobby':75,'jack':95}
n=input('enter the name of the student:')
try:
    print(n,'marks',dict[n])
except KeyError:
    print("name not found")
