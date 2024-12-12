                            #NO.1 (i)

def circle_area (radius):

    pie = 3.14
    area_of_the_circle = pie * (radius**2)
    return area_of_the_circle 

radius = 4
area = circle_area(radius)

#printing the area of the circle
print(f"\nThe area of the circle is: {area} ",'\n\n')
circle_area(radius)



                           #NO.1(ii)
def sum_of_odd_numbers ():
    integers = [4,7,2,9,12,15]
    sum = 0 #initializing the sum

    #using a for loop
    for number in integers:
        if number %2 and number !=0:
            sum+=number

    print(f"\nThe sum of all odd numbers is: {sum}",'\n\n')#printing the result
sum_of_odd_numbers() #calling the function


                           #NO.1(iii)
def number_operations(number_one, number_two):
    # computing the operations
    sum = number_one + number_two
    difference = number_two - number_one
    product = number_one * number_two

#using if, else to compute the quotient
    if number_two != 0:
        quotient = number_two / number_one
    else:
        print("undefined")
    return sum, difference, product, quotient #returning the operations

#inputing numbers
number_one = int(input("\nEnter the first number:   "))
number_two = int(input("Enter the second number:    "))

sum, difference, product, quotient = number_operations(number_one, number_two)

print(f"\nThe sum of numbers is : {sum} ")
print(f"The difference of numbers is : {difference} ")
print(f"The product of numbers is : {product} ")
print(f"The quotient of numbers is : {quotient} ",'\n\n')


                 #NO.1(iv)

student_info = {'name':'Alice','age':20,'grade':'A'}

#updating the value of age to '26'

student_info['age'] = 26
print(f"\nThe updated dictionary is: {student_info}",'\n\n')

# adding a new key-value pair

student_info['city'] = 'Kampala'
print(f"\nThe updated dictionary with a new key-value pair is: {student_info}",'\n\n')




    
   