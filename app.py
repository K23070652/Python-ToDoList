import streamlit as st
import csv

# Define the path to the CSV file
tasks_file = "tasks.csv"
completed_file = "completed_tasks.csv"

def load_tasks(file):
    """Load the tasks from the CSV file."""
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]
    except FileNotFoundError:
        return []

def save_tasks(file, task_list):
    """Save the tasks to the CSV file."""
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

def add_task():
    """Handles adding a task."""
    task = st.session_state["new_task"].strip()
    if task:  # Prevent empty tasks
        st.session_state.tasks.append(task)
        save_tasks(tasks_file, st.session_state.tasks)
        st.session_state["new_task"] = ""  # Reset input field

def mark_completed(task):
    """Moves a task to completed list."""
    if task in st.session_state.tasks:
        st.session_state.tasks.remove(task)
        st.session_state.completed.append(task)
        save_tasks(tasks_file, st.session_state.tasks)
        save_tasks(completed_file, st.session_state.completed)
        st.rerun()  # Refresh UI

def delete_task(task):
    """Deletes a task from the tasks list."""
    if task in st.session_state.tasks:
        st.session_state.tasks.remove(task)
        save_tasks(tasks_file, st.session_state.tasks)
        st.rerun()  # Refresh UI

def main():
    st.title("To-Do List")

    
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?cs=srgb&dl=pexels-adrien-olichon-2387793.jpg&fm=jpg");
            background-attachment: fixed;
            background-size: cover;
            color: white;
        }

        .header {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #fff;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        .task-list {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 15px;
            margin-top: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        }

        .task-item {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            margin: 5px 0;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
            font-size: 18px;
        }

        .task-item button, .task-item checkbox {
            background-color: #ff4b5c;
            color: white;
            border: none;
            cursor: pointer;
            padding: 5px;
            border-radius: 3px;
            font-size: 14px;
        }

        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 10px 0;
            text-align: center;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            font-size: 14px;
            font-family: Arial, sans-serif;
        }

        .footer a {
            color: #ff4b5c;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            <p>Made by <a href="https://github.com/K23070652">Manav Sukheja</a></p>
        </div>
        """, unsafe_allow_html=True
    )


    # Initialize session state variables
    if "tasks" not in st.session_state:
        st.session_state.tasks = load_tasks(tasks_file)
    
    # Initialize completed tasks list
    if "completed" not in st.session_state:
        st.session_state.completed = load_tasks(completed_file)

    # Input new tasks
    st.text_input("Add a new task:", key="new_task", on_change=add_task)

    # Button to add task
    if st.button("Add"):
        add_task()
        st.rerun()  # Refresh UI

    # Display tasks with checkboxes and delete
    if st.session_state.tasks:
        st.markdown("<div class='task-list'>", unsafe_allow_html=True)
        st.write("### Current Tasks:")
        for index, task in enumerate(st.session_state.tasks):
            col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
            col1.markdown(f"<div class='task-item'>{task}</div>", unsafe_allow_html=True)
            if col2.checkbox("✅", key=f"checkbox_{task}"):
                mark_completed(task)
            if col3.button("❌", key=f"delete_{task}_{index}"):
                delete_task(task)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No tasks added yet.")

    # Display completed tasks
    if st.session_state.completed:
        st.write("### Completed Tasks ✅")
        for task in st.session_state.completed:
            st.write(f"✅ {task}")

    # Button to clear all tasks
    if st.button("Clear all tasks"):
        st.session_state.tasks.clear()
        save_tasks(tasks_file, st.session_state.tasks) # Save changes to file
        st.rerun()  # Refresh UI

    if st.button("Clear Completed Tasks"):
        st.session_state.completed.clear()
        save_tasks(completed_file, st.session_state.completed) # Save changes to file
        st.rerun() # Refresh UI


if __name__ == "__main__":
    main()