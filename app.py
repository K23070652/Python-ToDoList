import streamlit as st
import csv

# Define the path to the CSV file
tasks_file = "tasks.csv"

def load_tasks():
    """Load the tasks from the CSV file."""
    try:
        with open(tasks_file, "r") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]
    except FileNotFoundError:
        return []

def save_tasks(task_list):
    """Save the tasks to the CSV file."""
    with open(tasks_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

def main():
    st.title("To-Do List")

    # Set background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?cs=srgb&dl=pexels-adrien-olichon-2387793.jpg&fm=jpg");
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize task list in session state
    if "tasks" not in st.session_state:
        st.session_state.tasks = load_tasks()

    # Input new tasks
    task_input = st.text_input("Add a new task:")
    
    if st.button("Add"):
        if task_input.strip():  # Prevent empty tasks
            st.session_state.tasks.append(task_input)
            save_tasks(st.session_state.tasks)  # Save updated tasks
            st.rerun()  # Refresh the UI to show new tasks

    # Display tasks
    if st.session_state.tasks:
        st.write("Current tasks:")
        for i, task in enumerate(st.session_state.tasks):
            st.write(f"{i+1}. {task}")

    else:
        st.write("No tasks added yet.")

    # Button to clear all tasks
    if st.button("Clear all tasks"):
        st.session_state.tasks.clear()
        save_tasks(st.session_state.tasks)  # Save changes
        st.rerun()  # Refresh UI

if __name__ == "__main__":
    main()