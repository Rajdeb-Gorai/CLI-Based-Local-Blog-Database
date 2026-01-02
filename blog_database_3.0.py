#===== LIBRARIES =================================================================================================
from datetime import datetime      #    library that pics time automatically


from colorama import init, Fore, Style      #   Library that helps to add color to the terminal


import os       #   fuction added to impliment to refresh the terminal


import re       #   function to enable searching more moduler and efficient and make the code more readable


import time        #    function added for countdown feature


init(autoreset=True)
#=================================================================================================================




#===== FUNCTIONS =================================================================================================
def add_new_blog(): #option 1
#````````````````````````````


    clear_screen()  #clears the screen


    #   basic inputs 
    print(Fore.LIGHTYELLOW_EX + "\nTITLE : ", end = "")
    title = input(Fore.LIGHTCYAN_EX + "")
    print(Fore.LIGHTYELLOW_EX + "\nAUTHOR : ", end = "")     
    author = input(Fore.LIGHTCYAN_EX + "")
    print("Co-Author : ", end = "")
    coauthor = input(Fore.LIGHTBLUE_EX + "")
    #````````````````````````````


    #   enables user to enter multiline post
    print(Fore.LIGHTYELLOW_EX + "\nBlog", Fore.BLUE + "(Type", Fore.LIGHTMAGENTA_EX + "'END'", Fore.BLUE + "in the next line to submit) : \n", Fore.RED + "  NOTE : you won't be able to edit when you hit to the next line!\n")
    lines = []
    while True:
        line = input(Fore.LIGHTCYAN_EX + "")
        if line.strip() == "END":
            break
        lines.append(line)
    blog = "\n  ".join(lines)
    #````````````````````````


    #   for automatic date pickup and autoformatiing into dd-mm-yy date format
    date = datetime.now().strftime("%d-%m-%y")
    #`````````````````````````````````````````


    #   creates the index of the new post
    with open("BD.txt", "r") as f:
        index = 0
        for each_line_in_dataset in f:
            if "INDEX : " in each_line_in_dataset:
                extracted_data = each_line_in_dataset.split(":")
                index = int(extracted_data[1].strip())
        new_index = index+1
    #``````````````````````


    #   process of saving the data into text file
    with open("BD.txt", "a") as f:
        f.write("\n-----------------------------\n")
        f.write("\n=== BLOG START ===\n")
        f.write("\nINDEX : "+ str(new_index) + "\n")
        f.write("\nTITLE : " + title + "\n")
        f.write("\nAUTHOR : " + author + "\n")
        f.write("\nCO-AUTHOR : " + coauthor + "\n")
        f.write("\nBLOG : \n\n" + blog + "\n")
        f.write("\nDATE : " + date + "\n")
        f.write("\n=== BLOG END ===\n")
    #``````````````````````````````````


    clear_screen()

    #   countdown for main menu
    for i in range(3, 0, -1):
        clear_screen()
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\nYour Blog has been Successfully Posted!\n")
        print(Fore.GREEN + Style.NORMAL + f"\n Redirecting to Main Menu in {i} seconds!")
        time.sleep(1)
    #````````````````
        


    clear_screen()  #   clears the screen
    #`````````````
#`````````````````




def view_all_post(): #option 2
#`````````````````````````````


    for i in range(4, 0, -1):   #   Instruction and Countdown
        clear_screen()
        print(Fore.RED + "Hit", Fore.LIGHTRED_EX + "ENTER", Fore.RED + "for Main Menu!")
        print(f"\nShowing Results in {i} Seconds!")
        time.sleep(1)
    #````````````````


    clear_screen()  #   clears the screen


    #   reads from the data and search
    with open("BD.txt", "r") as f:
        all_lines = f.readlines()
        #````````````````````````


        #   searching
        for lines in all_lines:
            if "=== BLOG START ===" in lines:
                print(Fore.LIGHTRED_EX + lines)
            elif "=== BLOG END ===" in lines:
                print(Fore.LIGHTRED_EX + lines)
            elif "AUTHOR : " in lines:
                print(Fore.LIGHTGREEN_EX + lines)
            elif "TITLE : " in lines:
                print(Fore.LIGHTBLUE_EX + lines)
            elif "CO-AUTHOR : " in lines:
                print(Fore.LIGHTMAGENTA_EX + lines)
            elif "DATE : " in lines:
                print(Fore.LIGHTYELLOW_EX + lines)
            else:
                print(lines.strip())
        #```````````````````````````


    #   taking input to go back to main menu
    while True:
        user_input = input("\n")
        if user_input == "":
            clear_screen()
            main_menu()
            break
#````````````````




