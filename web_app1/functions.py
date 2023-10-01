FILEPATH = r"C:\Users\steve\PycharmProjects\pythonProject\venv\my_tutorials\files\todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos

    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())