#include <stdio.h>

int main()
{
	int A[2][2],i,j; 

	printf("The size of integer datatype is: %ld", sizeof(int));
	printf("\n");

	printf("\n Please enter the values ");


	for(i=0; i< 2; i++){
		for(j=0; j<2; j++){
			printf("\n Please enter the value at the index (%d ,%d) :   ", i, j);
			scanf("%d", &A[i][j]);
		};
	}


	printf("\n i    - j    - Address            - Values ");

	for(i=0; i< 2; i++){
		for(j=0; j<2; j++){
			printf("\n %d    - %d    - %p     - %d", i,j, &A[i][j], A[i][j]);
		};
	}
	
	printf("\n");
	printf("\n");
	return 0;
}
