# Docker

```bash
docker logs {name}
# List process (containers)
docker ps
# Go inside container
docker exec -it {name} ash
#build image
docker build -t {name} .
# Run image
docker run -it --name {name_image} -p {port_ecoute}:{port_expose} {name}
# Stop container
docker stop {name}
```
