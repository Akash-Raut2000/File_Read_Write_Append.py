# Writing to a file using 'w' mode
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a simple file handling example.\n")

# Appending to a file using 'a' mode
with open('example.txt', 'a') as file:
    file.write("Appending a new line to the file.\n")

# Reading from a file using 'r' mode
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire file
    print("File Content:\n", content)

# Reading file line by line
with open('example.txt', 'r') as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # Remove extra whitespace/newlines
