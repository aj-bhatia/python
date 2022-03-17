#!/bin/sh
echo What should I name the file?

read filename

echo How should I describe the file?

read description

if [[ -e "$filename".py ]]; then
	echo This file already exists. Please choose another name.
else
	touch "$filename".py
	echo $'# Ajay Bhatia\n# '"$filename"$'\n# '"$description"$'\n\n\n\nif __name__ == \"__main__\":\n\t' > "$filename.py"
	vim "$filename".py
fi
