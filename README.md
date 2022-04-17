# Clients Products Wishlist

## Quick install with docker-compose (Dockerized Enviroment)
The fastast way to get started is by build and running the docker container with **<a href="https://docs.docker.com/compose/install/">docker-compose</a>**.
>$ docker-compose up

This is pull the base images for the backend and the database, as well build the python eviroment used by the backend.

## Local Enviroment Alternative
If you don't want to use a dockerized enviroment, you may as well do it manually by following the steps:

<ol>
<li>
    Move to the <b>app</b> directory
</li>

<li>
    Create a <a href="https://docs.python.org/3/tutorial/venv.html">python  enviroment</a> for the backend <a href="https://fastapi.tiangolo.com/">FastAPI</a> app
</li>

<li>
    Install the packages in <code>requirements.txt</code> file, eg:

    $ pip install -r requirements.txt

</li>

<li>
    Run the server with the following command

    $ uvicorn main:app --reload --host '0.0.0.0' --port 8000

For VSCode users, you may instead run launch it with the debugger **Python: FastAPI Local Debugger** option located in the <code>.vscode/launch.json</code> file
</li>

<li>
    You will also need a PostgreSQL server set up, you can either run it locally or with docker, just <b>don't forget to update the connection url in the <code>.env</code> file  in the project root directory !!!</b> to adept your enviroment
</li>
</ol>


## API Documentation
Once running, you may access the Swagger interactive API documentation in the following url:
> <a href="http://localhost:8000/docs">http://localhost:8000/docs<a/>


## Creating a user
To create a user, do a POST request to following endpoint like the example:
> curl -X 'POST' \
  'http://localhost:8000/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "user@example.com",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false,
  "first_name": "string",
  "last_name": "string"
}

You may use any tool that fits you best for this (eg. Postman, Insommina, ThunderClient and so on). There is also the possiblity to use interactive API Docs for this (and any other request), just click the <b>Try it Out</b> button and fill the desired payload.

If you are going with Postman like applications, you can download the OpenAPI Specification JSON file and import the collection (saves time!)
> <a href="http://localhost:8000//openapi.json">http://localhost:8000/openapi.json</a>

#### Note
To create a super user, for now, the `is_superuser` property must be set to **True** manually with and SQL statement.


## Project Disclaimer
This is my very first FastAPI project, and I haven't had a lot of time lately. I spent a lot of time integrating the services and making the enviroment friendly to use. As a result there are some point that still needs improvement.
<ul>
<li>There is no tool to store/encrypt sensitive data - eg. the JWT Secret in the env file</li>
<li>When running the docker, there isn't an easy way to run alembic for migration management, for now it is necessary to run it within the backend container </li>
<li>There are no integration tests yet</li>
</ul>