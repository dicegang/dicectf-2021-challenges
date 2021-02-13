FROM busybox AS wasmtime

WORKDIR /
RUN wget -O - https://github.com/bytecodealliance/wasmtime/releases/download/v0.22.1/wasmtime-v0.22.1-x86_64-linux.tar.xz \
	| tar -xJ wasmtime-v0.22.1-x86_64-linux/wasmtime

FROM redpwn/jail:sha-0a1cd30

COPY --from=debian:10-slim / /app
COPY --from=wasmtime /wasmtime-v0.22.1-x86_64-linux/wasmtime /app/usr/bin/wasmtime
COPY start.sh /app/app/challenge
RUN mkdir /app/app/cache
COPY wasmpwn.wasm config.toml /app/app/
COPY excalibur.txt flag.txt /app/app/data/
ENV JAIL_MEM 20971520
