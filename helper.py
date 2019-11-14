#!/usr/bin/env python3
##########
# HELPER #
##########

# The purpose of this script is to help me to organize my life, deal with my autism, adhd, etc.


# Import modules
import sys

# Utils
def read_file(file):
    '''Returns the list of lines from the file'''
    f = open(file, "r")
    data = f.readlines()
    f.close()
    return data


# Lists

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

def write_lists(data):
    f = open("data_lists.txt", "w")
    for l in data :
        f.write(l[0] + ";" + l[1] + ";" + "$".join(l[2]) + "\n")
    f.close()

def print_list(l):
    name = l[0]
    category = l[1]
    content = l[2]
    print("\x1b[31m\x1b[1mList {}:\x1b[0m".format(name))
    print("Category : {}".format(category))
    for item in content :
        print("- {}".format(item))



def view(l):
    data = read_lists()
    for list in data :
        if list[0] == l :
            print_list(list)
            #print(list[2]) ##todo : prettyprinter
            return 0
    print("Error : list not found")
    return 1


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
    else :
        print("Error : unknown command")
        return 1

sys.exit(main())
