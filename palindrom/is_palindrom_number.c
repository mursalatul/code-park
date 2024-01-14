#include <stdio.h>

/*
is the inputed number a valid palindrom

@param long_long number

@return int 1(if the number is a valid palindrom), 0(if the number is not a valid palindrom)
*/
int is_palindrom_number(long long num)
{
    /* by default considering num as a palindrom */
    int status = 1;

    // saving a temporary copy of the number to perform operation
    long long temp_num = num;

    /* store reverse num */
    long long reverse_num = 0;
    while (temp_num) /* loop will work till temp_num is not 0 */
    {
        reverse_num = (reverse_num * 10) + (temp_num % 10);
        temp_num /= 10;
    }
    printf("%lld", reverse_num);
    /* if reverse_num and the num is same then the inputed number is a palindrom */
    return reverse_num == num;
}

int main()
{
    long long n;
    scanf("%lld", &n);
    printf("%lld", is_palindrom_number(n));
    return 0;
}