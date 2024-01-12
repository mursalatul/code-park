#include<bits/stdc++.h>
using namespace std;
/*
    #Selection sort algorithm.
    -Find the minimum element in unsorted array & swap it with the element at beginning.[1]
    -repeate [1] until the array is sorted.

    paremeter:
    -n = to recieve array size.
    -arr[] = to recieve the array[]
*/
void selection_sort(int n,long long arr[])
{
    double temp;
    /*i is iterating from 1st index (i=0) to 2nd last index (n-1) of the array*/
    for(int i=0; i<n-1; i++)
    {
        /*j is iterating from (i+1) index to last index (n) of the array*/
        for(int j=i+1; j<n; j++)
        {
            /*Comparing value of arr[i+1] with arr[i]*/
            if(arr[j] < arr[i])
            {
                /*Swapping values*/
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

//main function
int main()
{
    int n, i;
    cin >> n;//taking input for n
    long long arr[n];//declaring & initializing arr[n]


    //Taking input for arr[n]
    for(i=0; i<n; i++)
    {
        cin >> arr[i];
    }

    /*
        passing arguments (n,arr):
        -n = passing size of arr[n]
        -arr = passing all the elements of arr[n]
    */
    selection_sort(n,arr);//calling selection sort function & passing arguments.


    /*printing sorted arr[n]*/
    for(i=0; i<n; i++)
    {
        cout << arr[i] << ' ';
    }

    return 0;
}