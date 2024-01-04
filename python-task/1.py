
#Extend nested list by adding the sublist
def one():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    list1[2][1][2].extend(sub_list)
    print(list1)
    #list1[2][1][2].append(sub_list)            -->op:['a', 'b', ['c', ['d', 'e', ['f', 'g', ['h', 'i', 'j']], 'k'], 'l'], 'm', 'n']
#one()

#convert two list to dict
def two():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    result=dict(zip(keys,values))
    print(result)
#two()

# Delete a list of keys from a dictionary
def three():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    keys=["name","salary"]
    for i in keys:
        sample_dict.pop(i)
    print(sample_dict)
# three()

#Rename key of a dictionary
def four():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    sample_dict["location"]=sample_dict.pop('city')
    print(sample_dict)
#four()

#Get the key of a minimum value from the following dictionary
def five():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
        }
    print(min(sample_dict))
# five()

def six():
    file = 'sample.txt'
    input_str = input('Enter a word: ')
    
    #checks the given input in the file
    def check_str(file, input_str):
        with open(file, 'r') as file:
            content = file.read().lower()
            return input_str.strip('.,!?()[]{}:;"\'').lower() in content  

    #count of each word in the file
    def count_words(file):
        with open(file, 'r') as file:
            content = file.read().lower()
            words = content.split()
            word_counts = {}
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            return word_counts
        
    #count of total word
    def total_word_count(word_counts):
        return sum(word_counts.values())

    present = check_str(file, input_str)
    print(f'The word "{input_str}" is in the file: {present}')
    
    word_counts = count_words(file)
    print(f'Total count of words: {total_word_count(word_counts)}')
    
    for word, count in word_counts.items():
        print(f'"{word}": {count} times')

#six()
import time
import pandas as pd

def seven():
    # Decorator to read dataset
    def read_dataset_and_measure_time(func):
        def wrapper():
            #executon time calculation
            start = time.time()
            #ds reading 
            df = pd.read_csv("salaries.csv")
            df = pd.DataFrame(df)
            func(df)
            end = time.time()
            print(f'Execution Time: {end - start}')
        return wrapper

    #iterrows method
    @read_dataset_and_measure_time
    def iterrows_check(df):
        count=0
        for index, row in df.iterrows():
            print(row['salary'])
            count += 1
            if count == 10:
                break
            

    
    #itertuples method
    @read_dataset_and_measure_time
    def itertuples_check(df):
        count=0
        for row in df.itertuples():
            print(row)
            count += 1
            if count == 10:
                break

            
    #apply method         
    @read_dataset_and_measure_time      
    def apply_check(df): 
        #based on this condition return the salary range       
        def salary_ran(salary):
            if  salary>50000:
                return "Low"
            elif salary>75000:
                return "Average"
            else:
                return "High"
        new=df['salary'].apply(salary_ran)
        print(new.head(3))
        print(new.tail(3))
     
    #map method   
    @read_dataset_and_measure_time 
    def map_check(df):
        #mapping based on work_year column
        mappings = {
        2022: 'one',
        2023: 'two'
        }
        df['yr_exp'] = df['work_year'].map(mappings)
        print(f"Dataframe after Mapping:{df.head(5)} ")
        
    iterrows_check()
    itertuples_check()
    apply_check()
    map_check()
# seven()    


from functools import reduce
def eight():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #Lambda with Map - Square each number
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("Squared Numbers:", squared_numbers)

    #Lambda with Filter - Filter even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even Numbers:", even_numbers)

    #Lambda with Reduce - Find the product of all numbers
    product = reduce(lambda x, y: x * y, numbers)
    print("Product of Numbers:", product)

    #Lambda with For Loop - Print each number multiplied by 2
    multiply_by_two = lambda x: x * 2
    for num in numbers:
        print(multiply_by_two(num), end=' ')
#eight()

def nine():
    #sort-->return none,change the original according to the given condition
    l=[10,6,3,2,9,8,1,5]
    l.sort()
    print(l)
    l.sort(reverse=True)
    print(l)
    
    #sorted-->return the sorted list without changing the original list
    l1=['aaa','e','bbbb','dd','ccccc']
    print(sorted(l1))
    print(sorted(l1,key=len))
          
# nine()

def ten1():
    class person():
        def __init__(self,name,age):
            print(f'Hello! {name},And your age is {age}')
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    values=person(user_name,user_age)
    
#ten1()

import math
def ten2():
    class Shape:
        def area(self):
            pass  
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return math.pi * self.radius**2

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height

    radius=int(input("enter radius:"))
    width=int(input("enter width:"))
    height=int(input("enter height:"))
    circle = Circle(radius)
    rectangle = Rectangle(width, height)

    print("Area of Circle:", circle.area())
    print("Area of Rectangle:", rectangle.area())
# ten2()


import random
def eleven():
    # Generate a random 5-digit number
    random_number = str(random.randint(10000, 99999))
    max_tries = 5
    for tries in range(max_tries):
        user_guess = input("Enter your 5-digit guess: ")

        # Check if the guess is correct
        if user_guess == random_number:
            print("You guessed the correct number!!")
            break
        
        # Check each digit and provide feedback
        feedback = ""
        for i in range(5):
            if user_guess[i] == random_number[i]:
                feedback += "C"
            elif user_guess[i] in random_number:
                feedback += "B"
            else:
                feedback += "A"
        print("Feedback:", feedback)
        
    # If the user couldn't guess the number in the allowed tries
    if user_guess != random_number:
        print("out of tries.The correct number was:", random_number)
# eleven()

def twelve():
    data = [{"roll_no": 1, "name": "John", "games": ["cricket", "football"],
        "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
       {"roll_no": 2, "name": "Mick", "games": ["football", "hockey"],
        "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
       {"roll_no": 3, "name": "June", "games": ["badminton", None],
        "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
       {"roll_no": 4, "name": "Adam", "games": ["soccer", "badminton"],
        "marks": {"maths": 86, "science": 91, "cs": 82}, "rank": 4},
       {"roll_no": 5, "name": "Robb", "games": ["cricket", None],
        "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
       {"roll_no": 6, "name": "Arya", "games": ["football", "hockey"],
        "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
       ]
    #1 Get the details of students studied ‘cs’
    df = list(filter(lambda row: 'cs' in row['marks'] , data))
    print(df)
    print('-----------------------------------------------------------------------------------')
    #2 Update student ranks and insert the key 'percentage'
    for item in data:
         if "maths" in item["marks"]:
            item["marks"]["maths"] *= 3
         if "science" in item["marks"]:
             item["marks"]["science"] *= 2
         for subject, mark in item["marks"].items():
            item["percentage"] = (mark / 600) * 100
    for student in data:
        student['games'] = [game for game in student["games"] if game is not None]
    print(data)
    print('-----------------------------------------------------------------------------------')
    #3
    data_df = pd.DataFrame(data)
    data_df["pre_rank"] = data_df["rank"]
    data_df['new_rank'] = data_df.groupby('percentage', sort=True).ngroup()+1
    data_df = data_df.sort_values(by="new_rank")
    data_df['change_in_ranks'] = data_df.apply([lambda row:1 if row['new_rank'] < row["pre_rank"]
                                               else -1 if row['new_rank'] > row["pre_rank"]
                                              else '-'] , axis=1)
    data_df_rank = data_df[['name', 'percentage' , 'pre_rank' , 'new_rank' , 'change_in_ranks']].copy()
    print(data_df_rank)
# twelve()

def thirteen():
    


