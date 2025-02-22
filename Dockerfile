FROM ubuntu:latest
LABEL authors="relapt"

ENTRYPOINT ["top", "-b"]