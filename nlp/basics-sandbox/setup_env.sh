#!/bin/bash

# Check if virtual environment directory exists
if [ ! -d "sklearn-env" ]; then
    # Create the virtual environment if it doesn't exist
    echo "Creating virtual environment..."
    python -m venv sklearn-env
else
    echo "Virtual environment already exists."
    if [ -z "$@" ]; then
        echo "Install packages using $0 <name_of_the_package_1> <...> ..."
    fi
fi

# Activate the virtual environment
source sklearn-env/bin/activate

# Check if any packages were provided as arguments
if [ "$#" -eq 0 ]; then
    echo "No packages specified. Exiting."
    exit 1
fi

# Function to check if a Python package is installed
check_and_install() {
    PACKAGE=$1
    if ! pip show $PACKAGE &> /dev/null; then
        echo "$PACKAGE is not installed. Installing..."
        pip install -U $PACKAGE
    else
        echo "$PACKAGE is already installed."
    fi
}

# Loop through all the packages provided as arguments
for PACKAGE in "$@"; do
    check_and_install $PACKAGE
done

echo "All specified packages are handled."