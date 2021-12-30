#!/bin/bash

docker run \
    -it \
    --rm \
    --name mini_api_dev_container \
    -p 90:90  \
    -v /home/julio/Desktop/todo-backend:/code \
    mini_api \
    /bin/bash