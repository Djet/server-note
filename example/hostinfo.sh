#!/bin/bash
echo -e "Host:" 
hostname
echo "Interface:"
ip a
echo "Route"
ip r
echo "Docker info"
docker ps
