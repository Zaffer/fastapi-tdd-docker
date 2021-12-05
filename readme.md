# Dev

`uvicorn app.main:app --reload`


# Build

`docker-compose build`


# Run

`docker-compose up -d`


# Database

`docker-compose exec web-db psql -U postgres`
`\c web_dev`
`\q`