#include <stdio.h>

int main()
{
    double count = 0;
	double nxt = 1;
	double add = 0;
	double max_no = 0;
	printf("Please enter the maximum denominator value. = ");
	scanf("%lf", &max_no);
	while (nxt > 0.001){
	    nxt = 1/(count+1);
	    //printf("nxt=%lf \n", nxt);
	    add = add+nxt;
	    //printf("add=%lf \n", add);
	    count = count+1;
	    if (count >= max_no){
	        break;
	    }
	}
    if (nxt<=0.001){
        printf("The limit reached(The sum changed by 0.001)\n");
	}
	printf("The sum is = %lf ", add);

    return 0;
}

