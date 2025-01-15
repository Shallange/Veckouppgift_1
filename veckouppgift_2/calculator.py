#5 Miniräknare
def calculator_tool(n1,n2,n3):
    sum_of_num = n1 + n2 + n3

    #Finding biggest number
    if n1 > n2 and n1 > n3:
        largest_num = n1
    elif n2 > n1 and n2 > n3:
        largest_num = n2
    else:
        largest_num = n3
    
    #Check if all numbers are euqual -> returns bool
    all_num_is_equal = n1 == n2 == n3

    #Check if 2 numbers are equal -> return Bool
    two_num_is_equal = n1 == n2 or n1 == n3 or n2 == n3
 
    #Find middle number
    if n1!= n2 and n1 != n3 and n2 != n3:
        numbers = [n1,n2,n3]
        numbers.sort()
        middle = numbers[1]
    else:
        middle = None
    
    return sum_of_num, largest_num, all_num_is_equal,two_num_is_equal, middle


def format_print_result(n1,n2,n3, largest_num, all_equal, two_equal, middle):
    results = f"""
    T1 = {n1}  |  T2 = {n2}  |  T3 = {n3}  |  Störst = {largest_num}  |  Två lika? = {two_equal} |  Tre lika? = {all_equal} |  Mellerst? = {middle}
    """
    return results


#user input
num1 = int(input("skriv första talet: "))
num2 = int(input("skriv andra talet: "))
num3 = int(input("skriv tredje talet: "))


sum_of_num, largest_num, all_num_is_equal,two_num_is_equal, middle =  calculator_tool(num1, num2, num3)
print(format_print_result(num1, num2, num3, largest_num, all_num_is_equal, two_num_is_equal, middle))