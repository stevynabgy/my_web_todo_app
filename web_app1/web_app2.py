import streamlit as st
import pathlib

import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"  #session_state is a type of dictionary data type
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is App is to improve your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder=" Add New Todo ...",
              on_change=add_todo, key='new_todo')


#st.session_state
# to stop run in terminal use Cntrl+C
# to add required files for web app run " pip freeze  > requirements.txt " in terminal
# enable version control from VCS pull down menu. Select GIT
#connect to git hub by creating new package in Github ; copy the url ;Click on GiT select manage remote and paste URL
#to link to Github