def search_post_by_author(): #option 3
#`````````````````````````````````````


    for i in range(3, 0, -1):   #   Instruction and Countdown
        clear_screen()
        print(Fore.RED + "Hit", Fore.LIGHTRED_EX + "ENTER", Fore.RED + "for Main Menu!")
        print(f"\nShowing Results in {i} Seconds!")
        time.sleep(1)
    clear_screen()


    #   takes input from the user
    print(Fore.MAGENTA + "Enter Author Name : ", end = "")
    searched_blog_by_author = (input(Fore.CYAN + "").strip()).lower()
    clear_screen()
    #`````````````


    #   display searched option 
    print(Fore.YELLOW + "SHOWING RESULTS FOR", Fore.LIGHTGREEN_EX + searched_blog_by_author, "\n")
    #`````````````````````````````````````````````````````````````````````````````````````````````


    #   program for searching the required data
    found = False
    with open("BD.txt", "r") as f:
        all_lines = f.readlines()
        line_pointer = 0
        for line in all_lines:
            line_pointer += 1
            if re.search(rf"^AUTHOR\s*:\s*{searched_blog_by_author}$", line.strip(), re.IGNORECASE):
                found = True
                start = line_pointer
                while start>=0 and "=== BLOG START ===" not in all_lines[start]:
                    start -= 1
                while start<len(all_lines) and "=== BLOG END ===" not in all_lines[start]:
                    if "=== BLOG START ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "=== BLOG END ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTGREEN_EX + all_lines[start])
                    elif "TITLE : " in all_lines[start]:
                        print(Fore.LIGHTBLUE_EX + all_lines[start])
                    elif "CO-AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTMAGENTA_EX + all_lines[start])
                    elif "DATE : " in all_lines[start]:
                        print(Fore.LIGHTYELLOW_EX + all_lines[start])
                    else:
                        print(all_lines[start].strip())
                    start += 1
    if found == False:
        print("\nBlog not Found for this author!\n")
    #```````````````````````````````````````````````  


    #   taking input to go back to main menu
    while True:
        user_input = input("\n")
        if user_input == "":
            clear_screen()
            main_menu()
            break
#````````````````




def search_post_by_coauthor(): #option 4
#```````````````````````````````````````


    for i in range(3, 0, -1):   #   Instruction and Countdown
        clear_screen()
        print(Fore.RED + "Hit", Fore.LIGHTRED_EX + "ENTER", Fore.RED + "for Main Menu!")
        print(f"\nShowing Results in {i} Seconds!")
        time.sleep(1)

    clear_screen()


    #   takes input from the user
    print(Fore.MAGENTA + "Enter Co-Author Name : ", end = "")
    searched_blog_by_coauthor = input(Fore.CYAN + "").strip()
    clear_screen()
    print(Fore.YELLOW + "SHOWING RESULTS FOR", Fore.LIGHTGREEN_EX + searched_blog_by_coauthor, "\n")
    #``````````````````````````````````````````````````````````````


    #   opens and stores data into variable for further operation
    with open("BD.txt", "r") as f:
        lines = f.readlines()
    #````````````````````````


    #   program for searching the required data
    found = False
    with open("BD.txt", "r") as f:
        all_lines = f.readlines()
        line_pointer = 0
        for line in all_lines:
            line_pointer += 1
            if re.search(rf"^CO-AUTHOR\s*:\s*{searched_blog_by_coauthor}$", line.strip(), re.IGNORECASE):
                found = True
                start = line_pointer
                while start>=0 and "=== BLOG START ===" not in all_lines[start]:
                    start -= 1
                while start<len(all_lines) and "=== BLOG END ===" not in all_lines[start]:
                    if "=== BLOG START ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "=== BLOG END ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTGREEN_EX + all_lines[start])
                    elif "TITLE : " in all_lines[start]:
                        print(Fore.LIGHTBLUE_EX + all_lines[start])
                    elif "CO-AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTMAGENTA_EX + all_lines[start])
                    elif "DATE : " in all_lines[start]:
                        print(Fore.LIGHTYELLOW_EX + all_lines[start])
                    else:
                        print(all_lines[start].strip())
                    start += 1
    if found == False:
        print("\nBlog not Found for this co-author!\n")
    #```````````````````````````````````````````````


    #   taking input to go back to main menu
    while True:
        user_input = input("\n")
        if user_input == "":
            clear_screen()
            main_menu()
            break
    #````````````
