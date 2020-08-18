#include<stdio.h>
#include <stdlib.h>
int main(){
	int max = 6, add = 0, diff = 0, x1, y1, x2, y2;
	float no = 0, average;
	for(y1 = 0; y1 < max; y1++){
		x1 = 0;
		for(x1 = 0; x1 < max; x1++){
			y2 = 0;
			for(y2 = 0; y2 < max; y2++){
				x2 = 0;
				for(x2 = 0; x2 < max; x2++){
					diff = abs(x2 - x1) + abs(y2 - y1);
					add = add + diff;
					no = no + 1;
				}
			}
		}
	}
	printf("Total distance = %d", add);
	average = add/no;
	printf("\nAverage distance = %f", average);
	return 0;
}
