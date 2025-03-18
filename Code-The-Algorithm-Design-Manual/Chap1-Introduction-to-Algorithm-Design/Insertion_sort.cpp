#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int  main(){
	int A[5], i, j, temp;

	i =0;

	for(i=0; i<5; i++){
		cout<<"Enter element at index "<<i<< endl; 
		cin >> A[i];
	}

	i =0;
	cout<<"i = "<<i<< endl; 

	while(i<5){

		for (j=0; j<i; j++){
			if (A[j] > A[i]){
				temp =  A[j];
				A[j] =  A[i];
				A[i] = temp;
			}
		}
	i++;
	}


	for(i=0; i<5; i++){
		cout<<"element at index " <<i<< "= "<<A[i]<< endl; 
	}
}




// Answer @ page 4:

// void insertion_sort(item_type s[], int n) {
// 	int i, j;
// 	/* counters */
// 	for (i = 1; i < n; i++) {
// 		j = i;
// 		while ((j > 0) && (s[j] < s[j - 1])) {
// 		swap(&s[j], &s[j - 1]);
// 		j = j-1;
// 		}	
// 	}
// }













