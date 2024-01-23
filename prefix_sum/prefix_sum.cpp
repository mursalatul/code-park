#include <iostream>
#include <vector>
using namespace std;


/*
return a vector of prefix sum of the inputed vector

Parameter:
- vector long long

Return:
- vector long long of size inputed vector + 1(cause first element will be 0)
*/
vector<long long> prefix_sum(vector<long long> v)
{
    // initializing prefix sum vector
    long long n = v.size();
    vector<long long> psum(n + 1, 0);
    for (long long i = 1; i <= n; i++)
    {
        psum[i] = psum[i - 1] + v[i - 1];
    }
    return psum;
}

int main()
{
    vector<long long> v = {4, 3, 2, 5};
    for (long long x : prefix_sum(v))
        cout << x << ' ';
    return 0;
}