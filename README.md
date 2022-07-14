#Django_Tutorials_mini_project

Concept:

    - Create a basic Django app attached to a Postgres DB,
      and PGAdmin as the GUI to access the Postgres DB.

    - Create a .env file and utilize python-decouple from the 
      requirements.txt file to secure the DB's credentials 

    - Create an initial Dockerfile for the Django app

    - Dockerized all 3 elements using Docker Compose.

    - Setup Docker volumes to persist data.

    - Set 'depends-on' instructions for docker-compose.yml
      so the Postgres DB is created first

    - Edit Django's 'command' in docker-compose.yml to make migrations 
      when the container is created 

    - Utilize Insomnia to send API requests.