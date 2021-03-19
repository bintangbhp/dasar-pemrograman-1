# *******************************************************************
# lab06.py
#
# Sorting a list of numbers using the Selection-Sort Algorithm
# *******************************************************************

##
# The selectionSort function sorts a list using the selection sort algorithm.
#
# @param values: the list to sort
# @return the total number of swaps
#
# calls the function minimumPosition
#

def selectionSort(values):
    swap = 0
    for sort in range (len(values)):
        index = minimumPosition(values, sort)
        if index != sort:
            values[index], values[sort] = values[sort], values[index]
            swap += 1
    return swap

##
# Finds the smallest element in a tail range of the list.
# @param values: the input list
# @param start: the first position in values to compare
# @return the position of the smallest element in the
# range values[start] . . . values[len(values) - 1]
#

def minimumPosition(values, start):
    indexMin = start
    for i in range(indexMin + 1 , len(values)):
        if values[indexMin] > values[i]:
            indexMin = i
    return indexMin

##
# Demonstrates the selection sort algorithm by sorting a
# list of numbers given by the user.
def main():
    input_string = input("Type a sequence of numbers (example: 3,100,-5,3): \n")
    # Mengubah input menjadi list berisi integer
    input_list = []
    for list_inp in input_string.split(','):
        list_inp = int(list_inp)
        input_list.append(list_inp)
    
    # Melakukan sorting input
    number_list = []
    for sorted_list in input_string.split(','):
        sorted_list = int(sorted_list)
        number_list.append(sorted_list)
    swap = selectionSort(number_list)

    print(f"Input list:\n {input_list}")
    print(f"Sorted list:\n {number_list}")
    print('Number of swaps in Selection-Sort:', swap)

main()