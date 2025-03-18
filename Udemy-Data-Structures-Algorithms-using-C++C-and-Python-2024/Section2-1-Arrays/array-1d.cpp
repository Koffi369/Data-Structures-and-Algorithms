#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif

    // Code Starting
    int A[10], arr_size, i;

    cout << "Size of Integer datatype:"  << sizeof(int) << endl;

    cout << "\nEnter the array size (1 to 10): ";
    cin >> arr_size;

    // Check if the array size is within bounds
    if (arr_size < 1 || arr_size > 10) {
        cout << "Array size must be between 1 and 10!" << endl;
        return 1;  // Exit the program with an error code
    }

    for (i = 0; i < arr_size; i++) {
        cout << "\nEnter element at index " << i << ": ";
        cin >> A[i];
    }

    cout << "Index    -Address    -Value" << endl;

    for (i = 0; i < arr_size; i++) {
        cout << "\n" << i << "    " << &A[i] << "    " << A[i] << endl;
    }

    return 0;
}
