import streamlit as st

import functions
from functions import *
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    write_todos(todos)

    #st.experimental_rerun()

todos = get_todos()


st.title("My Todo Application")
st.subheader("This is my todo application")
st.write("(Hopefully this application with increase your productivity...)")


for index, todo in enumerate(todos):
   checkbox = st.checkbox(todo, key=f"todo_{index}")
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.experimental_rerun()
       


st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
