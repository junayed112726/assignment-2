#problem2.py
user = input("Enter ur name : ")

name = open("name.txt","w")
name.write(user)
name.close()
print("Name saved successfully.")