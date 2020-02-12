template <class ttype>
void print_array(ttype array[], int size){
    for(int i=0; i < size-1; i++){cout << array[i] << ", ";}
    cout << array[size-1];
    cout << endl;
}
