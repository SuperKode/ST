# TTK4145
# Exc_2

from threading import Thread, Lock

mtx = Lock()
i = 0

# Function for increasing i
def increaseNumber():
	global i
	for x in range(0, 999998):
		mtx.acquire()
		i += 1
		mtx.release()

# Function for decreasing i
def decreaseNumber():
	global i
	for x in range(0, 999999):
		mtx.acquire()
		i -= 1
		mtx.release()

# Main function
def main():
	threadIncNumber = Thread(target = increaseNumber, args = (),)
	threadIncNumber.start()
	threadDecNumber = Thread(target = decreaseNumber, args = (),)
	threadDecNumber.start()
	threadIncNumber.join()
	threadDecNumber.join()
	print(i)

main()
