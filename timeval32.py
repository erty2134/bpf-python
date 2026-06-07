import ctypes

class timeval(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_int32),
        ("tv_usec", ctypes.c_int32)
    ]