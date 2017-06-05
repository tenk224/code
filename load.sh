#!/bin/bash

SECONDS=0

export PATH=$PATH:/usr/lib/openmpi/bin

rm -f cpu.csv
rm -f ram.csv

./monitor_cpu.sh &
./monitor_ram.sh &

t=5
t=$(( t+0 ))

mpirun --allow-run-as-root -np 4 ./qs.o 7000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 3000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 1 ./qs.o 1000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 6000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 2 ./qs.o 5000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 2 ./qs.o 3000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 1 ./qs.o 6000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 4 ./qs.o 2000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 9000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 2 ./qs.o 1000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 6000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 4 ./qs.o 8000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 1 ./qs.o 9000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 4 ./qs.o 9000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 1 ./qs.o 4000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 4 ./qs.o 9000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 1 ./qs.o 1000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 3000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 6000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 3000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 9000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 3 ./qs.o 6000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 2 ./qs.o 1000000 > /dev/null &
sleep $t
mpirun --allow-run-as-root -np 2 ./qs.o 7000000 > /dev/null &
sleep $t
sleep $t
sleep $t
sleep $t


#kill monitor
kill $(ps -ef | grep "monitor_cpu.sh" | grep "/bin/bash" | awk '{print $2}'+0) > /dev/null &
kill $(ps -ef | grep "monitor_ram.sh" | grep "/bin/bash" | awk '{print $2}'+0) > /dev/null &

echo $SECONDS

