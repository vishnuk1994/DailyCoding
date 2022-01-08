/*
Count the number of ways to reach the top of n stairs where taking 1 or 2 steps at atime is allowed
Nice explanation: https://www.youtube.com/watch?v=fiPLaxkhdcQ&ab_channel=BackToBackSWE

*/
#include <iostream>

using namespace std;

int CountWaysForStep(int n)
{
    int a[n+1];
    a[0]=1;
    a[1]=1;
    a[2]=2;
    for (int i =2; i<=n; i++)
    {
        a[i] = a[i-1] + a[i-2];
    }
    return a[n];
}

int main()
{
    int n = 5;
    cout<<"Hello World : " << CountWaysForStep(n);

    return 0;
}
