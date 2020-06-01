# Flask API on Docker with PostgreSql 

**Dockerizing a REST API builded on Flask ! <br>This API provides endpoints to get random facts about one of my favourite games 🕹️ STREET FIGHTER II !**


## Features
- Docker
- Docker Compose
- Flask
- Gunicorn
- SQLAlchemy
- Postgres
- A website for API's documentation and usage, created with Nicepage and Docker (Nginx image)


**website**<br>
![website](images/website.png)

## Setup

Download this releases then build and run in Docker locally
```bash
git clone https://github.com/kenybapin/docker-flask-api.git
cd docker-flask-api
docker-compose up -d --build
```
## Getting started
Base URL for all endpoints
```bash
http://localhost:5000
```
Website URL
```bash
http://localhost:9000
```

### Possible Future Extensions
- Try factoring code and remove unused libraries.
- Add users on facts with auth (name, email, token)
- Display Facts dynamically on website (HTML/CSS/jQuery) ==> bring Pop-up text to each character.
