/* date.x - Specification of remote date and time service
bindate() which returns the binary time and date (no args).
This file is the input to rpcgen */
struct add_arg {
	int first;
	int second;
};
struct sub_arg {
	int first;
	int second;
};
struct mul_arg {
	int first;
	int second;
};
struct div_arg {
	int first;
	int second;
};
program RSUM_PROG { /* remote program name (not used)*/
version RSUM_VERS { /* declaration of program version
number*/
long BINDATE(void) = 1; /* procedure number = 1 */
long ADDER(add_arg) = 2; /* procedure number = 2*/
long SUBER(sub_arg) = 3; /* procedure number = 3*/
long MULER(mul_arg) = 4; /* procedure number = 4*/
long DIVER(div_arg) = 5; /* procedure number = 5*/
} = 1; /* definition of program version =
1*/
} = 0x3012225; /* remote program number (must be
unique)*/
