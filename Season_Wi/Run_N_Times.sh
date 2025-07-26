#!/bin/bash

Season="${PWD##*/}"
Flag=0

while [ "$Flag" -eq 0 ]; do
    read -p "Numero de Bucles: " input_value
    read -p "Offset: " offset
    if ! [[ "$input_value" =~ ^[0-9]+$ ]] || ! [[ "$offset" =~ ^[0-9]+$ ]]; then
        echo "Solo Enteros"
    else
        Flag=1
    fi
done

for ((i = 1; i <= input_value; i++)); do
    index=$((i + offset))
    for region in {1..4}; do
        exe_dir="./${Season}_Region_${region}/${Season}_Region_${region}_Gibbs_Sampling"
        exe_name="${Season}_r${region}E4gs"
        (
            cd "$exe_dir" || exit
            ./"$exe_name" "$index" &
        )
    done
done

wait  # Wait for all background processes to finish
