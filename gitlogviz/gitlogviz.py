import argparse
import subprocess
import sys
import tkinter as tk
from tkinter import Scrollbar, Text

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def save_git_log_graph(commit_limit=10):
    """
    Save and display a visual representation of the git log.

    Parameters:
        commit_limit (int): The number of recent commits to display.

    Returns:
        None
    """
    # Construct the git log command to retrieve a graph of recent commits
    git_log_command = 'git log --graph --oneline --all --format=format:"%h %s"'

    # Execute the git log command and capture the output
    git_log_output = subprocess.check_output(git_log_command, shell=True, text=True)

    # Split the output into lines
    lines = git_log_output.strip().split("\n")

    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Determine the range of commits to display based on the commit_limit parameter
    if isinstance(commit_limit, str) or commit_limit == 0:
        # If commit_limit is 0 or not an integer, display all commits
        commits = lines

    elif commit_limit >= 1:
        # If commit_limit is a positive integer, select the latest 'commit_limit' commits
        commits = lines[:commit_limit]

    elif commit_limit <= -1:
        # If commit_limit is a negative integer, select the first 'abs(commit_limit)' commits
        commits = lines[len(lines) + commit_limit :]

    # Display the first 'commit_limit' lines of the git log output as text on the plot
    ax.text(0.1, 0.9, "\n".join(commits), va="top", fontfamily="monospace")

    # Set the aspect ratio, turn off axis, and display the plot
    ax.set_aspect("auto")
    ax.axis("off")

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Git Log Graph")

    # Create a Canvas widget and pack it into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Create a vertical scrollbar
    v_scrollbar = Scrollbar(
        root, orient=tk.VERTICAL, command=canvas.get_tk_widget().yview
    )
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to use the scrollbar
    canvas_widget.config(yscrollcommand=v_scrollbar.set)

    # Create a Text widget for displaying commit information
    text_widget = Text(root, height=10, width=50, wrap=tk.WORD)
    text_widget.pack(side=tk.BOTTOM)

    # Display the commit information in the Text widget
    text_widget.insert(tk.END, "\n".join(commits))
    text_widget.config(state=tk.DISABLED)  # Disable text editing

    def on_close():
        root.destroy()  # Destroy the Tkinter window when closed
        sys.exit()

    # Set up a protocol to handle the window close event
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Run the Tkinter main loop
    root.mainloop()


def main():
    # Create an argument parser for command-line options
    parser = argparse.ArgumentParser(description="Visualize Git log in a graph.")

    # Add an argument for the number of recent commits to display (default is 3)
    parser.add_argument(
        "--limit", type=int, default=3, help="Number of recent commits to display"
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to save and display the git log graph
    save_git_log_graph(commit_limit=args.limit)


if __name__ == "__main__":
    # Entry point of the script
    main()
