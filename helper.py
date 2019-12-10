#!/usr/bin/env python3
##########
# HELPER #
##########

# The purpose of this script is to help me to organize my life, deal with my autism, adhd, etc.


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
'''

'''
Lists representation :
- one list <-> one line
- one list :
  noun ; category ; elt1 $ etlt2 $ elt3 ...
'''

def read_lists():
    '''Returns the data for lists'''
    data = read_file("data_lists.txt")
    result = []
    for line in data :
        line = line.strip()
        if line == "" :
            continue
        line = line.split(";")
        result.append((line[0], line[1], line[2].split("$")))
    return result

def write_list(data):
    '''Writes the new list (stored in data) in the file'''
    f = open("data_lists.txt", "a")
    f.write(data[0] + ";" + data[1] + ";" + "$".join(data[2]) + "\n")
    f.close()

def print_list(l):
    '''Prints a list (pretty-printer)'''
    name = l[0]
    category = l[1]
    content = l[2]
    print("\x1b[31m\x1b[1mList {}:\x1b[0m".format(name))
    print("Category : {}".format(category))
    for item in content :
        print("- {}".format(item))

## Operators
# How to ask for a list l
def view(l):
    '''Views a list'''
    data = read_lists()
    for list in data :
        if list[0] == l :
            print_list(list)
            #print(list[2]) ##todo : prettyprinter
            return 0
    print("Error : list not found")
    return 1

# How to add a list l
def add(name, cat, list_elts):
    '''Adds a list'''
    data = read_lists()
    for list in data :
        if list[0] == name :
            print("Error : a list with this name already exists")
            return 1
    write_list([name, cat, list_elts])
    print("You created the list", name)
    return 0


# Main function

def main():
    if len(sys.argv) <= 1 :
        print("Error : need command")
        return 1
    elif sys.argv[1] == "view" :
        if len(sys.argv) <= 2 :
            print("Error : you need to specify which list to view")
            return 1
        else :
            return view(sys.argv[2])
    elif sys.argv[1] == "add" :
        if len(sys.argv) <= 2 :
            print("Error : you need to specify the name of the list you want to add")
            return 1
        elif len(sys.argv) <= 3 :
            print("Error : you need to specify the category of the list you want to add")
            return 1
        elif len(sys.argv) <= 4 :
            print("Error : you are trying to add an empty list")
            return 1
        else :
            return add(sys.argv[2], sys.argv[3], sys.argv[4:])
    else :
        print("Error : unknown command")
        return 1

sys.exit(main())
