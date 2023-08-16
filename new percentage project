#Project completion total return by active projects

#Number of line items in each of the projects active
project_items = [0, 0, 0]
#Name of the active projects
project_names = ["KUS ECU OTA", "KCA ECU OTA", "KCA FOD"]
#KUS ECU OTA items as they are 8/15/23
kuseo_project_totals = [100, 100, 90, 100, 100, 50, 90, 100, 98, 80, 100, 100, 0, 70, 10, 5, 5, 20, 0, 90, 30, 0, 0, 0, 0, 0]
#KCA ECU OTA items as they are 8/15/23
kcaeo_project_totals = [90, 100, 100]
#KCA FOD items as they are 8/15/23
kcafd_project_totals = [90, 90, 50, 0, 90, 90, 90, 40, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Making the project line items equal to the number of items in project total for all projects.
project_items[0] = len(kuseo_project_totals)
project_items[1] = len(kcaeo_project_totals)
project_items[2] = len(kcafd_project_totals)

#Adding new items to the project line items and/or averaging out the percentage of project complete
def add_to_kuseo_totals():
    #print the current line item total to the user
    print("You currently have " + str(project_items[0]) + " item lines in " + project_names[0])
    #asking user for new line items to be added.
    user_input = input("Do have totals to add?")
    #If there are new line items needed to be added, getting the total of each
    if user_input == "Y".lower():
        #getting the new total for the new line item
        new_total = input("What is the total?")
        #adding the new total to the totals in project list as integar
        kuseo_project_totals.append(int(new_total))
        #running the function again to loop the check for new items
        add_to_kuseo_totals()
    #if there are no new items from user, averaging and returning completion percentage   
    elif user_input == "N".lower():
        #for loop for each value in the project total list
        for i in kuseo_project_totals:
            #adding the project total to project items total
            project_items[0] += i
        #averaging the project total value by the amount of items in the list
        project_items[0] = project_items[0] / len(kuseo_project_totals) 
        #printing the completion percentage to the user as rounded value
        print(project_names[0] + " project completion is: " + str(round(project_items[0])))
        add_to_kcaeo_totals()
#Adding new items to the project line items and/or averaging out the percentage of project complete
def add_to_kcafd_totals():
    #print the current line item total to the user
    print("You currently have " + str(project_items[2]) + " item lines in " + project_names[2])
    #asking user for new line items to be added.
    user_input = input("Do have totals to add?")
    #If there are new line items needed to be added, getting the total of each
    if user_input == "Y".lower():
        #getting the new total for the new line item
        new_total = input("What is the total?")
        #adding the new total to the totals in project list as integar
        kcafd_project_totals.append(int(new_total))
        #running the function again to loop the check for new items
        add_to_kcafd_totals()
    #if there are no new items from user, averaging and returning completion percentage   
    elif user_input == "N".lower():
        #for loop for each value in the project total list
        for i in kcafd_project_totals:
            #adding the project total to project items total
            project_items[2] += i
        #averaging the project total value by the amount of items in the list
        project_items[2] = project_items[2] / len(kcafd_project_totals) 
        #printing the completion percentage to the user as rounded value
        print(project_names[2] + " project completion is: " + str(round(project_items[2])))
#Adding new items to the project line items and/or averaging out the percentage of project complete
def add_to_kcaeo_totals():
    #print the current line item total to the user
    print("You currently have " + str(project_items[1]) + " item lines in " + project_names[1])
    #asking user for new line items to be added.
    user_input = input("Do have totals to add?")
    #If there are new line items needed to be added, getting the total of each
    if user_input == "Y".lower():
        #getting the new total for the new line item
        new_total = input("What is the total?")
        #adding the new total to the totals in project list as integar
        kcaeo_project_totals.append(int(new_total))
        #running the function again to loop the check for new items
        add_to_kcaeo_totals()
    #if there are no new items from user, averaging and returning completion percentage   
    elif user_input == "N".lower():
        #for loop for each value in the project total list
        for i in kcaeo_project_totals:
            #adding the project total to project items total
            project_items[1] += i
        #averaging the project total value by the amount of items in the list
        project_items[1] = project_items[1] / len(kcaeo_project_totals) 
        #printing the completion percentage to the user as rounded value
        print(project_names[1] + " project completion is: " + str(round(project_items[1])))
        add_to_kcafd_totals()
#running the functions
add_to_kuseo_totals()

