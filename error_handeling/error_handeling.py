# file = open("text.txt", "w") #note : here "w" i.e write create a new file

# try:
#     file.write("Hello World")
# finally:
#     file.close()


# or note : here "w" i.e write create a new file

with open("text.txt", "w") as file:
    file.write("Hello World")