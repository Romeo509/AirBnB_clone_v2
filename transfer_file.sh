#!/bin/bash

# Check if a filename is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Get the filename from the command-line argument
local_file_path="$1"

# Define the remote servers
servers=("ubuntu@100.26.132.7" "ubuntu@107.23.95.221")

# Loop through each server and transfer the file to the home directory
for server in "${servers[@]}"; do
    # Use scp to copy the file to the remote server's home directory
    scp -i ~/.ssh/id_rsa "$local_file_path" "$server":~

    # Check the exit status of scp
    if [ $? -eq 0 ]; then
        echo "File transfer to $server successful!"
    else
        echo "File transfer to $server failed."
    fi
done
