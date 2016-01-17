# TTK4145
# Exc_1

from threading import Thread

i = 0

# Function for increasing i
def increaseNumber():
	global i
	for x in range(0, 999999)
		i += 1
		
# Function for decreasing i
def decreaseNumber():
global i
	for x in range(0, 999999)
		i -= 1

# Main function
main:
    threadIncNumber = Thread(target = increaseNumber, args = (),)
    threadIncNumber.start()
	
	threadDecNumber = Thread(target = decreaseNumber, args = (),)
    threadDecNumber.start()
	
	threadIncNumber.join()
    threadDecNumber.join()
	
    print(i)
	
main()
