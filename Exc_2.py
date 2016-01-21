# TTK4145
# Exc_2

from threading import Thread, Lock

mtx = Lock()
i = 0

# Function for increasing i
def increaseNumber():
  mtx.aquire()
	  global i
	  for x in range(0, 999998)
		  i += 1
	mtx.release()

# Function for decreasing i
def decreaseNumber():
  mtx.aquire()
    global i
	  for x in range(0, 999999)
		  i -= 1
	mtx.release()

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
