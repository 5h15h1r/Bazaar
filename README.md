## Bazaar
A marketplace website written in djanggo and postgreSQL

### Run Locally
1. Set up an .env file by reffering to .env.example
2. `docker compose -f docker-compose.yml up --build`
3. Apply migrations with following commands:
    ```bash
        docker compose exec web python3 manage.py makemigrations
        docker compose exec web python3 manage.py migrate
    ```