#!/bin/bash
find . -type f -name "*.c" | while read -r file; do
    binary=${file%.c}                  # Remove .c to get the binary path
    exec_dir=$(dirname "$binary")     # Directory where the binary is
    exec_name=$(basename "$binary")   # Name of the binary itself

    echo "Changing to $exec_dir and running $exec_name"
    
    if [ -x "$binary" ]; then
        cd "$exec_dir" || { echo "Failed to enter $exec_dir"; continue; }
        ./"$exec_name" &
        cd - > /dev/null               # Return to previous directory silently
    else
        echo "Executable $binary not found or not executable"
    fi
done
