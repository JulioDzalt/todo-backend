# Development

docker run -it --name mini_api_container -p 90:90  \
    -v /home/julio/Desktop/todo-backend:/code \
    mini_api /bin/bash

docker run \
  -it \
  --name daten --rm \
  -p 5014:5014 --net gepp \
  -v /home/ermiry/Documents/Work/gepp/gepp-daten:/home/daten \
  -v /home/ermiry/Documents/Work/gepp/gepp-daten/uploads:/home/daten/uploads \
  -v /home/ermiry/Documents/Work/gepp/keys:/home/daten/keys \
  -e RUNTIME=development \
  -e PORT=5014 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  -e MONGO_APP_NAME=daten -e MONGO_DB=gepp \
  -e MONGO_URI=mongodb://daten:password@192.168.100.39:27017/gepp \
  -e PUB_KEY=/home/daten/keys/key.pub \
  itpercepthor/gepp-daten:development /bin/bash