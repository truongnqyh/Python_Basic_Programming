############# r/w/a/r+
# read, readline, readlines
# write, writeline
def write_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n") # overwrite all the content of the file

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in file: ")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!!!")

fruits = ["apple", "orange", "banana", "watermelon"]
write_to_file("fruits.txt", fruits)
read_from_file("fruits.txt")