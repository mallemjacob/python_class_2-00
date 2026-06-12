# Class Notes: Virtual Environments

## File

`02_virtual_environment_notes.md`

## What It Is

A virtual environment is an isolated Python workspace for one project.

Different projects can use different package versions:

- Python game: Python 3.14, pygame
- Website: Python 3.15, Flask, requests
- Machine learning: Python 3.19, data science packages

## What It Does

- Keeps project packages separate.
- Lets one project use different package versions from another project.
- Prevents installed packages from becoming messy across the whole computer.
- Makes class projects easier to run again later.

## Why Use It

Without a virtual environment, packages for all projects are installed in the
same place. That can cause version conflicts. A virtual environment gives each
project its own clean space.

## Commands

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install requests flask
```

Deactivate it:

```bash
deactivate
```

## Watch Out For

- Activate the virtual environment before installing packages.
- If `python` does not work, try `python3`.
- Do not commit the `.venv/` folder to Git.
- If packages are missing, check that the virtual environment is activated.
- A virtual environment does not automatically install packages; you still use
  `pip install`.

## Class Flow

1. We used `requests` to call a website.
2. The website returned JSON data.
3. We converted the response using `.json()`.
4. We displayed part of that data in our own Flask website.
