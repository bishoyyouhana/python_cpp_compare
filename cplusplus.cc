#include <cstdio>
#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

// consts
const unsigned int k_max = 40000;
const unsigned int N = 10000;

int main()
{
    // table with data
    double data1[ N ];
    double data2[ N ];
    // table of results
    double coefs1[ k_max ];
    double coefs2[ k_max ]; 
    // main loop 
    const clock_t begin_time = clock();
    for( unsigned int j = 1; j<N; j++ )
    {
        for( unsigned int i = 0; i<k_max; i++ )
        {
            coefs1[ i ] += data2[ j-1 ]*(cos((i+1)*data1[ j-1 ]) - cos((i+1)*data1[ j ]));
            coefs2[ i ] += data2[ j-1 ]*(sin((i+1)*data1[ j-1 ]) - sin((i+1)*data1[ j ]));
        }
    }
    // end of main loop
    float total_time=float( clock () - begin_time );
    fprintf(stdout, "%1.f microseconds\n", total_time);

    return 0;
}