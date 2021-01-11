import information
import random
import matplotlib
import matplotlib.pyplot as plt
#cycles of model
cm = int(input("Enter a number of cycles:\n"))

points_for_scheme = [] #salary in each year
list_of_years = []#for y in scheme 
stack_years = []#years where you are bankrot 
i= 0 #to show salary in each year 
stack = 0 # how many stack years we have  
#marks of year 
mark_1 = "*"
mark_2 = "**"
mark_3 = "***"
#year to start 
year = int(input("Enter your start year (2019 for example):"))
 
salary_of_man = int(input("Enter your salary:"))
save_of_salaty_of_man = salary_of_man #save to calculate the result in next year
if salary_of_man >= 100000:
	print("You are rich")
while (cm!=0):
    cm=cm-1
    year=year + 1
    list_of_years.append(year)
    i = i+1
    #minimum salary to live in another country
    minimal_value_to_live = random.randint(100,134)
    object_1 = random.randint(100,234)
    object_2 = random.randint(100,450)
    object_3 = random.randint(100,560)
    object_4 = random.randint(100,1000)
    result_of_year = salary_of_man-object_1-object_2-object_3-object_4
    salary_of_man = save_of_salaty_of_man
    points_for_scheme.append(result_of_year)
    
    if result_of_year <= minimal_value_to_live:
        print("stack year")
        stack_years.append(year)
    else:
        pass
        
    if result_of_year>= 1000:
        print(year)
        print(mark_3)
    elif result_of_year <= 1000:
        print(year)
        print(mark_2)
    elif result_of_year<= 500:
        print(year)
        print(mark_1)


    print(points_for_scheme)  
    print("______________________________") 

def stack_years_graphic():
    plt.title("Graphic of stack years ")
    plt.xlabel("salary")
    plt.ylabel("years")
    plt.grid()
    x=list_of_years
    y=stack_years
    plt.plot(x,y)
    plt.show


def graphic():
    plt.title("Graphic of result ")
    plt.xlabel("salary after buying common products")
    plt.ylabel("years")
    plt.grid()      # to make grid in graphic
    x = list_of_years
    y = points_for_scheme
    plt.plot(x,y)  # make a graphic
    plt.show()

#condition for stack years
for stack_year in stack_years:
    if stack_year >= 1:
        stack = stack + 1

if stack >= 5:
    # if we have  5 stack years ,we draw grapthic
    stack_years_graphic()

#line to read command in terminal
def command_line():
    command_in_terminal = input("Enter command")
    if command_in_terminal == "result":
        graphic()
        command_line()
    elif command_in_terminal == "stack":
        stack_years_graphic()
        command_line()

    else:
        command_line()
        
command_line()


