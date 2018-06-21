import time
import webbrowser
import random

#Add your fav jams here. Could just upload link, but
#I like to keep a record of whats already been added
inspectorNorse = "https://www.youtube.com/watch?v=ebjXsc0UjdQ"
theKeyTheSecret = "https://www.youtube.com/watch?v=_j-Tji1DueU"
rayOfLight = "https://www.youtube.com/watch?v=a4tD8dy9Reg"
doctorPressure = "https://www.youtube.com/watch?v=492p1sCou_U"
scatMan = "https://www.youtube.com/watch?v=Hy8kmNEo1i8"
sexyThing = "https://www.youtube.com/watch?v=YUY9Y9RFiHY"
gotToGiveItUp = "https://www.youtube.com/watch?v=Ayyy-03ITDg"
youShouldBeDancing = "https://www.youtube.com/watch?v=_JoZS6LgqYI"
meine = "https://www.youtube.com/watch?v=h7qTI6Njp9g"
aintNoMountain = "https://www.youtube.com/watch?v=-C_3eYj-pOM"
callOnMe = "https://www.youtube.com/watch?v=7ou6MoKmxFQ"
jazzPotato = "https://www.youtube.com/watch?v=vmOArLdg9d4"
pinaColada = "https://www.youtube.com/watch?v=TazHNpt6OTo"

def take_a_break():
	for i in range(4):
		#Select the amount of time you want, before a break-reminder
		#i.e. great song comes on
		time.sleep(35*60)
		choices = [inspectorNorse,
			theKeyTheSecret,
			doctorPressure,
			scatMan,
			rayOfLight,
			callOnMe,
			youShouldBeDancing,
			sexyThing,
			jazzPotato,
			meine,
			aintNoMountain,
			pinaColada,
			gotToGiveItUp]
		webbrowser.open(random.choice(choices))

take_a_break()


