#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
#include <inttypes.h>
#include <net/bpf.h>
#include <net/if.h>

struct ioctl_data{
    __uint32_t x;
};

int main(){
    /*
    printf("%lu\n", sizeof(struct ifreq));

    __uint32_t iowrTest = _IOWR('M', 1, struct ioctl_data);
    printf("iowrTest %u\n", iowrTest);

    __uint32_t ioTest = _IO('M',2);
    printf("ioTest %u\n", ioTest);

    __uint32_t iorTest = _IOR('M',2,struct ioctl_data);
    printf("iorTest %u\n", iorTest);
    
    __uint32_t iowTest = _IOW('M',2,struct ioctl_data);
    printf("iowTest %u\n", iowTest);
    
    printf("\n\n");
    struct ifreq ifr;
    strcpy(ifr.ifr_name, "en0");
    printf("size of ifreq: %lu\n", sizeof(ifr));
    printf("size of ifreq ifr_ifru: %lu\n", sizeof(ifr.ifr_ifru));
    */
    printf("%lu\n", BIOCSRTIMEOUT);
    printf("%zu\n", sizeof(struct timeval));
    printf("%zu\n", sizeof(struct timeval32));
    //printf("%d\n%d\nBIOCSETF\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n",BIOCGBLEN,BIOCSBLEN,BIOCFLUSH,BIOCPROMISC,BIOCGDLT,BIOCGETIF,BIOCSETIF,BIOCSRTIMEOUT,BIOCGRTIMEOUT,BIOCGSTATS,BIOCIMMEDIATE,BIOCVERSION,BIOCGRSIG,BIOCSRSIG,BIOCGHDRCMPLT,BIOCSHDRCMPLT,BIOCGSEESENT,BIOCSSEESENT,BIOCSDLT,BIOCGDLTLIST,BIOCSETFNR);
    return 0;
}