import numpy as np
#numpy libary
from time import sleep
#time libary
from random import randint

def fake_initializing():
	#function for faking waiting phase
	print("initializing...")
	#output "inizilising"
	sleep(3)
	#waits 3 sec.
	print("compiling...")
	sleep (3)
	print("finished")
	
rng = np.random.default_rng() 
#Randomizer

n = 29
#amout of numbers needed

r = np.zeros(n) 
#generates array with 3 zeros

error = 0
#variables which counts the revelutions

t = 0
#index 

fake_initializing()
#fakes loading phase

for i in range(n):
	#Loop; i goes from 0 to 2
	r[i] = rng.integers(low=1, high=24, size=1)
	#generates random number between 1-24
	if i == 0:
		print(r[i])
		#output first random number
	else:
		while t < i:
			if r[t] == r[i]:
			    #checking for double numbers
				r[i] = rng.integers(low=1, high=24, size=1)
				#print("t = ",t)
				t = 0
				error += 1
				#adds 1 too the value of error	
				if error >= 100:
					print("Fehler: generiert identische Zahlen, keine Zufallsgeneration möglich")
					quit() 
					#quits programm after 100 revelutions
			t += 1 
		print(r[i])
		#output random number
		error = 0
		t = 0
	sleep(2)
		#waits 2 sec. for excitment