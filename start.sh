#!/bin/sh
docker build -t interview_doc -f Dockerfile .
docker run -it -p 80:8888 interview_doc

