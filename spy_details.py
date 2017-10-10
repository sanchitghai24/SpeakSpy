from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        #constructor with parameters
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = [] #we can add this entry later
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Natkhat','Mr.',24,9.4)
#calling class objects and giving values to the parameters + it's better than dictionary
friend_one = Spy('Sherlock', 'Mr.', 21,8.2)
friend_two = Spy('Jean', 'Mrs.', 48,7.2)
friend_three = Spy('Hawk', 'Mrs.', 35, 4.2)
friend_four=Spy('Neckromancer007','Mr.',22,6.4)
friend_five=Spy('Popeye','Mr.',29,7.5)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five]