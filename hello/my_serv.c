/* File: sum_svc.c

Programmer: Mark Fienup

Date: January 21, 1998

Before compiling: rpcgen -N rsum.x and gcc -c rsum_xdr.c

"Compile" using: gcc -o sum_svc sum_svc.c rsum_svc.c rsum_xdr.o -lnsl

Description: This is a server program that provides two remote procedures:

"sum_two_1" takes two numbers and returns their sum, and

"max_two_1" takes two numbers and returns the string "first" if

the first number is >= to the second number; otherwise it returns

"second". */

#include <rpc/rpc.h>
#include "rsum.h"
long *sum_two_1(long op1, long op2, struct svc_req *cl) {
static long sum; /* Note that the return result must be "static" */
sum = op1 + op2;
return &sum;
}
char **max_two_1(long op1, long op2, struct svc_req *cl)
{
static char *max_str;
if (op1 > op2) {
max_str = "first";
} else {
max_str = "second";
} /* end if */
return &max_str;
}
