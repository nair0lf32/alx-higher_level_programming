#!/bin/bash
# Displays the size of the body of the response of a request to given url
curl -s "$1" | wc -c
