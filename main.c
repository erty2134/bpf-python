#include <stdlib.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <inttypes.h>

struct ioctl_data{
    __uint32_t x;
};

int main(){
    __uint32_t iowrTest = _IOWR('M', 1, struct ioctl_data);
    printf("iowrTest %u\n", iowrTest);

    __uint32_t ioTest = _IO('M',2);
    printf("ioTest %u\n", ioTest);

    __uint32_t iorTest = _IOR('M',2,struct ioctl_data);
    printf("iorTest %u\n", iorTest);
    
    __uint32_t iowTest = _IOW('M',2,struct ioctl_data);
    printf("iowTest %u\n", iowTest);
    
    return 0;
}