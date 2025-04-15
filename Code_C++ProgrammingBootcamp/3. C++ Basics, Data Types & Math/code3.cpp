
#include <cstdlib>
#include <string>
#include <iostream>


using namespace std;

int main(){


    string question (" Please Enter a number:  ");
    string snum1, snum2;

    cout <<  question;

    cin >>  snum1;

    cout <<  question;

    cin >>  snum2;


    int inum1 = stoi(snum1);
    int inum2 = stoi(snum2);


    printf(" For int:  %d + %d = %d\n", inum1, inum2, (inum1 + inum2)) ;




    double dnum1 = stod(snum1);
    double dnum2 = stod(snum2);


    printf("For double: %f + %f = %f\n", dnum1, dnum2, (dnum1 + dnum2)) ;

    return 0;
}


// You can compile in the terminal with
// g++ -std=c++17 code3.cpp -o code3
// Execute it with ./code3 


/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////



// #include <cstdlib>
// #include <iostream>
// #include <string>
// using namespace std;
 
// int main() {
     
//     // Create a string
//     string sQuestion ("Enter Number 1 : ");
    
//     // Create empty strings to store values
//     string sNum1, sNum2;
    
//     cout << sQuestion;
    
//     // Receive user input and store it
//     cin >> sNum1;
    
//     cout << "Enter Number 2 : ";
//     cin >> sNum2;
    
//     // Convert from strings to int
//     // stod converts from strings to doubles
//     int nNum1 = stoi(sNum1);
//     int nNum2 = stoi(sNum2);
    
//     // Math Operators
//     printf("%d + %d = %d\n", nNum1, nNum2, (nNum1 + nNum2));
//     printf("%d - %d = %d\n", nNum1, nNum2, (nNum1 - nNum2));
//     printf("%d * %d = %d\n", nNum1, nNum2, (nNum1 * nNum2));
//     printf("%d / %d = %d\n", nNum1, nNum2, (nNum1 / nNum2));
//     printf("%d %% %d = %d\n", nNum1, nNum2, (nNum1 % nNum2));
    
//     // ----- PROBLEM : MILES TO KILOMETERS -----
//     // Sample knowing that kilometers = miles * 1.60934
//     // Enter Miles : 5
//     // 5 miles equals 8.0467 kilometers
    
//     // Create needed variables
//     string sMiles;
//     double dMiles, dKilometers;
    
//     // Ask user to input miles and store string input
//     cout << "Enter Miles : ";
//     cin >> sMiles;
    
//     // Convert from string to double
//     dMiles = stod(sMiles);
    
//     // Convert from miles to km
//     dKilometers = dMiles * 1.60934;
    
//     // Output the results
//     printf("%.1f miles equals %.4f kilometers\n", dMiles, dKilometers);
    
//     return 0;
// }
