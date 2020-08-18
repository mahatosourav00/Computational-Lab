#include<stdio.h>
int main(){
	int A[3]={2, 3, 4};
	int B[3]={5, 6, 7};
	int sum[3];
	int i, j, add = 0;
	printf("Two verctors are A = { ");
	for(j = 0; j < 3; j++){
		printf("%d, ", A[j]);
	}
	printf(" } and B = { ");
	for(j = 0; j < 3; j++){
		printf("%d, ", B[j]);
	}
	printf(" } \n");
	//A+B
	for(i = 0; i < 3; i++){
		sum[i] = A[i] + B[i];
	}
	printf("Vector sum = { ");
	for(j = 0; j < 3; j++){
		printf("%d, ", sum[j]);
	}
	printf(" } \n");
	//dot product
	for(i = 0; i<3; i++){
		int multiply = A[i] * B[i];
		add = multiply + add;
	}
	printf("Dot product is = %d", add);
	return 0;
}
