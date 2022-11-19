# Import library
import datetime

# Login Section
passwords = dict()

# Open user.txt for reading
with open('user.txt', 'r') as file_text:                   
    for line in file_text:                                 
        user = line.split(',')[0].strip()           
        password = line.split(',')[1].strip()       
        passwords[user] = password                  

# Check username and password if its correct
while True:                                         
    username = input('Enter your username: ')       
    password = input('Enter your password: ')       

    if username in passwords:                       
        if passwords[username] == password:         
            break                                  
        else:                                       
            print('Wrong password!\n')              
    else:                                           
        print('Username not found!\n')              



while True:
    
    # Check password  and username to see which menu to print out.
    if username == 'admin':                                             

        # Admin menu
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()
    else:                                                              

        #User menu
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

    # Register new user option
    if menu == 'r':

        # User must enter a new username:
        new_username = input('Enter new username: ')

        # User must enter a new password:
        new_password = input('Enter password: ')

        # User must confirm the new password:
        confirm_password = input('Re-enter password: ')                         
        
        if username == 'admin':

            # When password confirmed add username and password to user.txt
            if new_password == confirm_password:                                     
                with open('user.txt', 'a') as file_text:                       
                    file_text.write(f'{new_username}, {new_password}\n')                
            else:

                # If password does'nt match it will print the following:
                print('Passwords do not match\n')                       
        else:                                                       
            print('Only admin can register a new user\n')               

    # Adding a task option
    elif menu == 'a':                                                                       
        task_user = input('Enter the username of the person to assign task to: ')            
        title = input('Enter title of task: ')                                              
        description = input('Enter description of task: ')                                  
        due_date = input('Enter due date of task: ')                                         
        curr_date = datetime.date.today().strftime('%d %b %Y')                               
        completed = 'No'                                                                    

        # Write to tasks.txt
        with open('tasks.txt', 'a') as file_text:                                                          
            file_text.write(f'{task_user}, {title}, {description}, {due_date}, {curr_date}, {completed}\n')   

    # View all tasks option
    elif menu == 'va':                                                  
        with open('tasks.txt', 'r') as file_text:                              
                for lists in file_text:
                    lists = lists.split(", ")
                    task_user = lists[0]
                    title = lists[1]
                    description = lists[2]
                    due_date = lists[3]
                    curr_date = lists[4]
                    

                    # Print the following tasks entered
                    print(f"""
                Task username  {task_user},
                Task title     {title},
                Task description  {description},
                Task due date  {due_date},
                Current date   {curr_date},
                """)                                                 

    # View my tasks option
    elif menu == 'vm':

        # Open task file to see content of all tasks entered
        with open('tasks.txt', 'r') as file_text:                              
           for lists in file_text:
                    if username in lists:
                        lists = lists.split(", ")
                        task_user = lists[0]
                        title = lists[1]
                        description = lists[2]
                        due_date = lists[3]
                        curr_date = lists[4]
                        
                        
                        # Print the following tasks entered
                        print(f"""
                    Task username  {task_user},
                    Task title     {title},
                    Task description {description},
                    Task due date  {due_date}
                    Current date   {curr_date},
                    """)

    # Display statistics option       
    elif menu == 'ds':

        # Open task.txt to read number of task entered
        with open('tasks.txt', 'r') as file_text:                              
            print('totalTasks =', len(file_text.readlines()))

        # Open user.txt to read number of users entered
        with open('user.txt', 'r') as file_text:                               
            print('totalUsers =', len(file_text.readlines()))                  
        print()
        
    # Exit option
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        
        # Else statement takes us back to user menu if user did not choose correctly from the menu
        print("You have made a wrong choice, Please Try again")
