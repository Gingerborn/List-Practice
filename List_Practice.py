import time #imports the time module

dev_list = ["yolo", 786, ["Yes", "No"],"hello", True, "Pi"] #first list
user_list = [] #second list that will be edited by the user

print("Calculating developer list...")
time.sleep(1)
print(dev_list) #prints the dev list
print("But wait there is a nested list within the list...listception! Calculating...")
time.sleep(1)
print(dev_list[2]) #prints the nested list
print(dev_list[2][0]) #prints the first element in the nested list, "Yes"
print(dev_list[2][1]) #prints the second element in the nested list, "No"
print("Now let's do stuff to it!")
time.sleep(1)
print("First let's check the length of the string.")
time.sleep(1)
print(len(dev_list), "elements") #prints the current length of the dev list
time.sleep(1)
print("CLONE THAT SON OF A GUN!")
clonedev_list = dev_list[:] #clones the dev list by using a slice and sets it to clonedev list
time.sleep(1)
print(dev_list)
print(clonedev_list, "<-Clone")
time.sleep(1)
print("Now let's do some things to the clone list!")
time.sleep(1)
print("Let's add a zebra to the list")
clonedev_list.append("zebra") #adds zebra to the end of the clonedev list
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("Coolio, now let's add a number in the middle.")
clonedev_list.insert(2, 1234) #inserts number 1234 into the 2 position of the clonedev list between 786 and the nested list
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("Let's get rid of Pi.")
del clonedev_list[6] #deletes "Pi" using del
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("Let's remove hello as well, I don't feel like it needs to be there.")
clonedev_list.remove("hello") #removes "hello" from the clonedev list
time.sleep(1)
print(clonedev_list)
time.sleep(1)
print("I want that yolo, I NEED IT!")
NEEDIT = clonedev_list.pop(0) #pops "yolo" out of the list and sets it to NEEDIT
print(NEEDIT)
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("Crap! I need that yolo back in ma list!")
print("It's alright, concatenate man is here to save the day!")
clonedev_list = clonedev_list + ["yolo"] #adds "yolo" back into the list using concatenation
time.sleep(1)
print("New list =", clonedev_list)
time.sleep(1)
print("PHEEEEEW, got scared there for a minute...")
time.sleep(1)
print("Ok let's finish up by printing the list out, one element at a time.")
for element in clonedev_list: #this for loop prints out each element line by line
	time.sleep(1)
	print(element)
    
time.sleep(3)
print("Ok, now you can add some stuff to your own list.")
time.sleep(1)
x = True #sets x to true in order to close the while loop
while x == True:
	print("Would you like to add something to your list?")
	answer = input(">  ") #questions if you want to continue
	if answer == "yes":
		time.sleep(1)
		print("What would you like to add?")
		item = input(">  ") #asks the item you want to add and sets it to item
		user_list.append(item) #adds the item to the end of the list using append
		time.sleep(1)
		print("Your list is now:", user_list)
		number = 0 #this is for later when I want to delete the list fully
		number = number + 1 #everytime the while loop loops the number adds 1 to count the number of loops/elements added
	else: #if the answer earlier was no or something else than yes then it print the user list and closes the while loop
		time.sleep(1)
		print("Your list = ", user_list)
		time.sleep(1)
		x = False

time.sleep(1)
print("Now I think that' enough with our lists, let's destroy the evidence.")
time.sleep(1)
del clonedev_list[0:6] #deletes the entire clonedev list using a slice
del user_list[0:number + 1] #deletes the entire user list using a slice between 0 and how many times the while loop looped
print(clonedev_list, "Our first list has been deleted...")
time.sleep(1)
print(user_list, "Your list has been deleted...")
time.sleep(1)
print("Ok, list program signing off, cheers!")
