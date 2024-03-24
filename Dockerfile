FROM ubuntu:latest
LABEL authors="Robin"

ENTRYPOINT ["top", "-b"]