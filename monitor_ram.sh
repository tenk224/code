#!/bin/bash

while true;
do
	free -m | grep "Mem" | awk '{print $3}' >> ram.csv
	sleep 1
done
