# py_shiny_semantic_examples
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
