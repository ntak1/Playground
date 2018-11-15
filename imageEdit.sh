#!/bin/bash

command=$1

if [ "$command" ==  "gray_scale" ]
then
    echo "Input the directory name: "
    read base_dir
    if [ -z $base_dir ]
    then
        echo "You didn't input the name"
    else
        for image in `ls $base_dir`; do
            #echo item: $image
            image_name=$base_dir/${image%.*}
            echo $image_name
            convert $base_dir/$image -set colorspace Gray -separate -average $image_name"_out.png"
        done
    fi
fi
