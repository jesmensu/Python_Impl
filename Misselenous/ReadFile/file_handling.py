x= ""
with open('Misselenous/ReadFile/sample.txt', 'r') as f:
    f.seek(8)
    x = f.read()
    y = f.name

    print(y)

print(x)



import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# Delete file test2.txt
os.remove("text2.txt")

# Create a directory "test"
os.mkdir("test")

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")


# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )

# Changing a directory to "/home/newdir"
os.chdir("Misselenous/ReadFile")
with open('sample.txt', 'r') as f:
    x = f.read()
    y = f.name
    print(y)
    print(x)


