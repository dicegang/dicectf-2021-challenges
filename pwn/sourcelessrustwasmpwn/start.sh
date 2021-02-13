#!/bin/sh
cd data && exec /usr/bin/wasmtime run --config ../config.toml ../wasmpwn.wasm --dir ./
