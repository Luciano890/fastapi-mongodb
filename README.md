# REST API with FastAPI and Mongodb

## Conda

`
conda create -n fastapi-mongo python=3.9.5 -y
`
## Virtual Environment

`
(fastapi-mongo)$ pip install -r requirements.txt
`

## Docker command

`
docker run --name db-mongo -p 27017:27017 -d mongo:latest
`

## FastAPI

`
uvicorn app:app --reload
`