# Read a .txt file and print its contents
file_path = 'doc.txt'
with open(file_path, 'r') as file:
    contents = file.read()
    print(contents) 

