main_menu_list = ["End Session","View Logs","Record Log","Edit Log",\
"Delete Log"]

log_location_list = ["London","Birmingham","Manchester","Southampton",\
"Edinburgh","Belfast","Newcastle"]
def location_listing():
    print("\nLocation List:")
    for location in log_location_list:
        print(f"-\t{location}")
        
log_goods_type_list = ["Electronics","Clothing","Sporting","Toys",\
"Mechanicals","Crafts","Houshold Goods","Physical Medias","Foods","Other"]
def goods_type_listing():
    print("\nGoods Type List:")
    for goods in log_goods_type_list:
        print(f"-\t{goods}")

def main_menu_list_output():
    print("Main Menu:") # output menu
    for i, option in enumerate(main_menu_list):print(f"[{i}] {option}")

def view_logs():
    global log_list
    log_list = open("log_list.txt" , "+a")
    log_list.seek(0);log_list_read = log_list.read()
    if log_list_read == "":print("No Logs Available\n")
    else:
        for log in enumerate(log_list_read,1):print(f"\n{log_list_read}");break
    log_list.close() # output list

def record_log():
    with open("log_list.txt" , "+a") as log_list:
        global log_count
        current_entry = "log_number"
        while True:
            if current_entry == "log_number":
                log_number = input("\nRecord Menu:\n[0] Main Menu\n\
Enter Log Number (6 Digits): ") # input check
                if log_number == "0":print("Back To Main Menu\n");break
                elif log_number.isnumeric():
                    if log_number in log_list:print("Log Already Recorded")
                    elif len(log_number) != 6:print("Invalid Digit Count")
                    else:print("Valid Log Number");current_entry = "log_name"
                else:print("Input Contains Invalid Characters")

            elif current_entry == "log_name":
                log_name = input("\n[0] Main Menu\n[-1] Back\n\
Enter Log Name (Character Limit [20]): ")
                if log_name == "0":print("Back To Main Menu\n");break
                elif log_name == "-1":
                    print("Back To Previous Entry")
                    current_entry = "log_number"
                elif len(log_name) > 20:print("Name Too Long")
                else:
                    if log_name.isalnum():
                        current_entry = "log_tracking"
                        print("Valid Log Tracking") # input check
                    else:print("Input Contains Invalid Characters")

            elif current_entry == "log_tracking":
                log_tracking = input("\n[0] Main Menu\n[-1] Back\n\
Enter Log Tracking Number (8 Digits): ")
                if log_tracking == "0":print("Back To Main Menu\n");break
                elif log_tracking == "-1":
                    print("Back To Previous Entry")
                    current_entry = "log_name"
                elif log_tracking.isnumeric():
                    if log_tracking in log_list:
                        print("Tracking Already Used\n")
                    elif len(log_tracking) != 8:print("Invalid Digit Count")
                    else:
                        current_entry = "log_location"
                        print("Valid Log Tracking")
                else:print("Invalid Input\n") # input check

            elif current_entry == "log_location":
                log_location = input("\n[0] Main Menu\n[-1] Back\n\
[1] Location List\nEnter Log Location: ")
                if log_location == "0":print("Back To Main Menu\n");break
                elif log_location == "-1":
                    print("Back To Previous Entry")
                    current_entry = "log_tracking"
                elif log_location == "1":location_listing()
                elif log_location in log_location_list:
                    print("Valid Location");current_entry = "log_goods_type"
                else:print("Invalid Input\n")
                    
            elif current_entry == "log_goods_type":
                log_goods_type = input("\n[0] Main Menu\n[-1] Back\n\
[1] Goods Type List\nEnter Log Goods Type: ")
                if log_goods_type == "0":print("Back To Main Menu\n");break
                elif log_goods_type == "-1":
                    print("Back To Previous Entry")
                    current_entry = "log_location"
                elif log_goods_type == "1":goods_type_listing()
                elif log_goods_type in log_goods_type_list:
                    print("Valid Goods Type\n")
                    current_entry = "full_log"
                else:print("Invalid Input")
                
            elif current_entry == "full_log":
                full_log = f"Log Number:\t{log_number}\nLog Name:\t\
{log_name}\nTracking:\t{log_tracking}\nLocation:\t{log_location}\nGoods:\t\t\
{log_goods_type}\n\n"
                print(f"Log Recorded:\n{full_log}")
                log_list.write(full_log)
                log_list.close();break

def edit_log():
    log_list = open("log_list.txt" , "+a")
    log_list.seek(0)
    log_list_read = log_list.read()
    while True:
        if log_list_read == "":
            print("No Logs Available\n");break
        else:
            for i, log in enumerate(log_list_read,1):print(f"[{i}] {log}")
            delete_option = input("\nEdit Menu:\n[0] Main Menu\n\
Enter Log Index: ")
            if delete_option == "0":print("Back To Main Menu");break
    log_list.close() # output list

def delete_log():
    log_list = open("log_list.txt" , "+a")
    log_list.seek(0)
    log_list_read = log_list.read()
    while True:
        if log_list_read == "":
            print("No Logs Available\n");break
        else:
            for i, log in enumerate(log_list_read,1):print(f"[{i}] {log}")
            delete_option = input("\nDelete Menu\n[0] Main Menu\n\
Enter Log Index: ")
            if delete_option == "0":print("Back To Main Menu");break
    log_list.close() # output list

while True: # main loop
    main_menu_list_output();menu_option = input("Enter Option: ")
    
    if menu_option == "0": # end session
        print("Session Ended");break

    elif menu_option == "1":view_logs() # view logs

    elif menu_option == "2":record_log() # record log

    elif menu_option == "3":edit_log() # edit log
    
    elif menu_option == "4":delete_log() # delete log
        
    else:print("Invalid Input\n") # input check