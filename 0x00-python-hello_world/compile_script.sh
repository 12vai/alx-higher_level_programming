#!/bin/bash

# Check if PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable not set."
    exit 1
fi

# Compile the Python script
python -m py_compile "$PYFILE"

# Get the base filename without extension
filename_without_extension=$(basename "$PYFILE" ".py")

# Rename the compiled file to the desired format
compiled_filename="$filename_without_extension.pyc"
mv "__pycache__/$filename_without_extension.cpython-*.pyc" "$compiled_filename"

# Clean up the __pycache__ directory
rm -rf "__pycache__"

echo "Compilation completed. Compiled file: $compiled_filename"

