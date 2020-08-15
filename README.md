# Django URL Shortner
A simple url shortner

## How to Run


### Development
To run in development env:
1. Install Docker https://www.docker.com/products/docker-desktop
2. Make .env file in same directory as `docker-compose.yml` or edit the `.env` path in it. Refer `env_sample` file.
3. From the root directory of app execute `docker-compose up` or `docker-compose up -d` to run as daemon. Docker will pull and build the image first time and execute the containers.
4. Open `http://127.0.0.1/` to see things in action.


#### Super user
1. To create super used make sure the docker containers are running.
2. Login to docker machine of application 'docker-compose exec app sh'
3. Navigate to application directory in VM. `cd ./application`
4. execute `./manage.py createsuperuser`
