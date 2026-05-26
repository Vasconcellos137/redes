#!/bin/bash

# for i in 1 2 3 4 5 
#     do
#         echo Nick: $i
#         sleep 1s
#     done

# $ -> parâmetros q passamos p dentro do script
# se n tiver esse echo... abaixo, n é possivel passar outros parâmetros 

# echo $0 $1 $2 
# for i in $(seq 5) 
#     do
#         echo Nick: $i
#         sleep 1s
#     done


for i in $(seq $1 | tac ) 
    do
        echo Nick: $i
        sleep 1s
    done