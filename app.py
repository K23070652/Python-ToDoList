import streamlit as st
import csv

# Define the path to the CSV file
tasks_file = "tasks.csv"

def load_tasks():
    """
    Load the tasks from the CSV file.
    """
    try:
        with open(tasks_file, "r") as f:
            reader = csv.reader(f)
            task_list = [row[0] for row in reader]
    except FileNotFoundError:
        task_list = []
    return task_list


def display(task_list):
    # Display the current tasks
    if len(task_list) == 0:
        st.write("No tasks added yet.")
    else:
        st.write("Current tasks:")
        for i, task in enumerate(task_list):
            st.write(f"{i+1}. {task}")


def save_tasks(task_list):
    """
    Save the tasks to the CSV file.
    """
    with open(tasks_file, "w", newline="") as f:
        f.truncate(0)
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])


def main():
    st.title("To-Do List")
    
    
# Load the tasks from the CSV file
task_list = load_tasks()

# Input new tasks
task_input = st.text_input("Add a new task:")
if st.button("Add"):
    if task_input != "":
        # Add the new task to the list and save it to file
        task_list.append(task_input)
        save_tasks(task_list)
        task_input = ""
        display(task_list)

#Button to clear all tasks
if st.button("Clear all tasks"):
    # Clear the task list and save the changes to file
    task_list.clear()
    save_tasks(task_list)
    display(task_list)

#Run the app
if __name__ == "__main__":
    main()