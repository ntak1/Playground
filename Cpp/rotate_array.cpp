using namespace std;
#include<iostream>
#define MAX_SIZE 100

inline int mod(int a, int m){
    if ( a > 0) return a%m;
    else return ((a+m)%m);
}

void print_array(int array[], int n){
    for(int i=0; i < n; i++){
        cout << array[i] << ", ";
    }
    cout << endl;
}

void rotate(int array[], int d, int n){
    int i, j, k = 1;
    int temp;
    for( i=d-1; i>=0; i--){
        temp = array[i];
        for(j=i; j< (n-k); j++){
            array[j] = array[j+1]; 
        }
        array[n-k] = temp;;
        
        k++;
    }
}

int main(){
    int d, n;
    int array[MAX_SIZE];

    cout << "d: ";    
    cin >> d;

    cout << "n: ";    
    cin >> n;

    for(int i=0; i < n; i++){
        cin >> array[i];
    }

    // Sanity check
    cout << "d: " << d << ",n: " << n << endl;
    cout << "array before: ";
    print_array(array, n);
    
    rotate(array, d, n);
    cout << "array after: ";
    print_array(array, n);

    return 0;
}
