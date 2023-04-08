# file = open("my_file.txt", )
# content = file.read()
# print(content)
# file.close()

with open("my_file.txt") as file:
    content = file.read()
    print(content)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text")

with open("new_file.txt", mode="w") as file:
    file.write("New Text\n")


"""
bein in the same folder:        ./file.txt, ./next_folder/file.txt
goin to the previous folder:    ../file.txt, ../previous_folder/file.txt
"""