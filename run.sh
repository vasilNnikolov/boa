#!/bin/bash

start_dir="$(pwd)/"
image_dir="$start_dir"bad_images/
function get_images_from_web {
    if [ -d $image_dir ]; then
        rm -r $image_dir 
    fi
    mkdir $image_dir 
    links="${start_dir}image_links.txt"

    while IFS= read -r line; do
        wget -q $line -P $image_dir
    done < $links 
}

get_images_from_web

echo "got images"

python3 file.py

# rm ${start_dir}bad_images/
