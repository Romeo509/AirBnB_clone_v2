#!/bin/bash

# Check if a folder path is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <folder_path>"
    exit 1
fi

# Get the folder path from the command-line argument
local_folder_path="$1"

# Define the remote servers
servers=("ubuntu@100.26.132.7" "ubuntu@107.23.95.221")

# Loop through each server and transfer the folder to the home directory
for server in "${servers[@]}"; do
    # Use scp with -r to copy the folder to the remote server's home directory
    scp -r -i ~/.ssh/id_rsa "$local_folder_path" "$server":~

    # Check the exit status of scp
    if [ $? -eq 0 ]; then
        echo "Folder transfer to $server successful!"
    else
        echo "Folder transfer to $server failed."
    fi
done
