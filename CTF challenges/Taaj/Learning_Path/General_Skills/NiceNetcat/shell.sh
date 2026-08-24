#!/bin/bash

HOST="wily-courier.picoctf.net"
PORT="56418"

nc "$HOST" "$PORT" | while read -r decimal; do
    printf "\\$(printf '%03o' "$decimal")"
done
printf '\n'