using namespace std;
#include<iostream>
#include"utils.h"

inline int mod(int a, int b){
    if(a<0) return (a%b)+ b;
    else return (a%b);
}

template <class ttype>
void rotate_vector(ttype array[],int d, int n){
    int pos=0, next_pos;
    int i = 0;
    int j = 0;
    int n_grups=n/d + 1;
    ttype temp;
    d = mod(d,n);

    while(i < d){
        pos = i;
        temp = array[pos];
        next_pos = mod(pos+d,n);
        j = 0;
        while(j<n_grups-1){
            array[pos] = array[next_pos];
            pos = next_pos;
            next_pos = next_pos + d;
            if (next_pos>=n) break;
            j++;
            print_array(array,n);
        }
        array[pos] = temp;
        i ++;
    }
}

int main(){
    int array[] = {1,2,3,4,5,6,7};
    int d = 2;
    int n = 7;
    rotate_vector(array,d,n);
    print_array(array,n);

    return 0;
}
