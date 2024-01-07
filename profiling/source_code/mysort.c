#define _POSIX_C_SOURCE 199309L

#include <inttypes.h>
#include <memory.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

#ifndef NMAX
#error NO NMAX
#endif

#define BAD_ALEN 1
#define BAD_ARR 2

typedef int arr_t[NMAX];

int swap(void *pl, void *pr, size_t size)
{
    char buf[size];

    memcpy(buf, pl, size);
    memcpy(pl, pr, size);
    memcpy(pr, buf, size);

    return EXIT_SUCCESS;
}

size_t arr_scan(arr_t a, size_t alen)
{
    for (size_t i = 0; i < alen; ++i)
    {
        if (scanf("%d", &a[i]) != 1)
            return i;
    }
    return alen;
}

void mysort(
void *base, size_t num, size_t size, int (*compare)(const void *, const void *))
{
    // clang-format on
    void *buf = calloc(1, size);

    if (buf == NULL)
        return;

    char *cbase = (char *)base;

    for (size_t i = 0; i < num; ++i)
    {
        memcpy(buf, base, size);
        size_t max_offset = 0;

        for (char *pcur = cbase; (pcur - cbase) / size < num - i; pcur += size)
            if (compare(pcur, buf) > 0)
            {
                max_offset = (pcur - cbase);
                memcpy(buf, pcur, size);
            }

        swap(cbase + size * (num - i - 1), cbase + max_offset, size);
    }

    free(buf);
}

long delta_time(struct timespec mt1, struct timespec mt2)
{
    return 1000000000 * (mt2.tv_sec - mt1.tv_sec) + (mt2.tv_nsec - mt1.tv_nsec);
}

int int_cmp(const void *pl, const void *pr)
{
    int *pil = (int *)pl;
    int *pir = (int *)pr;

    return *pil - *pir;
}

int main(void)
{
    arr_t a;
    struct timespec begin, end;
    size_t alen = 0, tmp;

    if (scanf("%zu", &alen) != 1)
        return BAD_ALEN;
    tmp = arr_scan(a, alen);
    if (alen != tmp)
        return BAD_ARR;

    clock_gettime(CLOCK_REALTIME, &begin);

    mysort(a, alen, sizeof(int), int_cmp);

    clock_gettime(CLOCK_REALTIME, &end);

    int tmpvar = a[0];
    a[alen - alen / 2] = tmpvar;

    printf("%zu %lu\n", alen, delta_time(begin, end));

    return EXIT_SUCCESS;
}
