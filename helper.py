#!/usr/bin/env python3
##########
# HELPER #
##########

# The purpose of this script is to help with organizations and to-do lists.

# Import modules
import sys

'''We assume that the data_lists.txt file already exists'''

## Utils
def read_file(file):
    '''Returns the list of lines from the file'''
    f = open(file, "r")
    data = f.readlines()
    f.close()
    return data


## Lists
'''
Here, we will find the functions handling the file data_lists.txt.
Lists representation :
- one list <-> one line
- one list :
  noun ; category ; elt1 $ etlt2 $ elt3 ...
'''

def read_lists():
    '''Returns the data for lists'''
    data = read_file("data_lists.txt")
    result = []
    for line in data:
        line = line.strip()
        if line == "":
            continue
        line = line.split(";")
        result.append((line[0], line[1], line[2].split("$")))
    return result

def write_list(data):
    '''Writes the new list (stored in data) in the file'''
    f = open("data_lists.txt", "a")
    f.write(data[0] + ";" + data[1] + ";" + "$".join(data[2]) + "\n")
    f.close()

def rewrites_all(data):
    '''Rewrites everything from data'''
    f = open("data_lists.txt", "w")
    for line in data:
        f.write(line[0] + ";" + line[1] + ";" + "$".join(line[2]) + "\n")
    f.close()

def print_list(l):
    '''Prints a list (pretty-printer)'''
    name = l[0]
    category = l[1]
    content = l[2]
    print("\x1b[31m\x1b[1mList {}:\x1b[0m".format(name))
    print("Category : {}".format(category))
    for item in content:
        print("- {}".format(item))


## Operators
# How to ask for a list l
def view(l):
    '''Views a list'''
    data = read_lists()
    for list in data :
        if list[0] == l:
            print_list(list)
            return 0
    print("Error: list not found")
    return 1

# How to add a list l
def add(name, cat, list_elts):
    '''Adds a list'''
    data = read_lists()
    for list in data:
        if list[0] == name:
            print("Error: a list with this name already exists")
            return 1
    write_list([name, cat, list_elts])
    print("You created the list", name)
    return 0

# How to append an element elt to a list l
def append(list_name, elt):
    # TODO (feature) : be able to choose where we add the element -> relevant ?
    data = read_lists()
    test = False
    for line in data:
        if line[0] == list_name:
            line[2].append(elt)
            test = True
    if (not test):
        print("Error: list not found")
        return 1
    rewrites_all(data)
    return 0

# How to delete a list l
def delete(list_name):
    data = read_lists()
    data_temp = []
    test = False
    for line in data:
        if line[0] != list_name:
            data_temp.append(line)
            test = True
    if (not test):
        print("Error: list not found")
        return 1
    rewrites_all(data_temp)
    return 0

def remove_elt(list_name, elt):
    data = read_lists()
    data_temp = []
    for line in data:
        if line[0] != list_name:
            data_temp.append(line)
        else:
            line_temp = line
            line_temp[2].remove(elt)
            data_temp.append(line_temp)
    rewrites_all(data_temp)
    return 0

# How to view all lists in a given category
def view_cat(cat_name):
    data = read_lists()
    L = []
    for line in data:
        if line[1] == cat_name:
            L.append(line[0])
    L = list(sorted(L))
    if len(L) == 0:
        print("Error: there is no list in this category")
        return 1
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("List of lists:"))
    for item in L:
        print("- {}".format(item[0]))
    return 0

# How to view all categories
def view_cat_names():
    data = read_lists()
    L = []
    for line in data:
        L.append(line[1])
    L = sorted(set(L))
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("Categories"))
    for item in L:
        print("- {}".format(item))
    return 0


# How to view everything
def view_all():
    data = read_lists()
    for line in data:
        print_list(line)
    return 0

# Main function

def welcome():
    print("Welcome!")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To view a list"), "view name_of_list")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To create a list"), "add name_of_list category_of_list elt1 el2 etc")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To append an element to a list"), "append name_of_list name_of_element")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To delete an element from a list"), "done name_of_list name_of_element")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To delete a list"), "delete name_of_list")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To view the lists in a category"), "view_category name_of_category")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To view the list of the categories"), "view_categories")
    print("\x1b[31m\x1b[1m{}:\x1b[0m".format("To view the list of all the lists"), "view_everything")

def main():
    if len(sys.argv) <= 1:
        welcome()
        return 0
    elif sys.argv[1] == "view":
        if len(sys.argv) <= 2 :
            print("Error: you need to specify which list to view")
            return 1
        else:
            return view(sys.argv[2])
    elif sys.argv[1] == "add":
        if len(sys.argv) <= 2:
            print("Error: you need to specify the name of the list you want to add")
            return 1
        elif len(sys.argv) <= 3:
            print("Error: you need to specify the category of the list you want to add")
            return 1
        elif len(sys.argv) <= 4:
            print("Error: you are trying to add an empty list")
            return 1
        else:
            return add(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif sys.argv[1] == "append":
        if len(sys.argv) <= 2:
            print("Error: you need to specify the name of the list")
            return 1
        elif len(sys.argv) <= 3:
            print("Error: you need to specify the element you want to append")
            return 1
        else:
            return append(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "done":
        if len(sys.argv) <= 2:
            print("Error: you need to specify the name of the list")
            return 1
        elif len(sys.argv) <= 3:
            print("Error: you need to specify the element you want to delete")
            return 1
        else:
            return (remove_elt(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == "delete":
        if len(sys.argv) <=2:
            print("Error: you need to specify the name of the list you want to delete")
            return 1
        else:
            return (delete(sys.argv[2]))
    elif sys.argv[1] == "view_category":
        if len(sys.argv) <= 2:
            print("Error: you need to specify a category")
            return 1
        else:
            return view_cat(sys.argv[2])
    elif sys.argv[1] == "view_categories":
        return (view_cat_names())
    elif sys.argv[1] == "view_everything":
        return (view_all())
    else:
        print("Error: unknown command")
        welcome()
        return 1

sys.exit(main())
