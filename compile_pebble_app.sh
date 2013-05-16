#!/bin/bash

claypellet_src_path="$(dirname $0)/claypellet"
includes="-I. -I./include -I./build -I./build/src -I${claypellet_src_path}"

./waf build

gcc -shared -std=c99 ${includes} -o build/claypellet_app.so ${claypellet_src_path}/claypellet.c src/*.c
