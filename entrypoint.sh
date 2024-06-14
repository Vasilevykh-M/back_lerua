#!/bin/sh

# Launch nginx
nginx &

# Launch app
fastapi run /code/app/main.py --port 8500