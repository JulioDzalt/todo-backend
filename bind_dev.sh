#!/bin/bash

docker run -it --name mini_api_container -p 90:90  \
    -v /home/julio/Desktop/todo-backend:/code \
    mini_api /bin/bash