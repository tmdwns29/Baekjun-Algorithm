#include <iostream>
using namespace std;
int N;
int d[10];
int main()
{
    cin >> N;
    for (int i = 0; i < N; ++i)
    {
        cin >> d[i];
    }

    if (N == 1)
    {
        if (d[0] == 0)
        {
            cout << "YES\n0";
            return 0;
        }
    }
    cout << "YES"
        << "\n";
    cout << d[N - 1] << d[N - 1] << d[N - 1];

    return 0;
}