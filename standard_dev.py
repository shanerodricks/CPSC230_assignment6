import math

pos_int = int(input("Enter a positive integer: "))
list = []

def print_sorted(int_list):
    #takes a list of integers and prints them sorted_grades
    print(list.sort())


def compute_mean(int_list):
    #takes list of integers and prints mean
    count = 0
    var = 0
    sum = 0
    for num in list:
         sum = sum + num
         var += 1
    mean = sum / var
    return mean

def compute_variance(int_list, a_mean):
    #take integer list and returns variance
    summation = 0
    for var in list:
        variance = ((var - a_mean) ** 2)
        summation += 1
    return variance

def compute_standard_dev(int_list):
    #take variance input and return standard deviation

    standard_dev = math.sqrt(variance)
    return standard_dev

#main
while pos_int >= 0:
    pos_int = int(input("Enter a positive integer: "))
    list.append(pos_int)

else:
    print_sorted(list)
    mean = compute_mean(list)
    print("The mean is: ", mean)
    print("The variance is: ",  compute_variance(list, mean))
    variance = compute_variance(list, mean)
    print("The standard deviation is: ", compute_standard_dev(variance))
    standard_dev = compute_standard_dev(list)
    #compute mean and standard deviation, then print
