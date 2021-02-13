FROM gcr.io/distroless/base-debian10

COPY server handler flag.txt /app/

WORKDIR /app/
ENTRYPOINT ["/app/server"]
EXPOSE 31337
