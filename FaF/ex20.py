from sys import argv

script, input_file = argv

def print_all(file):
    print(file.read())
    
def rewind(file):
    file.seek(0)
    
    def print_a_line(line_count, f):
        print(line_count, f.readline())
        
current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines: ")

Current_line = 1
print_a_line(current_line, current_file)

Current_linen = current_ file + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
