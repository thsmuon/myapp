import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)
    print(todo)



st.title("My todo App")
st.subheader("This is my todo app")

st.write("This is to improve activity")

st.checkbox("Buy grocery")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')
