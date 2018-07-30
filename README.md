# TODO_BE
> This repo serves as backend service for todolists including dockerized service
Please use this repo with https://github.com/GhostFanta/TODO_FE

## Requirement

+ Python >= 3.5

## Run & Deploy
+ Run local instance: `flask run`(need database pre configured)
+ Run dockerized service(Ubuntu): 

>If your system do not contain docker and docker-compose, check:
https://docs.docker.com/compose/install/

```json
sudo su(password)
docker-compose build
docker-compose up
```
Check Init user
```
user: zichu@test1.com
password: 123456789
```

Due to uncertainty of network

## Release 1
Check PR: https://github.com/GhostFanta/TODO_BE/pull/7

## Release 2
Check PR: https://github.com/GhostFanta/TODO_BE/pull/10