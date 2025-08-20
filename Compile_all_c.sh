#!/bin/bash

# Find all .c files recursively
find . -type f -name "*.c" | while read -r file; do
    dir=$(dirname "$file")                  # Directory of the .c file
    base=$(basename "$file" .c)             # Filename without extension
    echo "Compiling $file in $dir..."
    gcc -O3 -fomit-frame-pointer -funroll-loops "$file" -lm -o "$dir/$base"
done