#````````````````



                
def search_post_by_date(): #option 5
#```````````````````````````````````


    clear_screen()


    #   takes search input from the user
    print(Fore.GREEN + "Enter Date (dd-mm-yy format) : ", end = " ")
    searched_blog_by_date = input(Fore.LIGHTGREEN_EX + "").strip()
    #```````````````````````````````````````````````````````````````````````


    clear_screen()


    for i in range(3, 0, -1):
        print(Fore.RED + "Hit", Fore.LIGHTRED_EX + "ENTER", Fore.RED + "for Main Menu")
        print(Fore.GREEN + f"\nshowing results in {i} seconds!")
        time.sleep(1)
        clear_screen()


    #   opens and stores data into variable for further operation
    with open("BD.txt", "r") as f:
        lines = f.readlines()
    #````````````````````````


    print(Fore.GREEN + "Showing Results for Date :", Fore.LIGHTGREEN_EX + searched_blog_by_date, "\n")


    #   program for searching the required data
    found = False
    with open("BD.txt", "r") as f:
        all_lines = f.readlines()
        line_pointer = 0
        for line in all_lines:
            line_pointer += 1
            if re.search(rf"^DATE\s*:\s*{searched_blog_by_date}$", line.strip(), re.IGNORECASE):
                found = True
                start = line_pointer
                while start>=0 and "=== BLOG START ===" not in all_lines[start]:
                    start -= 1
                while start<len(all_lines) and "=== BLOG END ===" not in all_lines[start]:
                    if "=== BLOG START ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "=== BLOG END ===" in all_lines[start]:
                        print(Fore.LIGHTRED_EX + all_lines[start])
                    elif "AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTGREEN_EX + all_lines[start])
                    elif "TITLE : " in all_lines[start]:
                        print(Fore.LIGHTBLUE_EX + all_lines[start])
                    elif "CO-AUTHOR : " in all_lines[start]:
                        print(Fore.LIGHTMAGENTA_EX + all_lines[start])
                    elif "DATE : " in all_lines[start]:
                        print(Fore.LIGHTYELLOW_EX + all_lines[start])
                    else:
                        print(all_lines[start].strip())
                    start += 1
    if found == False:
        print("\nBlog not Found for given date!\n")


    #   taking input to go back to main menu
    while True:
        user = input("")
        if user == "":
            clear_screen()
            main_menu()
            break
    #````````````
#````````````````



  
def clear_screen():     #   function to clear screen
#``````````````````
    os.system('cls' if os.name == 'nt' else 'clear')
#```````````````````````````````````````````````````




def main_menu():    #   main CLI
#```````````````


    while True:


        #   program that tracks count of how much blogs has been posted till now and stores in a variable
        try:
            with open("BD.txt", "r") as f:
                total_number_of_blog = 0
                for each_line in f:
                    if "INDEX : " in each_line:
                        extracted_data = each_line.split(":")
                        total_number_of_blog = int(extracted_data[1].strip())
        
        except FileNotFoundError:
            total_number_of_blog = 0
            clear_screen()
            print(Fore.RED + Style.BRIGHT + "\nDisclaimer: BD.txt file is missing!")
            print(Fore.YELLOW + "Creating new BD.txt with header...\n")

            time.sleep(2)

            with open("BD.txt", "w") as f:
                f.write("=== BLOG DATABASE CREATED === DATE : " + datetime.now().strftime("%d-%m-%y") + "\n")

            for i in range(3, 0, -1):
                clear_screen()
                print(Fore.LIGHTGREEN_EX + f"New BD.txt created successfully! Redirecting in {i} seconds...")
                time.sleep(1)
        #   ``````````````````````````````````````````````````````````````


        #   CLI interface & selected option picker
        print(Fore.YELLOW + Style.BRIGHT + "\n/----------------------------------------\ \n|<<----=== SIMPLE BLOG DATABASE ===---->>|\n\----------------------------------------/")
        print(Fore.CYAN + Style.NORMAL + "Total Number of Blogs Posted :",Fore.GREEN + Style.NORMAL +  str(total_number_of_blog))
        print(Fore.MAGENTA + "Current Date :", Fore.LIGHTMAGENTA_EX + time.strftime("%d-%m-%y"))

        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "\n\n          Select Your Option")
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "\n   1. Add New Blog")
        print(Fore.GREEN + Style.NORMAL + "   2. View All Posts")
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "   3. Search Post by Author")
        print(Fore.MAGENTA + "   4. Search Post by Co-Author")
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "   5. Search Posts By date")
        print(Fore.RED + Style.BRIGHT + "   6. Exit")

        selected_option = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\nENTER OPTION : ")    


        #   try and except portin so that user does not enter another data type
        try:
            selected_option = int(selected_option)
        except ValueError:
            clear_screen()
            print(Fore.RED + "\nEnter a Valid Option!\n")
            continue
        #```````````````````````````````````


        #   function calls for selected option

        if selected_option == 1:        #   for option 1 [adding new post to the database]
            add_new_blog()


        elif selected_option == 2:      #   for option 2 [for displaying all posts]
            view_all_post()


        elif selected_option == 3:      #   for option 3 [for searhing all posts by Author name]
            search_post_by_author()


        elif selected_option == 4:
            search_post_by_coauthor()


        elif selected_option == 5:      #   for option 4 [for searhing all posts by Date]
            search_post_by_date()


        elif selected_option == 6:      #   for option 5 [for exiting the terminal]
            for i in range(3, 0, -1):
                clear_screen()
                print(Fore.LIGHTRED_EX + f"Closing the terminal in {i} seconds!...\nBye.....")
                time.sleep(1)
            clear_screen()
            break


        else:                           #   it works when user inputs invalid option
            clear_screen()
            print(Fore.RED + "\nEnter a valid Option!!\n")
        #````````````````````````````````````
    #````````````````````````````````````````
#=================================================================================================================





#===== USER INPUTS AND OUTPUTS ===================================================================================
#   main terminal flow for recurrent terminal until exit
clear_screen()


main_menu()
#=================================================================================================================