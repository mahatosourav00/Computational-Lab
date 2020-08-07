#include <stdio.h>

int main()
{
    int count = 0;
	double multiply = 1;
	int integer;
	printf("Enter the integer for which you want calculate factorial = ");
	scanf("%d", &integer);
	int backup = integer;
	if(integer < 0){
	    while(integer < 0){
		    printf("The integer must be > or = to 0");
	    	scanf("%d", &integer);
	    }
	}
	
	while(integer>0){
		multiply = multiply*integer;
		integer = integer-1;
	}
	printf("The factorial of %d is = %lf", backup, multiply);

    return 0;
}
