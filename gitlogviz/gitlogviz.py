import argparse
import subprocess

import matplotlib.pyplot as plt


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

    # Display the first 'commit_limit' lines of the git log output as text on the plot
    ax.text(0.1, 0.9, "\n".join(lines[:commit_limit]), va="top", fontfamily="monospace")

    # Set the aspect ratio, turn off axis, and display the plot
    ax.set_aspect("auto")
    ax.axis("off")
    plt.show()


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
