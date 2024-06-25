import functools
import sys

def run(input):
    numbers = []
    
    for string in input:
        string_length = len(string)
        first_number = None
        last_number = None
        for i in range(0, len(string)):
            if (first_number == None and string[i].isdigit()):
                first_number = string[i]
                
            if (last_number == None and string[string_length - 1 - i].isdigit()):
                last_number = string[string_length - 1 - i]
            
            if (first_number and last_number):
                numbers.append(int(first_number + last_number))
                break
    return functools.reduce(lambda a, b: a + b, numbers)

if __name__ == "__main__":
    print(sys.argv)
    f = open(sys.argv[1], "r")
    lines = f.read().split("\n")
    
    print(run(lines))
