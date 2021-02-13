FROM python:3-slim

RUN pip3 install numpy pycryptodome

WORKDIR /ctf
COPY lwe.py shake.py server.py public.key flag.txt ./

EXPOSE 3000

CMD ["python3", "server.py"]
