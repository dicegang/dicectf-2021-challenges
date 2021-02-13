FROM redpwn/jail:sha-0a1cd30

COPY --from=gcr.io/distroless/base-debian10 / /app
COPY flag.txt /app/app/
COPY lost_in_your_eyes /app/app/challenge

ENV JAIL_WALL_TIME=5
