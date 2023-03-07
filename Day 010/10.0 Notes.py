#FUNCTIONS WITH OUTPUTS

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name"""
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

print(format_name("kamil", "sobania"))