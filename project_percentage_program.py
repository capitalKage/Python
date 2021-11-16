#list of milestones entered by user
milestone_name_list = []
#list of percentages entered by user
pecentage_list = []
#joined list of milestones and percentages

#boolean checks for while loops
percentages_bool = False
#average of all project percentages entered by the user
averaged_total = 0

print("""
Welcome to the project average finder prototype.
First you will enter your milestones when complete please type DONE.
You can quit at any time by typing STOP
Once you have entered all percentages, please type DONE
The program will compile your list and milestones to a text file.
""")

#function for collecting all the milestones in the program
def milestone_collection():
    milestone_bool = True
    while milestone_bool == True:
        request_input = input("Please enter your milestones \n>")
        if request_input == "DONE":
            milestone_bool = False
            pecentage_collection()
        elif request_input == "STOP":
            print("Program is shutting down")
            break
        else:
            milestone_name_list.append(request_input)

#Function for collecting all the percentages in the program
def pecentage_collection():
    percentages_bool = True
    while percentages_bool == True:
        request_input = input("Please enter your percentages \n>")
        if request_input == "DONE":
            percentages_bool = False
            finished(0,len(pecentage_list))
        elif request_input == "STOP":
            print("Program is shutting down")
            break
        else:
            converted = int(request_input)
            pecentage_list.append(converted)

#Calculation of the average number function
def finished(total, entry_number):
    print(pecentage_list)
    for i in pecentage_list:
        print(i)
        total += i
    print(total)
    print(entry_number)
    averaged_total = total / entry_number
    write_to_file()
    with open("Average.txt", 'a') as average_file:
        average_file.write('Your project completion average is: ' + str(averaged_total))

#function to write to text file
def write_to_file():
    compiled_list = [list(a) for a in zip(milestone_name_list, pecentage_list)]
    with open("Average.txt", "a") as average_file:
        for i in milestone_name_list:
            average_file.writelines(i + '\n')
                

milestone_collection()








