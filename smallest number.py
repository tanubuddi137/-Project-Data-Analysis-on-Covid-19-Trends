# write a program on the command line that takes a list of numbers and returns the smallest number in the list

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
