# multi-container
Requires: docker.io, docker-compose

REPOSITORY                   TAG         IMAGE ID       CREATED          SIZE
multi-container_flask        latest      a1a0b2153661   26 minutes ago   441MB
multi-container_nginx        latest      f5d0d9d4310c   5 hours ago      133MB

TODO:
Try distroless to further reduce size of the images

# Build the images
sudo docker-compose build

# Run the containers
sudo docker-compose up -d

# Stop the containers
sudo docker-compose down

# Log into the shell of the container
sudo docker exec -it <container ID> /bin/bash

# Clean up docker images repository
sudo docker image rm <image ID>
sudo docker system prune
