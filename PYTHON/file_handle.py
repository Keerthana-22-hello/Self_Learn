# file handling

'''
Mode            Description
-----------------------------------------------------------
'r'	            Read (default). Error if file doesn't exist
'w'	            Write. Overwrites if file exists
'a'	            Append. Adds content to the end
'x'	            Create. Error if file exists
'b'	            Binary mode (e.g., 'rb', 'wb')
'+'	            Read and write (e.g., 'r+')
'''
file=open("a.txt","w")
file.write("Hello World!\n")
file.write("I am doing well.\n")
file.close()
print("\nFile Written successfuly..")

file=open("a.txt","a")
file.write("Miss. Keerthana interested in coding.\n")
file.write('So she is taking B.E. CSE.')
file.close()
print("\nFile appended successfully..")

file=open("a.txt","r")
content=file.read()
print(content)
file.close()
print("\nFile read successfully")
print()
print()
with open("a.txt","a") as f:
    f.write("As you cn see, I'm saying this to you through the code...\nSo, come with me let' enjoy the tech world as per our wish..")
print()
with open("a.txt","r") as r:
    print(r.read())
print();print("file read successfully using with statement")
