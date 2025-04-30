// You can compile in the terminal with
// g++ -std=c++17 code42.cpp -o code42
// Execute it with ./code42

/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <numeric>
#include <cmath>
#include <sstream>
#include <thread>
#include <ctime>
 
#include <deque>
#include <list>
#include<forward_list>
using namespace std;
 
bool isEven(const int& val){
    return (val % 2) == 0;
}
 

int main()
{
    // ---------- SEQUENCE CONTAINERS ----------
    // Contains data stored in order
    
    // ---------- DEQUES ----------
    
    // A deque (Deck) is a dynamic array like vectors
    // except it also allows for insertion or deletion
    // from the front
    deque<int> deq1; 
    
    // Add to the end and front
    deq1.push_back(5);
    deq1.push_front(1);
    deq1.push_front(0);

    cout << "-----------------------" << endl;
    for(int i : deq1)
        cout << i << endl;


    // Add values with assign
    deq1.assign({11,12});

    // deq1 = {13,14};

    cout << "----------   deq1.assign({11,12})  -------------" << endl;
    for(int i : deq1)
        cout << i << endl;


    
    // Get the size
    cout << "Size : " << deq1.size()
            << endl;
    
    // Access by index
    cout << deq1[0] << endl;
    cout << deq1.at(1) << endl;
    
    // Add at an index using an iterator
    deque<int>::iterator it = deq1.begin() + 1;
    deq1.insert(it, 3);


    cout << "-----------    deq1.insert(it, 3);  ------------" << endl;
    for(int i : deq1)
        cout << i << endl;



    
    // Add multiple values
    int tempArr[5] = {6,7,8,9,10};
    deq1.insert(deq1.begin(), tempArr +1, tempArr+5);



    cout << "-----------   deq1.insert(deq1.end(), tempArr, tempArr+5);  ------------" << endl;
    for(int i : deq1)
        cout << i << endl;


    
    // Erase at an index 
    deq1.erase(deq1.end() - 1);


    cout << "-----------    deq1.erase(deq1.end());  ------------" << endl;
    for(int i : deq1)
        cout << i << endl;



    
    // Erase 1st 2 elements
    deq1.erase(deq1.begin(), deq1.begin()+3);



    cout << "-----------  deq1.erase(deq1.begin(), deq1.begin()+3);  ------------" << endl;
    for(int i : deq1)
        cout << i << endl;


    
    // Pop first value
    deq1.pop_front();


    cout << "-----------  deq1.pop_front(); ------------" << endl;
    for(int i : deq1)
        cout << i << endl;




    
    // Pop last
    deq1.pop_back();

    cout << "------------   deq1.pop_back();  -----------" << endl;
    for(int i : deq1)
        cout << i << endl;



    
    // Create a deque with 2 50s
    deque<int> deq2(2,50);
    

    // Swap values in deques
    deq1.swap(deq2);


    cout << "------------ deq1.swap(deq2);  -----------" << endl;
    cout << "------------deq1 -------" << endl;
    for(int i : deq1)
        cout << i << endl;

    cout << "------------deq2 ------" << endl;
    for(int i : deq2)
        cout << i << endl;

    
    // Delete all values
    deq1.clear();
    
    // Cycle through the deque
    cout << "----------- deq1.clear();  ------------" << endl;
    for(int i : deq1)
        cout << i << endl;
}

