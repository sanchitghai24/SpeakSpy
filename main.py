from spy_details import spy_name, spy_salutation, spy_age, spy_rating

status_default = ["Rishte me to hum tumahre baap lagte hai..", "Hum tumahri aukat se bahar hai..","Wanna be the king of spy..Follow me ;)"]
spy_friend_name=[]
spy_friend_age=[]
spy_friend_rating=[]
spy_friend_is_online=[]

def add_friend():
    new_name = input("Add your Co-Spy's Name\n")
    new_salutation = input("Are they Mr or Ms ? : ")
    new_name = new_salutation + "." + new_name
    new_age = input("Age?\n")
    new_rating = input("Spy rating?\n")

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        spy_friend_name.append(new_name)
        spy_friend_age.append(new_age)
        spy_friend_rating.append(new_rating)
        spy_friend_is_online.append(True)
    else:
        print "Sorry..The Spy you entered does not exist"

    return len(spy_friend_name)

def add_status(present_status):
    if present_status!=None:
        print "Your present Status is "+ present_status+"\n"
    else:
        print "You don't have any present status.."

    default = raw_input ("Wanna select from default status ?? (Y/N)\n")

    if default.upper() == "N":
        new_status = raw_input ("Please type your status\n")

        if len(new_status)>0:
            updated_status = new_status
            status_default.append(updated_status)

    elif default.upper() == "Y":
        item_position = 1
        for message in status_default:
            print str(item_position) + ". " + message
            item_position = item_position + 1

        message_selection = input("\n Choose from the above status..")
        if len(status_default)>= message_selection:
            updated_status = status_default[message_selection - 1]

    return updated_status

def start_chat(spy_name,spy_age,spy_rating):
    menu_show = True
    present_status = None

    while menu_show:
        print "MENU\n 1.Add a Status Update\n 2.Add a Friend\n 3.Send a secret message\n 4.Read a secret message\n 5.Read Chats from a User\n 6.Close Application"
        menu_choice = input("Your Choice: ")

        if menu_choice == 1:
            print "You choose Update Status Option.."
            present_status = add_status(present_status)
            print "Status Updated to : "+ present_status
        elif menu_choice == 2:
            print "You choose Add a friend Option.."
        elif menu_choice ==3:
            print "You choose Send a secret message Option.."
        elif menu_choice ==4:
            print "You choose Read a secret message Option.."
        elif menu_choice == 5:
            print "You choose Read Chats Option.."
        else:
            print "You choose Close Application..\n Thank You for your visit !!"
            exit()


question = "Continue as "+spy_salutation+"."+spy_name+" (Y/N)?\n"
user = raw_input(question)

if user.upper() == "Y":
    print ""
else:
    spy_name = raw_input("Hello Spyy...What's your name ??\n")
    spy_salutation = raw_input("What should our community call you ? Mr. , Ms. or Mrs. ?\n")

    if len(spy_name)and len(spy_salutation)>0:
        print "Alright "+ spy_salutation + "." + spy_name + " . We would like to know a little more about.."
    else:
        print "Fields not filled correctly..Please try again.."
        exit()

    spy_age = input("What's your age ??\n")
    spy_age = int(spy_age)

    if spy_age > 50:
         print "OH! Grandpa Spy is here :P "
    elif spy_age <50 and spy_age >12:
        print "Young Spy is here..WELCOME "
    else:
        print "Not Eligible kiddo..Go Home and try again after some years ! "
        exit()

    spy_rating = input("What's your rating??\n")
    spy_rating = float(spy_rating)

    if spy_rating>=4.5:
        print "Hello Undercover Agent Spy.."
    elif spy_rating<4.5 and spy_rating>=3.5:
        print "Hello Foreign Agent Spy"
    elif spy_rating<3.5 and spy_rating>=2.5:
        print "Hello Double Agent Spy"
    elif spy_rating<2.5 and spy_rating>=1.5:
        print "Hello Secret Service Agent Spy"
    else:
        print "I Hope you are promoted soon. Keep up"

print "------------------------------------------------"

spy_is_online = True

print "Authentication Complete! Now you are entering the SpySpeak Zone.."
print "Welcome "+spy_salutation+"."+spy_name+", Age:"+str(spy_age)+", Rating:"+str(spy_rating)+" . Proud to serve you."

start_chat(spy_name,spy_age,spy_rating)

