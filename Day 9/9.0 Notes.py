#DICTIONARES
# key:value
# word in dictionary:definition of the word

key_value_dict = {
"Key":"Value",
"Key2":"Value2",
"Key3":"Value3",
}

#RETRIEVING ITEMS FROM DICT
print(key_value_dict["Key2"])

#ADDING NEW ITEM TO DICT
key_value_dict["Key4"] = "Value4"
print(key_value_dict)

#CREAT EMPTY DICT
empty_dict = {}
empty_dict["Key"] = "Value"
print(empty_dict)

#WIPE EXISTING DICT
key_value_dict = {}
print(key_value_dict)

#EDIT AN ITEM IN DICT
empty_dict["Key"] = "Value2"
print(empty_dict)

#LOOP THROUGH A DICT
for thing in empty_dict:
    print(thing)  # ONLY KEYS
    print(empty_dict[thing])  # KEYS AND VALUES
