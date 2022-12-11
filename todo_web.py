import streamlit as st
#from modules import todo_functions as f

FILEPATH = 'todos.xls'

# function to get todos
def get_todos(file_path=FILEPATH): #function with default argument
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH): # non default parameters should come first
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)


# import todos
todos = get_todos()

# get and write todo
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    f.write_todos(todos)

todos = get_todos()

st.title('Todo app')

# to complete the todo selected
# eliminate the todo from the state
# and rerun the checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.write('##')
st.text_input('',
              placeholder='Enter a todo',
              on_change=add_todo,
              key='new_todo')


st.session_state