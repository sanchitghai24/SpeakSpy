from spy_details import spy
from steganography import Steganography
from datetime import datetime

status_default = ["Rishte me to hum tumahre baap lagte hai..", "Hum tumahri aukat se bahar hai..","Wanna be the king of spy..Follow me ;)"]
spy_friend = []


def send_message():
    friend_choice = friend_selection()

    original_image = input("What is the name of the image?")
    output_path = 'output.jpg'
    text = input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    spy_friend[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"

def read_message():
    sender = friend_selection()

    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    spy_friend[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"

def friend_selection():
    friend_number = 0

    for friend in spy_friend:
        print '%d. %s' % (friend_number + 1), friend['name']

    friend_number = friend_number + 1

    friend_choice = input("Choose from your friends")
    friend_choice_position = friend_choice - 1

    return friend_choice_position

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = input("Tell us your friend's name : ")
    new_friend['salutation'] = input("Are they Mr or Ms ?: ")
    new_friend['name'] = new_friend['salutation'] + "." + new_friend['name']
    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        spy_friend.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(spy_friend)

def add_status(present_status):
    if present_status!=None:
        print "Your present Status is : "+ present_status+"\n"
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

def start_chat(spy):
    menu_show = True
    present_status = None

    while menu_show:
        print "MENU\n 1.Add a Status Update\n 2.Add a Friend\n 3.Send a secret message\n 4.Read a secret message\n 5.Read Chats from a User\n 6.Close Application"
        menu_choice = input("Your Choice: ")

        if menu_choice == 1:
            print "You choose Update Status Option.."
            present_status = add_status(present_status)
            print "Status Updated to : " + present_status
        elif menu_choice == 2:
            print "You choose Add a friend Option.."
            all_friends = add_friend()
            print "You have %d friends now.." % (all_friends)
        elif menu_choice == 3:
            print "You choose Send a secret message Option.."
            send_message()
        elif menu_choice == 4:
            print "You choose Read a secret message Option.."
            read_message()
        elif menu_choice == 5:
            print "You choose Read Chats Option.."
        else:
            print "You choose Close Application..\n Thank You for your visit !!"
            exit()


question = "Continue as "+spy['salutation']+"."+spy['name']+" (Y/N)?\n"
user = raw_input(question)

if user.upper() == "Y":
    print ""
else:
    spy['name'] = raw_input("Hello Spyy...What's your name ??\n")
    spy['salutation'] = raw_input("What should our community call you ? Mr. , Ms. or Mrs. ?\n")

    if len(spy['name'])and len(spy['salutation'])>0:
        print "Alright "+ spy['salutation'] + "." + spy['name'] + " . We would like to know a little more about.."
    else:
        print "Fields not filled correctly..Please try again.."
        exit()

    spy['age'] = input("What's your age ??\n")
    spy['age'] = int(spy['age'])

    if spy['age'] > 50:
         print "OH! Grandpa Spy is here :P "
    elif spy['age'] <50 and spy['age'] >12:
        print "Young Spy is here..WELCOME "
    else:
        print "Not Eligible kiddo..Go Home and try again after some years ! "
        exit()

    spy['rating'] = input("What's your rating??\n")
    spy['rating'] = float(spy['rating'])

    if spy['rating']>=4.5:
        print "Hello Undercover Agent Spy.."
    elif spy['rating']<4.5 and spy['rating']>=3.5:
        print "Hello Foreign Agent Spy"
    elif spy['rating']<3.5 and spy['rating']>=2.5:
        print "Hello Double Agent Spy"
    elif spy['rating']<2.5 and spy['rating']>=1.5:
        print "Hello Secret Service Agent Spy"
    else:
        print "I Hope you are promoted soon. Keep up"

print "------------------------------------------------"

spy_is_online = True

print "Authentication Complete! Now you are entering the SpySpeak Zone.."
print "Welcome "+spy['salutation']+"."+spy['name']+", Age:"+str(spy['age'])+", Rating:"+str(spy['rating'])+" . Proud to serve you."

start_chat(spy)

