FROM redpwn/jail:sha-0a1cd30

COPY --from=ubuntu:20.04 / /app
COPY flag.txt /app/app/flag.txt
COPY babyrop /app/app/challenge
