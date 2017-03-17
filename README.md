# docker-taiga
A clean and portable Taiga instance, housed with docker-compose.

# Features
* Run taiga, dockerized
* Easily update both taiga-back and taiga-front

# Usage
1. (optional) Build the frontend and backend images using their respective build.sh scripts.
  Otherwise the images will be pulled from the docker repository and cannot be guaranteed up-to-date.
2. Create a .env file to set the variables listed in docker-compose.yml
3. Use
  `docker-compose up`
  and normal docker-compose commands to control the Taiga instance
