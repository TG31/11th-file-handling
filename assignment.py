# Exercise 1
def write_shopping_list(items, filename):
    file = open(filename, "w")
    c = 1
    for i in items:
        file.write(f"{c}. {i}\n")
        c += 1
    file.close()
items = ["Bread", "Milk", "Eggs"]
filename = "shopping_list.txt"
write_shopping_list(items, filename)

# Exercise 2
def read_names(filename):
    file = open(filename, "r")
    lst = []
    lines = file.readlines()
    for line in lines:
        if line.strip() != "":
            lst.append(line.strip())
    print(lst)
    file.close()
filename = "names.tsx"
read_names(filename)

# Exercise 3
def append_entry(filename, text):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    file = open(filename, "a")
    for item in text:
        found = False
        for line in lines:
            if line.strip() == item:
                found = True
        if found == False:
            file.write(item + "\n")
    file.close()
filename = "log.txt"
text = ["Mon", "Tue", "Wed"]
append_entry(filename, text)

# Exercise 4
def search_file(filename, word):
    # Write your code here
    pass

# Exercise 5
def number_the_lines(source, destination):
    # Write your code here
    pass
