# TODO_BE
> This repo serves as Todolist backend for DashHudson interview.
Please use this repo with https://github.com/GhostFanta/TODO_FE

### Run & Deploy
+ Project setup: `pip install -r requirements.txt`

+ Run local instance for development : `bash ${PROJECT_DIR}/boot.sh`

+ Run test: ``

### Structure Introduction:
```json
core/
├── api.py              // API entry points
└── requestparser.py    // Parser for prasing https request params and post body
dao/
├── __init__.py
├── model.py            // Define database models
├── operation.py        // Define sql operations
./helper/
├── seed.py             // Seed data for database migration
└── sqlhelper.py        // Response parser(legacy)
deploy.sh
Dockerfile              // Script for dockerize backend service
wsgi.py                 // wsgi configuration for gunicorn 
```