## Adding new packages
```bash
    docker-compose run web pip install [name of project]
    docker-compose run web pip freeze > requirements.txt
```

## Spinning up packages (locally)
To watch the logs
```bash
    docker-compose up
```

To spin it up in the background:
```bash
    docker-compose up -d
```

spinning up a single service:
```bash
    docker-compose up [service name] # E.G.: docker-compose up web
```

## Migrating your local database
```bash
    docker-compose run web python manage.py migrate
```