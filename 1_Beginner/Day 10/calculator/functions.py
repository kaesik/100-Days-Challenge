def add(num_a, num_b):
    """Function adds num_a to num_b"""
    return num_a + num_b


def subtract(num_a, num_b):
    """Function subtracts num_b from num_a"""
    return num_a - num_b


def multiply(num_a, num_b):
    """Function multiply num_a by num_b"""
    return num_a * num_b


def divide(num_a, num_b):
    """Function divide num_a by num_b"""
    return num_a / num_b


def calculation(num_a, num_b, operation):
    function = operations[operation]
    answer = function(num_a, num_b)
    return answer


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}