#Perform the following operations on the dictionary :
#8/2/23
#
#By Anupam Kanoongo

# create an empty dictionary
friends = {}

# input friends and their mobile numbers
while True:
    name = input("Enter the name of your friend (type 'stop' to exit): ")
    if name == 'stop':
        break
    mobile = input("Enter the mobile number of your friend: ")
    friends[name] = mobile

# display the name and mobile number of all friends
print("\nFriends and their mobile numbers:")
for name, mobile in friends.items():
    print(name,":",mobile)

# add a new friend to the dictionary
new_friend = input("\nEnter the name of the new friend: ")
new_mobile = input("Enter the mobile number of the new friend: ")
friends[new_friend] = new_mobile

# display the modified dictionary
print("\nModified dictionary:")
for name, mobile in friends.items():
    print(name,":",mobile)

# delete a friend from the dictionary
delete_friend = input("\nEnter the name of the friend you want to delete: ")
del friends[delete_friend]

# display the modified dictionary
print("\nModified dictionary:")
for name, mobile in friends.items():
    print(f"{name}: {mobile}")

# modify the mobile number of an existing friend
modify_friend = input("\nEnter the name of the friend whose mobile number you want to modify: ")
modify_mobile = input("Enter the new mobile number: ")
friends[modify_friend] = modify_mobile

# display the modified dictionary
print("\nModified dictionary:")
for name, mobile in friends.items():
    print(f"{name}: {mobile}")

# check if a friend is present in the dictionary or not
check_friend = input("\nEnter the name of the friend you want to check: ")
if check_friend in friends:
    print("The given friend is in the dictionary")
else:
    print("The given friend is not in the dictionary")
