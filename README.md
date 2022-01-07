# Production
```
    $ sh build.sh
    $ sh start.sh
```

# Development
```
    $ sh build_dev.sh
    $ sh bind_dev.sh
    $ sh start_dev.sh
```

# End points

## Create Todo
```
    curl --location --request POST 'http://127.0.0.1:3000/todo' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id": null,
        "title": "{description}",
        "description": "{description}"
    }'
```

## Get all Todos
```
    curl --location --request GET 'http://127.0.0.1:3000/todo'
```

## Get Todo by Id
```
    curl --location --request GET 'http://127.0.0.1:3000/todo/{todo_id}'
```
    
## Delete Todo by Id
```
    curl --location --request DELETE 'http://127.0.0.1:3000/todo/{todo_id}'
```

## Update Todo by Id
```
    curl --location --request PUT 'http://127.0.0.1:3000/todo' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id": {todo_id},
        "title": "{title}",
        "description": "{description}"
    }'

```

