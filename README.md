# server-note
Service for saving notes to git


# Server notes

![Docker Pulls](https://img.shields.io/docker/pulls/djet/server_note?style=for-the-badge)

Service for saving notes to git

## Running this software

### Config file

```
LISTEN=0.0.0.0
PORT=8080
GIT_REPO_DIR=/data/git_repo
```

### Using the docker image
    docker run --rm -d -p 8080:8080 --name server_note -v $(pwd)/data/git_repo:/data/git_repo djet/server_note

### Using the docker compose

```
version: '3'

services:
  server_note:
    image: djet/server_note:latest
    volumes:
      - ./data/git_repo:/data/git_repo
    ports:
      - 8080:8080
    restart: always

```
## Building the software

### Building with Docker

After a successful local build:

    docker build -t server_note .

## Use example

```
data=$(bash example/hostinfo.sh | base64 -w0)
curl -X POST -F "base64=${data}" http://127.0.0.1:8080/docker/$(hostname)/hostinfo.md
```

[hub]: https://hub.docker.com/r/djet/server_note/