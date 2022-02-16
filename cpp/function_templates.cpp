using namespace std;
#include<iostream>

template <class ttype>
void print_array(ttype array[], int size){
    for(int i=0; i < size-1; i++){cout << array[i] << ", ";}
    cout << array[size-1];
    cout << endl;
}

int main(){
    double darray[] = {0.1, 0.2 ,0.3};
    int iarray[] = {1,2,3};
    print_array(darray,3);
    print_array(iarray,3);
    return 0;
}
