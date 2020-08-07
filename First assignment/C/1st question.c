
#include <stdio.h>

int main()
{
    int count = 0;
	int add = 0;
	int max_no;
	printf("Please enter the max integer(< or = to 100) till you want to add = ");
	scanf("%d", &max_no);
	while (max_no > 100){
        printf("The integer have to be less than 100 = ");
        scanf("%d", &max_no);
	}
	while(count < max_no){
	    count = count + 1;
	    add = add + count;
	}
	printf("The sum of integers till %d = %d", max_no, add);

    return 0;
}
