import dis, marshal, struct, sys, time, types
from opcode import *

def ana_branch(code, i, hits):
    if i > len(code):
        return
    if i in hits:
        return
    else:
        hits.append(i)
    c = code[i]
    op = ord(c)
    if op == 111 or op == 112 or op == 114 or op == 115 or op == 120 or op == 93:
        oparg = ord(code[i+1]) + ord(code[i+2])*256
        if op == 120 or op == 93:
            oparg += i
            oparg += 3
        ana_branch(code, oparg, hits)
        ana_branch(code, i+3, hits)
    elif op == 110:
        oparg = ord(code[i+1]) + ord(code[i+2])*256
        ana_branch(code, i + oparg + 3, hits)
    elif op == 113:
        oparg = ord(code[i+1]) + ord(code[i+2])*256
        ana_branch(code, oparg, hits)
    else:
        if op>=HAVE_ARGUMENT:
            ana_branch(code, i+3, hits)
        else:
            ana_branch(code, i+1, hits)

def findlinestarts(code):
    """Find the offsets in a byte code which are start of lines in the source.

    Generate pairs (offset, lineno) as described in Python/compile.c.

    """
    byte_increments = [ord(c) for c in code.co_lnotab[0::2]]
    line_increments = [ord(c) for c in code.co_lnotab[1::2]]

    lastlineno = None
    lineno = code.co_firstlineno
    addr = 0
    for byte_incr, line_incr in zip(byte_increments, line_increments):
        if byte_incr:
            if lineno != lastlineno:
                yield (addr, lineno)
                lastlineno = lineno
            addr += byte_incr
        lineno += line_incr
    if lineno != lastlineno:
        yield (addr, lineno)

def findhits(code):
    hits = []
    n = len(code)
    i = 0
    ana_branch(code, i, hits)
    hits.sort()
    return hits

def anti_findlabels(code):
    """Detect all offsets in a byte code which are jump targets.
    Return the list of offsets.
    """
    hits = findhits(code)
    labels = []
    n = len(code)
    i = 0
    while i < n:
        if i not in hits:
            i+=1
            continue
        c = code[i]
        op = ord(c)
        i = i+1
        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i+1])*256
            i = i+2
            label = -1
            if op in hasjrel:
                label = i+oparg
            elif op in hasjabs:
                label = oparg
            if label >= 0:
                if label not in labels:
                    labels.append(label)
    return labels

def dis_anti_obf(co, lasti = -1):
    """Disassemble a code object, anti obf"""
    anti_code = ""
    code = co.co_code
    hits = findhits(code)
    labels = anti_findlabels(code)
    linestarts = dict(findlinestarts(co))
    n = len(code)
    i = 0
    i = 0
    extended_arg = 0
    free = None
    while i < n:
        if i not in hits:
            i+=1
            anti_code+="\x09"
            continue
        c = code[i]
        op = ord(c)
        if i in linestarts:
            if i > 0:
                print
            print "%3d" % linestarts[i],
        else:
            print '   ',
        
        if i == lasti: print '-->',
        else: print '   ',
        if i in labels: print '>>',
        else: print '  ',
        print repr(i).rjust(4),
        print opname[op].ljust(20),
        anti_code += code[i]
        i = i+1
        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i]) + ord(code[i+1])*256 + extended_arg
            extended_arg = 0
            anti_code+=code[i]
            anti_code+=code[i+1]
            i = i+2
            if op == EXTENDED_ARG:
                extended_arg = oparg*65536L
            print repr(oparg).rjust(5),
            if op in hasconst:
                print '(' + repr(co.co_consts[oparg]) + ')',
            elif op in hasname:
                print '(' + co.co_names[oparg] + ')',
            elif op in hasjrel:
                print '(to ' + repr(i + oparg) + ')',
            elif op in haslocal:
                print '(' + co.co_varnames[oparg] + ')',
            elif op in hascompare:
                print '(' + cmp_op[oparg] + ')',
            elif op in hasfree:
                if free is None:
                    free = co.co_cellvars + co.co_freevars
                print '(' + free[oparg] + ')',
        print
    print "patch code:"
    print(anti_code.encode("hex"))




def show_file(fname):
    f = open(fname, "rb")
    magic = f.read(4)
    moddate = f.read(4)
    modtime = time.asctime(time.localtime(struct.unpack('L', moddate)[0]))
    print "magic %s" % (magic.encode('hex'))
    print "moddate %s (%s)" % (moddate.encode('hex'), modtime)
    code = marshal.load(f)
    show_code(code)
     
def show_code(code, indent=''):
    print "%scode" % indent
    indent += '   '
    print "%sargcount %d" % (indent, code.co_argcount)
    print "%snlocals %d" % (indent, code.co_nlocals)
    print "%sstacksize %d" % (indent, code.co_stacksize)
    print "%sflags %04x" % (indent, code.co_flags)
    show_hex("code", code.co_code, indent=indent)
    dis_anti_obf(code)
    print "%sconsts" % indent
    for const in code.co_consts:
        if type(const) == types.CodeType:
            show_code(const, indent+'   ')
        else:
            print "   %s%r" % (indent, const)
    print "%snames %r" % (indent, code.co_names)
    print "%svarnames %r" % (indent, code.co_varnames)
    print "%sfreevars %r" % (indent, code.co_freevars)
    print "%scellvars %r" % (indent, code.co_cellvars)
    print "%sfilename %r" % (indent, code.co_filename)
    print "%sname %r" % (indent, code.co_name)
    print "%sfirstlineno %d" % (indent, code.co_firstlineno)
    show_hex("lnotab", code.co_lnotab, indent=indent)
     
def show_hex(label, h, indent):
    h = h.encode('hex')
    if len(h) < 60:
        print "%s%s %s" % (indent, label, h)
    else:
        print "%s%s" % (indent, label)
        for i in range(0, len(h), 60):
            print "%s   %s" % (indent, h[i:i+60])

show_file(sys.argv[1])