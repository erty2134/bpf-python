import ctypes


# Ioctl's have the command encoded in the lower word, and the size of
# any in or out parameters in the upper word.  The high 3 bits of the
# upper word are used to encode the in/out status of the parameter.

IOCPARM_MASK: int = ctypes.c_uint32(0x1fff) # parameter length, at most 13 bits

def iocparm_len(x: int) -> ctypes.c_uint32:
    return ctypes.c_uint32(((x) >> 16) & IOCPARM_MASK)

def iocbasecmd(x) -> ctypes.c_uint32:
    return ctypes.c_uint32((x) & ~(IOCPARM_MASK << 16))

def iocgroup(x) -> ctypes.c_uint32:
    return ctypes.c_uint32(((x) >> 8) & 0xff)


IOCPARM_MAX: ctypes.c_uint32 = ctypes.c_uint32(IOCPARM_MASK.value + 1) # max size of ioctl args
# no parameters
IOC_VOID: ctypes.c_uint32 = ctypes.c_uint32(0x20000000)
# copy parameters out
IOC_OUT: ctypes.c_uint32 = ctypes.c_uint32(0x40000000)
# copy parameters in
IOC_IN: ctypes.c_uint32 = ctypes.c_uint32(0x80000000)
# mask for IN/OUT/VOID
IOC_INOUT = ctypes.c_uint32(IOC_IN.value|IOC_OUT.value)


def _ioc(inout, group, num, len) -> ctypes.c_uint32:
    return ctypes.c_uint32(inout | ((len & IOCPARM_MASK.value) << 16) | (ord(group) << 8) | (num))

def _io(g, n) -> ctypes.c_uint32:
    return _ioc(IOC_VOID, (g), (n), 0)

def _ior(g, n, t) -> ctypes.c_uint32:
    return _ioc(IOC_OUT, (g), (n), len(t)) # make sure to pack t with struct so len works

def _iow(g, n, t) -> ctypes.c_uint32:
    return _ioc(IOC_IN, (g), (n), len(t)) # make sure to pack t with struct so len works

# this should be _IORW, but stdio got there first # but we dont got stdlib but to keep it consisnent we going with _IOWR
def _iowr(g, n, t) -> ctypes.c_uint32:
    return _ioc(IOC_INOUT.value, (g), (n), ctypes.sizeof(t)) # make sure to pack t with struct so len works


def main():
    class ioctl_data(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_uint32)
        ]

    varible: ctypes.c_uint32 = _iowr('M', 1, ioctl_data);
    print(varible.value)

if __name__ == "__main__":
    main()