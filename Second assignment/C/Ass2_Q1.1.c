#include<stdio.h>
#include <stdlib.h>
int main(){
	int arr[6]={1,2,3,4,5,6};
	int diff, i, j; 
	int sum = 0;
	float no, average;
	for (i = 0; i < 6; i++){
		for (j = 0; j < 6; j++){
			diff = abs(i - j);
			sum = sum + diff;
			no = no + 1;
		}
	}
	printf("Total distance = %d", sum);
	average = sum/no;
	printf("\nAverage distance = %f", average);
	return 0;
}
