#!/bin/bash
# Find and clean each ipython notebook
for file in $(find . -iname "*.ipynb");
do
    echo "Cleaning: $file"
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace $file
done

