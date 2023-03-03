# simple function
def greet():
    print("Something")
greet()

# function that allows for input
def greet_name(name):
    print(f"Hello {name}")
greet_name("Kamil")

#something = 123
#    ^        ^
#parameter = argument

# functions with more than one input
def greet_with(thing, name):
    print(f"Isn't the {thing} nice today, {name}?")

# positional argument
greet_with("weather", "Kamil")

# keyword argument
greet_with(name="Kamil", thing="weather")
