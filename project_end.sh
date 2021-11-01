#!/bin/bash

# we will be running this project at port 5600, so killing it using that port num
echo "Killing Project"
kill -9 $(lsof -ti:5600)