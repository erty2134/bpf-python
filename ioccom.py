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


def ioc(inout, group, num, len) -> ctypes.c_uint32:
    return ctypes.c_uint32(inout.value | ((len & IOCPARM_MASK.value) << 16) | (ord(group) << 8) | (num))

def io(g, n) -> ctypes.c_uint32:
    return ioc(IOC_VOID, (g), (n), 0)

def ior(g, n, t) -> ctypes.c_uint32:
    return ioc(IOC_OUT, (g), (n), ctypes.sizeof(t))

def iow(g, n, t) -> ctypes.c_uint32:
    return ioc(IOC_IN, (g), (n), ctypes.sizeof(t))

# this should be _IORW, but stdio got there first # but we dont got stdlib but to keep it consisnent we going with _IOWR
def iowr(g, n, t) -> ctypes.c_uint32:
    return ioc(IOC_INOUT, (g), (n), ctypes.sizeof(t))


def main():
    class ioctl_data(ctypes.Structure):
        _fields_ = [
            ("x", ctypes.c_uint32)
        ]

    iowr_test: ctypes.c_uint32 = iowr('M', 1, ioctl_data);
    print("iowr_test",iowr_test.value)

    io_test = io('M',2)
    print("io_test",io_test.value)
    
    ior_test = ior('M',2,ioctl_data)
    print("ior_test",ior_test.value)

    iow_test = iow('M',2,ioctl_data)
    print("iow_test",iow_test.value)


if __name__ == "__main__":
    main()