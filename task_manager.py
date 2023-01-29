
# --------------- Create functions for each option-----------------
# Function to register user
def reg_user():
 
 # Add a while true statement to get a new username unless the user already exists.
    while True:
        new_username = input("New Username: ")
        if new_username in username_password.keys():
            print("This user already exists. Please enter a new username.")
        else:
            break
        
 # - Request input of a new username and password
    new_password = input("New Password: ")

# - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
           
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


##################################################################################################################################
# Function to add task
def add_task():

    # - Prompt a user for the following: 
    #     - A username of the person whom the task is assigned to,
    #     - A title of a task,
    #     - A description of the task and 
    #     - the due date of the task.
    task_username = input("Name of person assigned to task: ")
    
 # Add a while loop to make sure it keeps asking for a user that has already been registered before it breaks.
    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")

        if task_username in username_password.keys():
            break     
    
 # while loop to get information. If there is a value error such as the wrong date format, it will bring the user back to the beginning 
 # of the loop to re-enter the data correctly.
    while True:
        try:
            task_title = input("Title of Task: ")
            task_description = input("Description of Task: ")
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


        # - Then get the current date.
    curr_date = date.today()
        # - Add the data to the file task.txt and
        # - As a default, all added tasks are false/ incomplete
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


##################################################################################################################################
# Function to view all tasks
def view_all():

    '''In this block you will put code so that the program will read the task from task.txt file and
     print to the console in the format of Output 2 presented in the task pdf (i.e. include spacing and labelling) 
     You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
            

    print("-----------------------------------")
    for t in task_list:
        disp_str = f"Task no: " + str(task_list.index(t)) + "\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        print("-----------------------------------")




##################################################################################################################################
# Function to view your own tasks
def view_mine():

    '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the task pdf (i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in the pdf '''
            

    print("-----------------------------------")
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task no: " + str(task_list.index(t)) + "\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Task completed:  {t['completed']}\n"
            print(disp_str)
            print("-----------------------------------")
    
       
    user_sel = int(input("Please enter a task number or -1 for main menu: "))
    
    if user_sel == -1:
        main_menu()
    
    else:
        if task_list[user_sel]['completed'] == True:
            print("This task is complete")
            main_menu()
        
        else:
            choice = input("How do you want to edit the task? Enter: completed or edit: ").lower()
            if choice == "completed":
                task_list[user_sel]['completed'] = True
                print("Task changed to completed")
            
            elif choice == "edit":
                reassign_date = input("Reassign task or change due date? Enter: reassign or date: ").lower()
                
                if reassign_date == 'reassign':
                    print(username_password.keys())
                    new_user = input("Who do you want to reassign to?: ").lower()
                    task_list[user_sel]['username'] = new_user   
                
                elif reassign_date == 'date':
                    new_date = input("What is the new date (YYYY-MM-DD)?: ")     #.strftime(DATETIME_STRING_FORMAT)
                    task_list[user_sel]['due_date'] = new_date

##################################################################################################################################
# Function to generate reports

def gen_report():
    total_tasks = len(task_list)
    
    task_complete = 0
    for i in range(total_tasks):
        if task_list[i]['completed'] == True:       # needs to be int not dictionary
            task_complete += 1
                
    task_overdue = 0
    for i in range(total_tasks):
        if task_list[i]['due_date'] < datetime.today() and task_list[i]['completed'] == False:
            task_overdue += 1
             
    
    with open("task_overview.txt", "w") as overview:
        overview.write("The total number of tasks generated and tracked using task manager is: " + str(total_tasks) + "\n")
        overview.write("The total number of completed tasks: " + str(task_complete) + "\n")
        overview.write("The total number of incompleted tasks: " + str(total_tasks - task_complete) + "\n")
        overview.write("The total number of incompleted and overdue tasks: " + str(task_overdue) + "\n")
        overview.write("The percentage of incomplete tasks: " + str(round((total_tasks - task_complete)/total_tasks*100)) + "%\n")
        overview.write("The percentage of overdue and incomplete tasks: " + str(round((task_overdue/total_tasks)*100)) + "%\n")
    
    
    print("This function prints a general report and a user specific report.")
    print(username_password.keys())
    which_user = input("Which user would you like?: ")
    
    user_tasks = 0
    user_complete = 0
    user_overdue = 0
    
    for t in range(len(task_list)):
        if task_list[t]['username'] == which_user:
            user_tasks += 1
        
        if task_list[t]['username'] == which_user and task_list[t]['completed'] == True:
            user_complete += 1
        
        if task_list[t]['username'] == which_user:
            if task_list[t]['due_date'] < datetime.today() and task_list[t]['completed'] == False:
                user_overdue += 1     
            
    
        
    with open("user_overview.txt", "w") as user_o:
        user_o.write("This overview is for " + which_user + "\n")
        user_o.write("The total number of tasks: " + str(user_tasks) + "\n")
        user_o.write("The tasks assigned: " + str(round((user_tasks/total_tasks)*100)) + "%\n")
        user_o.write("The tasks assigned that are completed: " + str(round((task_complete)/user_tasks*100)) + "%\n")
        user_o.write("The remaining tasks to be completed: " + str(round((user_tasks-task_complete)/user_tasks*100)) + "%\n")
        user_o.write("The overdue assignments: " + str(round((user_tasks-user_overdue)/user_tasks*100)) + "%\n")
    
    print("\nReports available now.")

 # Additional write task to keep the edits made
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
 
#################################################################################################################
# Function to display statistics
def dis_stat():

    print("------------------------------------------------")
    print("---------------Task_overview--------------------")
    contents = ""
    with open('task_overview.txt', 'r+', encoding='utf-8-sig') as f:
    
        for line in f:
                contents = contents + line
        print(contents)
    
    print("------------------------------------------------")
    print("---------------User_overview--------------------")
    contents_user = ""
    with open('user_overview.txt', 'r+', encoding='utf-8-sig') as f:
    
        for line in f:
                contents_user = contents_user + line
        print(contents_user)
    
#########################################################################
# Function that calls the main menu
        
def main_menu():
    while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
        print()
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate report
        ds - Display statistics
        e - Exit
        : ''').lower()

        if menu == 'r':
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm': 
            view_mine()
        elif menu == 'gr':
            gen_report()
        elif menu == 'ds':
            dis_stat()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

##############################################################################################################################

# Note use the following username and password to access the admin rights 
# username: admin
# password: password
#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
     
###################################################################################
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

##################################################################       
# Function to call for task

main_menu()
