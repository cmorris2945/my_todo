FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and
    returns the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = [line.strip() for line in file_local.readlines()]
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items int eh list in the text files"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items in the list to the text files"""
    with open(filepath, 'w') as file:
        for todo in todos_arg:
            file.write(todo + '\n')
