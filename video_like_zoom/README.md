# Jina video chat

## Prerequisites

First, you need a webcam.

## Run server

Server doesn't need a webcam of course.

```shell
pip install -U jina
jina flow --uses flow.yml
```

## Run client

```shell
pip install opencv-python
pip install -U jina docarray
python3 client.py grpcs://your-server-address-from-last-image yourusername
```
