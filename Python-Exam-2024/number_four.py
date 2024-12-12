                               #NO.4(i)
##(a)

# define OOP(object oriented programming)
# Object-Oriented Programming (OOP) is a programming model that organizes software design
# around objects rather than functions.
#  They have priciples like objects, classes.


#significance in software development

# Object Oriented Programming allows developers to break down a complex system  into simpler, smaller, manageable,
#  reusable components or objects.Each object can be developed, tested, and maintained independently(on its own)


              
                     #(b)
# A class is a blueprint or template for creating objects in Object-Oriented Programming (OOP).
#  It defines the structure and behavior the objects created from the class will have.

#It is different to an object because;
# An object is an instance of a class and it holds actual values for those attributes and can use the methods.


                                     #NO.4(ii)


def count_occurences(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words: #using a for loop
        word = word.strip(",.!?;:") # excluding punctuations while counting the words
        word_count[word] = word_count.get(word, 0) + 1 # sums up or counts the total number of each word in a sentence

    return word_count

sentence = input("\nEnter the sentence: ") #using a keyboard to input the sentence
print(count_occurences(sentence))

                                
                                 #NO.4(iii)

def sum_of_numbers (a,b):
    sum = a+b
    return sum
result = sum_of_numbers(3,4) #passing in attributes.
print(f"\nThe sum of the numbers is: {result}",'\n\n')



                                #NO.4(iv)
class Car:
    def __init__(self,brand,name,color): #passing in parameters
        self.brand = brand
        self.name = name
        self.color = color
#creating an object or instance for the class.
car1 = Car(brand="Toyota", name="Toyota-benze", color="black")
print(f"\nThe car brand is : {car1.brand}",'\n')
print(f"The car name is : {car1.name}",'\n')
print(f"The car color is : {car1.color}",'\n')


                             #NO.4 (v)


#adding a method called start_engine to the car class.


class Car:
    def __init__(self,brand,name,color): #passing in parameters
        self.brand = brand
        self.name = name
        self.color = color

     # Method to start the engine 
    def start_engine(self):
        print(f"The engine of the car has started.",'\n\n')

#creating the instance for the class
car1 = Car(brand="Toyota", name="Toyota-benze", color="black")

#calling the method
car1.start_engine()