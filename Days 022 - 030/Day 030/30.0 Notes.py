# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"error: {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("wee woo error")


# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("human height should not be over 3m")
# bmi = weight / height ** 2
# print(bmi)
