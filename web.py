import streamlit as st
import functions as functions


def add_todo():
    new_todo = st.session_state["new"].title() + '\n'
    todolist.append(new_todo)
    functions.write_todolist(todolist)


todolist = functions.get_todolist()

st.title('TaskMaster')
st.subheader("A minimalist To-do app.")
st.write("This app is to increase your productivity.")

for ind, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if todo.strip('\n') == '':
        todolist.remove(todo)
        functions.write_todolist(todolist)
    if checkbox:
        todolist.pop(ind)
        functions.write_todolist(todolist)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="", placeholder="Enter a new todo to be added",
              on_change=add_todo, key="new")
