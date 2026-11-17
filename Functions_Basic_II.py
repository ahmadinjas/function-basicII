my_list = []

def Countdown (num): 
    for x in range (num, -1, -1):
        my_list.append(x)

    return my_list 

print(Countdown(5))


#   2 
def Print_and_Return(print_return):
    print(print_return[0])

    return  print_return [1] 

print(Print_and_Return([1,2]))

#  3 

def First_Length(my_list) : 
    sum = my_list[0] + len(my_list)

    return sum 

print(First_Length([1,2,3,4,5]))

#  4 

list_my = [5,2,3,2,1,4]
def Values_Second(my_li) : 
    if len(my_li) < 2 : 
        return False
     
    new_list = [] 

    for value in my_li:
        if value > my_li [1] : 
          new_list.append(value) 

    print(len(new_list))
    return new_list

print(Values_Second(list_my)) 

#  5 


def Length_Value (a ,  b) : 
    vv=[]
    for i in range(a): 
        vv.append(b)
    
    return vv 

print(Length_Value(4 , 7 ))
print(Length_Value(6,2))

#   5 

def lenght (size , vul):
    return [vul]*size

print(lenght(2,3))




