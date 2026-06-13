import sys
import bpf
import os
import errno
import fcntl
import ctypes
import types


def is_sudo() -> bool:
    if os.geteuid() == 0:
        return True
    return False


def open_bpf() -> int:
    fd: int | None = None
    for i in range(0,256):
        try:
            fd = os.open(f"/dev/bpf{i}", os.O_RDWR)
        except OSError as e:
            if e.errno == errno.EBUSY:
                continue
            raise e
    if fd == None:
        pass # maybe a warning or something later on?
    return fd


def main() -> int:
    if not is_sudo():
        sys.stderr.write("Sudo required!\n")
        return 1
    
    device = open_bpf()
    if device == None:
        sys.stderr.write("No BPF devices available!\n")
        return 1

    ifr: bpf.ifreq = bpf.ifreq()
    ifr.ifr_name = b"en0"

    fcntl.ioctl(device, bpf.BIOCSETIF, ifr, True)

    buf_len: ctypes.c_int = ctypes.c_uint(1)

    fcntl.ioctl(device, bpf.BIOCIMMEDIATE, buf_len, True)
    fcntl.ioctl(device, bpf.BIOCGBLEN, buf_len, True)

    # do something

    os.close(device)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())