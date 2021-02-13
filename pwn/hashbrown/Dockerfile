FROM ubuntu:20.04 as runtime

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        qemu-system-x86 hashcash \
    && rm -rf /var/lib/apt/lists/*

FROM redpwn/jail:sha-0a1cd30

COPY --from=runtime / /app
COPY jail-hook.sh /jail/hook.sh
COPY initramfs.cpio bzImage run.sh /app/app/
COPY pow.sh /app/app/challenge

ENV JAIL_KEEP_ENV=true
ENV JAIL_WALL_TIME=600
ENV JAIL_CONNS_PER_IP=5
ENV JAIL_MEM=218103808
ENV JAIL_CPU=700
ENV JAIL_PIDS=7
