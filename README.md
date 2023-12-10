# GitLogViz

GitLogViz is a tool for visualizing the Git log in a graph. It provides a simple and interactive way to explore the commit history of a Git repository.

## Installation

You can install GitLogViz using `pip`. Make sure you have Python and pip installed on your system.

```bash
pip install gitlogviz
```

## Usage

Once installed, you can use GitLogViz by running the `gitlogviz` command in your terminal. By default, it will display a visual representation of the last 10 commits. You can customize the number of commits displayed using the `--limit` option.

```bash
# Display the latest 5 commits
gitlogviz --limit 5
```

This will show a graph of the last 5 commits.

### Advanced Usage

GitLogViz provides flexible options for visualizing commit history. The `--limit` option allows you to control the number of commits displayed in the graph. For example, to view the first 8 commits:

```bash
gitlogviz --limit 8
```

To show all commits, use:

```bash
gitlogviz --limit all
```

Additionally, you can use negative values to display commits relative to the latest, for instance:

```bash
# Display the first 3 commits
gitlogviz --limit -3
```

Experiment with different values to tailor the visualization to your needs.

## Contributing

If you would like to contribute to GitLogViz or report issues, please visit the [GitHub repository](https://github.com/okpyjs/gitlogviz). We welcome your feedback and contributions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
