#include <stdlib.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <inttypes.h>

struct ioctl_data{
    __uint32_t x;
};

int main(){
    __uint32_t varible = _IOWR('M', 1, struct ioctl_data);
    printf("%u\n", varible);
    return 0;
}