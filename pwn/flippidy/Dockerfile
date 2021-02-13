FROM redpwn/jail:sha-0a1cd30

COPY --from=ubuntu@sha256:c32bd2e76e7688eeb1bb39754fff7cdfc571626fc1abfded4f82a90de79f8d10 / /app
COPY flag.txt /app/app/flag.txt
COPY flippidy /app/app/challenge
