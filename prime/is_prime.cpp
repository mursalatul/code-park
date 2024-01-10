#include <iostream>
using namespace std;

/*
# check if a number is prime or not.

Parameter:
- long long: a number to check

Return:
- bool: true if the number is a prime number, else false
*/
bool is_prime(long long n)
{
    // if n is even or less then 2 it is not a prime number
    if (n < 2 || (n > 2 && n % 2 == 0))
        return false;
    
    // every number has atleast 1 divisor less then sqrt of it.  
    for (long long i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;
    return true;
}

// main function

// int main()
// {
//     long long x = 433332;
//     cout << is_prime(x);
//     return 0;
// }