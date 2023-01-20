# Example Applications of `shiny_semantic` in PyShiny
Demo applications using Shiny for Python with Shiny Semantic

## How to use this repository?

This is a monorepo with each folder being a separate shiny application with its own `README`, `requirements.txt` (to isolate dependencies), `manifest.json` (to isolate deployments).

To launch any application, navigate to the appropriate directory and follow the instructions in the README.

For example, to run `semantic-components` locally, one has to do the following steps:

```shell
# Unix terminal

# Navigate to the application's folder
cd semantic-components

# Create new virtual environment
python3 -m venv .venv

# Activate this environment
source .venv/bin/activate

# Install application's dependencies
pip install -r requirements.txt

# Launch the application
shiny run
```

## Development

For better development experience it is recommended to open each application in a separate IDE window to leverage code suggestions, formatting, etc.


## Deployment

All instructions below have two assumptions: (1) you are in an application-folder, not in the root (e.g. inside `semantic-components`) and (2) you have activated a virtual environment of the application that you are trying to deploy.

Shiny-for-Python allows easy deployment on RSConnect. First, make sure that the rsconnect CLI client is installed:

```shell
pip install rsconnect-python
```

First time configuration for the Appsilon team:

```
rsconnect add \
    --name connect.appsilon.com \
    --server https://connect.appsilon.com/ \
    --key <Insert your API key>
```

We rely on continuous delivery via git-backed deployment on RSConnect. Each application should have a separate `manifest.json` file, because each application is a separate deployment.

```
rsconnect write-manifest shiny \
    --overwrite \
    --exclude "**/*.pyc" \
    --exclude .DS_Store \
    . # APPLICATION DIRECTORY
```

When developing a feature on a feature branch, you can make a manual deployment (it is recommended to delete such deployments after the feature is merged into main):

```
rsconnect deploy shiny .
```
