# Running Scripts

## Concepts

Here I'll also explain a couple of important concepts on packaging
Python scripts effectively so anyone can run them.

These package principles are widely used across different languages, and the
specific one that we'll focus on is dependency management using configuration
and lock files.

## UV - Astral

UV is a Python dependency manager developed by Astral, built with Rust.
It's inspired in cargo, which is the dependency manager used in Rust. It is
fast, reliable, and super easy to use.

### Initialization

When initializing a project, UV provides us with the `uv init` command. It
initializes a couple of
files for us. The most important being `pyproject.toml`.

The toml file is a configuration file
where we declare our dependencies, sources, and package distribution specifics.
With that file created, running the command `uv sync` will create a Python
virtual environment.

### The Virtual Environment

This is a super important Python topic that I recommend you get familiar with,
since this knowledge
will help you debug a big number of issues that could arise in your Python
development.

To activate your environment, so that you use the correct interpreter, you will
need to execute
a command compatible with your current operating system. Go ahead and google
that.

`how to activate a Python virtual environment`

With the virtual environment activated, all packages that we add to our
configuration will automatically
be available to use.

### Adding and removing packages

We could manually work throughout the dependency version tree by looking at each
package
spec and provide a valid range using the correct syntax in the toml file.

That would be fun, wouldn't it? Probably not.

Fortunately, UV does that for us. If you want to add or remove a package, it's
as simple as running
the following commands:

```shell
uv add duckdb
uv remove duckdb
```

It'll check your current installed packages and assign a valid version.

### Running scripts

To run the scripts, we have a variety of valid ways. If you want to go with the
CLI,
UV has the run command that helps by activating the virtual environment for you.

```shell
uv run my_script.py
```

If you're using a Python IDE, it'll probably handle all of that for you. PyCharm
should do everything natively, and VSCode can also do that if you install an
auto-venv extension.

### Python Modules

...

