# adapted from https://nedbatchelder.com/blog/200804/the_structure_of_pyc_files.html

import binascii
import dis
import marshal
import sys
import time
import types


def get_long(s):
    return s[0] + (s[1] << 8) + (s[2] << 16) + (s[3] << 24)


def show_hex(label, h, indent):
    h = binascii.hexlify(h).decode('ascii')
    if len(h) < 60:
        print('%s%s %s' % (indent, label, h))
    else:
        print('%s%s' % (indent, label))
        for i in range(0, len(h), 60):
            print('%s   %s' % (indent, h[i:i+60]))


def show_code(code, indent=''):
    print('%scode' % indent)
    indent += '   '
    print('%sargcount %d' % (indent, code.co_argcount))
    print('%snlocals %d' % (indent, code.co_nlocals))
    print('%sstacksize %d' % (indent, code.co_stacksize))
    print('%sflags %04x' % (indent, code.co_flags))
    show_hex('code', code.co_code, indent=indent)
    dis.dis(code.co_code)
    print('%sconsts' % indent)
    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            show_code(const, indent+'   ')
        else:
            print('   %s%r' % (indent, const))
    print('%snames %r' % (indent, code.co_names))
    print('%svarnames %r' % (indent, code.co_varnames))
    print('%sfreevars %r' % (indent, code.co_freevars))
    print('%scellvars %r' % (indent, code.co_cellvars))
    print('%sfilename %r' % (indent, code.co_filename))
    print('%sname %r' % (indent, code.co_name))
    print('%sfirstlineno %d' % (indent, code.co_firstlineno))
    show_hex('lnotab', code.co_lnotab, indent=indent)
    exec(code)


def show_file(fname: str) -> None:
    with open(fname, 'rb') as f:
        magic_str = f.read(4)
        mtime_str = f.read(4)
        mtime = get_long(mtime_str)
        modtime = time.asctime(time.localtime(mtime))
        print('magic %s' % binascii.hexlify(magic_str))
        print('moddate %s (%s)' % (binascii.hexlify(mtime_str), modtime))
        if sys.version_info < (3, 3):
            print('source_size: (unknown)')
        else:
            source_size = get_long(f.read(4))
            print('source_size: %s' % source_size)
        f.read(4)
        show_code(marshal.loads(f.read()))


if __name__ == '__main__':
    show_file(sys.argv[1])
