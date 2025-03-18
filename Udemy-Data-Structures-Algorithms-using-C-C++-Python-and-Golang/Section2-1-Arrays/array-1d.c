#include <stdio.h>

int main(){

// #ifndef ONLINE_JUDGE

// 	freopen("input.txt", "r", stdin);

// 	freopen("output.txt", "w", stdout);

// #endif
	int A[5], i;
	printf("The size of integer datatype is %ld  ok \n", sizeof(int) );



	printf("\n Add the elements in the array");
	for (i=0; i<5; i++){
		scanf("%d", &A[i]);
	}


	printf("Index   -    Address  -   Content  \n ");
	for(i=0;i<5;i++){
		printf(" %d   -   %p   -  %d  \n",i,&A[i], A[i]);

	}
}




















