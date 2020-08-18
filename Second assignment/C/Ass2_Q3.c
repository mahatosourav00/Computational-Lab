#include<stdio.h>
int main(){
	int N[3][3], M[3][3], sum, i, j, k;
	FILE *m, *n;
	m = fopen("MatrixM.txt", "r");
	n = fopen("MatrixN.txt", "r");
	if(m == NULL){
		printf("Error openning Matrix1");
		return 1;
	}
	if(n == NULL){
		printf("Error openning Matrix2");
		return 1;
	}
	//read MatrixM
	printf("M= \n");
	for(i = 0; i < 3; i++){
		for(j = 0; j < 3; j++){
			fscanf(m, " %d ", &M[i][j]);
			printf(" %d ", M[i][j]);
		}
		printf("\n");
	}  
	//read MatrixN
	printf("\nN= \n");
	for(i = 0; i < 3; i++){
		for(j = 0; j < 3; j++){
			fscanf(n, " %d ", &N[i][j]);
			printf(" %d ", N[i][j]);
		}
		printf("\n");
	}
	//define matrixA
	int A[3][2] = {
	    {14, 18},
	    {12, 36},
	    {21, 32}
	    };
	printf("\nA= \n");
	for(i = 0; i < 3; i++){
		for(j = 0; j < 2; j++){
			printf(" %d ", A[i][j]);
		}
		printf("\n");
	}
	//M*A
	    //define matrixMA = M*A
	int MA[3][2]={
	    {0, 0},
	    {0, 0},
	    {0, 0}
	};
	
	printf("\nM*A= \n");
	for(i = 0; i < 3; i++){
	    for(j = 0; j < 2; j++){
	    	sum = 0;
	        for(k = 0; k < 3; k++){
	            int multiply = M[i][k]*A[k][j];
	            //printf(" %d + ", multiply);
	            sum = sum + multiply;  
	        }
	        //printf("= %d   ", sum);
	        MA[i][j] = sum;
	        printf(" %d ", MA[i][j]);
	    }
	    printf("\n");
	}
	
	//M*N
		//define matrixMA = M*A
	int MN[3][2]={
	    {0, 0},
	    {0, 0},
	    {0, 0}
	};
	printf("\nM*N= \n");
	for(i = 0; i < 3; i++){
	    for(j = 0; j < 3; j++){
	    	sum = 0;
	        for(k = 0; k < 3; k++){
	            int multiply = M[i][k]*N[k][j];
	            //printf(" %d + ", multiply);
	            sum = sum + multiply;  
	        }
	       // printf("= %d   ", sum);
	        MN[i][j] = sum;
	        //printf("%d,%d ", i, j);
	        printf(" %d ", MN[i][j]);
	    }
	    printf("\n");
	}
	
	return 0;
}
