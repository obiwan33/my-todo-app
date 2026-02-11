import streamlit as st
from streamlit import checkbox

import functions


todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["todo"] + "\n"
    todos.append(new_todo.title())
    functions.write_todos(todos)


st.title("My To do Apps")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="todo")
