import time

dev_list = ["yolo", 786, ["Yes", "No"],"hello", True, "Pi"]
user_list = []

print("Calculating developer list...")
time.sleep(1)
print(dev_list)
print("But wait there is a nested list within the list...listception! Calculating...")
time.sleep(1)
print(dev_list[2])
print(dev_list[2][0])
print(dev_list[2][1])
print("Now let's do stuff to it!")
time.sleep(1)
print("First let's check the length of the string.")
time.sleep(1)
print(len(dev_list), "elements")
time.sleep(1)
print("CLONE THAT SON OF A GUN!")
clonedev_list = dev_list[:]
time.sleep(1)
print(dev_list)
print(clonedev_list, "<-Clone")
time.sleep(1)
print("Now let's do some things to the clone list!")
time.sleep(1)
print("Let's add a zebra to the list")
clonedev_list.append("zebra")
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("Coolio, now let's add a number in the middle.")
clonedev_list.insert(2, 1234)
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("Let's get rid of Pi.")
del clonedev_list[6]
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("Let's remove hello as well, I don't feel like it needs to be there.")
clonedev_list.remove("hello")
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("I want that yolo, I NEED IT!")
NEEDIT = clonedev_list.pop(0)
print(NEEDIT)
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("Crap! I need that yolo back in ma list!")
print("It's alright, concatenate man is here to save the day!")
clonedev_list = clonedev_list + ["yolo"]
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("PHEEEEEW, got scared there for a minute...")
time.sleep(1)
print("Ok let's finish up by printing the list out, one element at a time.")
for element in clonedev_list:
	time.sleep(1)
	print(element)
    
time.sleep(3)
print("Ok, now you can add some stuff to your own list.")
time.sleep(1)
x = True
while x == True:
	print("Would you like to add something to your list?")
	answer = input(">  ")
	if answer == "yes":
		time.sleep(1)
		print("What would you like to add?")
		item = input(">  ")
		user_list.append(item)
		time.sleep(1)
		print("Your list is now:", user_list)
	else:
		time.sleep(1)
		print("Your list = ", user_list)
		time.sleep(1)
		x = False
		print("Ok, list program signing off, cheers!")
