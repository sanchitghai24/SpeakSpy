
spy_name = raw_input("Hello Spyy...What's your name ??\n")
spy_salutation = raw_input("What should our community call you ? Mr. , Ms. or Mrs. ?\n")

if len(spy_name)and len(spy_salutation)>0:
    print "Alright "+ spy_salutation + "." + spy_name + " . We would like to know a little more about.."
else:
    print "Please fill the Name and Salutation fields.."

spy_age = 0
spy_rating = 0.0
spy_is_online = False

spy_age = input("What's your age ??\n")

if spy_age > 50:
    print "OH! Grandpa Spy is here :P "
elif spy_age <50 and spy_age >12:
    print "Young Spy is here..WELCOME "
else:
    print "Not Eligible kiddo..Go Home and try again after some years ! "
    exit()

spy_rating = input("What's your rating??\n")

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

