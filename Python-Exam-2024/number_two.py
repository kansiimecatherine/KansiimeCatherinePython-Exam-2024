                          #NO.2(i)

# entering the details from a keyboard using the input() function

def student_details ():

    student_name = input("Enter the student name:  ")
    student_number = input("Enter the student number:  ")
    programming = int(input("Enter the programming marks:  "))
    data_science = int(input("Enter the data science marks:  "))
    computer_applications = int(input("Enter the computer applications marks:  "))

    average_mark = (programming + data_science + computer_applications) /3
    print(f"\nThe average mark is : {average_mark : .3f}",'\n\n')

student_details()

                                #NO.2(ii)

def calculate_mpg():

    # Inputing miles driven and gallons using a keyboard
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons of gas used: "))
    
    #miles-per gallon formula
    mpg = miles_driven / gallons_used
    print(f"The car's miles per gallon (MPG) is: {mpg}")
   
calculate_mpg() 

                               #N0.2(iii)

def not_divisible_by_two ():

    for number in range(1,101):
        if number %2 and number !=0: # Computing the not divisible numbers.
            print(number)
            
not_divisible_by_two()

