#include<iostream>
using namespace std;

/* Function to perform binary search in a sorted array
 Parameters:
 - arr: Sorted array to be searched
 - n: Size of the array
 - key: Element to be searched for
 Returns:
 - Index of the key if found, otherwise -1*/
 
int binarysearch(int arr[], int n, int key)
{
    int start = 0;  // Initialize the starting index of the search range
    int end = n;    // Initialize the ending index of the search range

    // Continue the search until the start index is less than or equal to the end index
    while (start <= end)
    {
        int mid = (start + end) / 2;  // Calculate the middle index

        if (arr[mid] == key)  // Check if the middle element is equal to the key
        {
            return mid;  // Return the index where the key is found
        }
        else if (arr[mid] < key)  // If key is greater, update the start index
        {
            start = mid + 1;
        }
        else  // If key is smaller, update the end index
        {
            end = mid - 1;
        }
    }

    // If key is not found in the array, return -1
    return -1;
}

int main()
{
    int n;
    cout << "Enter the array size: ";
    cin >> n;

    int arr[n];
    cout << "Enter the elements of the array in sorted order: ";
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int key;
    cout << "Enter the key: " ;
    cin >> key;

    // Call the binarysearch function and output the result
    cout << "The key is found at position: " << binarysearch(arr, n, key) << endl;

    // Return 0 to indicate successful execution
    return 0;
}
