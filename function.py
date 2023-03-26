FILEPATH = 'todo.txt'


def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of
    to_do items"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """Write the to_do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__index-py-12__":
    print("Hello")
    print(get_todos())