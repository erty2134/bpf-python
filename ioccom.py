import ctypes


# Ioctl's have the command encoded in the lower word, and the size of
# any in or out parameters in the upper word.  The high 3 bits of the
# upper word are used to encode the in/out status of the parameter.

IOCPARM_MASK: int = 0x1fff # parameter length, at most 13 bits

def iocparm_len(x: int) -> int:
    return (((x) >> 16) & IOCPARM_MASK)

def iocbasecmd(x) -> int:
    return ((x) & ~(IOCPARM_MASK << 16))

def iocgroup(x) -> int:
    return (((x) >> 8) & 0xff)


IOCPARM_MAX: int = (IOCPARM_MASK + 1) # max size of ioctl args
# no parameters
IOC_VOID: ctypes.c_uint32 = 0x20000000
# copy parameters out
IOC_OUT: ctypes.c_uint32 = 0x40000000
# copy parameters in
IOC_IN: ctypes.c_uint32 = 0x80000000
# mask for IN/OUT/VOID
IOC_INOUT = (IOC_IN|IOC_OUT)


def _ioc(inout, group, num, len):
    return (inout | ((len & IOCPARM_MASK) << 16) | ((group) << 8) | (num))

def _io(g, n):
    _ioc(IOC_VOID, (g), (n), 0)

def _ior(g, n, t):
    _ioc(IOC_OUT, (g), (n), len(t)) # make sure to pack t with struct so len works

def _iow(g, n, t):
    _ioc(IOC_IN, (g), (n), len(t)) # make sure to pack t with struct so len works

# this should be _IORW, but stdio got there first # but we dont got stdlib but to keep it consisnent we going with _IOWR
def _iowr(g, n, t):
    _ioc(IOC_INOUT,	(g), (n), len(t)) # make sure to pack t with struct so len works


def main():
    class ioctl_data(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_uint32)
        ]

    varible: ctypes.c_uint32 = _iowr('M', 1, ioctl_data);
    print(varible)

if __name__ == "__main__":
    main()