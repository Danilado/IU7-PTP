#define _POSIX_C_SOURCE 199309L

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <x86gprintrin.h>

unsigned long timeofday_ms_now()
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
    {
        return (unsigned long long)-1;
    }
    return val.tv_sec * 1000ULL + val.tv_usec / 1000ULL;
}

int main(void)
{
    long times[4] = {1000, 500, 100, 10};

    for (size_t i = 0; i < 4; ++i)
    {
        struct timespec remaining,
            request = {times[i] / 1000, times[i] % 1000 * 1000000};
        printf("%ld ", times[i]);

        unsigned long ms1;
        unsigned long ms2;

        ms1 = clock_gettime();
        nanosleep(&request, &remaining);
        ms2 = clock_gettime();

        printf("%lu\n", (ms2 - ms1));
    }

    return EXIT_SUCCESS;
}
