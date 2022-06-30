# pre-commit-template
pre-commit template to use in Python projects

## Quick start

1. Install pre-commit
    ```
    # using pip
    pip install pre-commit

    # using homebrew
    brew install pre-commit
    ```
2. Create a pre-commit config file.
    ```
    touch .pre-commit-config.yaml
    pre-commit sample-config >> .pre-commit-config.yaml
    ```
3. Install the git hook scripts.
    ```
    pre-commit install
    ```
