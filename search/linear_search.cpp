
#include <iostream>
using namespace std;

/*
Function to perform linear search

Parameters:
  - long long arr[]: an array to search in
  - long long n: size of the array
  - long long x: key to search for
  
Returns:
  - long long: index of the key if found, -1 otherwise
*/
long long linearSearch(long long arr[], long long n, long long x){
    for(long long i=0; i<n; ++i){
        if(arr[i] == x){
            return i;
        }
    }
    return -1;
}

// Main function
// int main() {
//     long long n;
//     cout << "Enter the size of the array: ";
//     cin >> n;

//     long long *arr = new long long[n];
//     cout<<"Enter the elements of the array:";
//     for(long long i = 0; i < n; ++i){
//         cin>>arr[i];
//     }

//     long long x;
//     cout<<"Enter one element to search:";
//     cin>>x;

//     long long result=linearSearch(arr, n, x);
//     cout<<result<<endl;

//     return 0;
// }
