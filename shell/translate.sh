
#!/bin/bash

# Define a function that runs the 'trans' script with the contents of the clipboard
function translate {
    # Get the contents of the clipboard using xclip
    clipboard=$(xclip -o)

    # Run the 'trans' script with the contents of the clipboard as input
    trans "$clipboard"
}

# Use xclip to monitor the clipboard for changes and run the 'translate' function when it updates
while true; do
    # Wait for the clipboard to change
    xclip -selection clipboard -watch /dev/null || continue

    # Run the 'translate' function
    translate

    # Wait for 2 seconds before checking the clipboard again
    sleep 2
done
