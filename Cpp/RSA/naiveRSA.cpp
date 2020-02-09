/* Input:
 *  A string with size up to 1000
 * Output:
 *  A encrypted and decipted string
 * Description:
 *  Implements RSA which can encrypt and decrypt strings composed of alphabetic
 *  characters from [a-z] without space.
 * Link:
 *  https://eli.thegreenplace.net/2019/rsa-theory-and-implementation/
*/
using namespace std;
#include<iostream>
#include<random>
#include<string>

#define LOWER 0
#define UPPER 19
#define MAX_SIZE 1000
#define SUB 97

unsigned long int gcd(unsigned long int a, unsigned long int b){
    if( a == b) return a;
    else if (a == 0) return b;
    else if (b == 0) return a;
    else if (a >b) return gcd(a%b,b);
    else return gcd(a,b%a);
}

unsigned long int pow(unsigned long int a, unsigned long int b){
    unsigned long int p=1;
    while(b>=1){
        p *= a;
        b--;
    }
    return p;
}

void print_array(unsigned long int array[], int size){
    for(int i=0; i < size; i++){
        cout << (char)(array[i] + SUB);
    }
    cout << endl;
}

int main(){
    // Choose two prime numbers p and q
    unsigned long int p=3,q=11, size;
    string plaintext;
    unsigned long int ciphertext[MAX_SIZE];
    unsigned long int deciphertext[MAX_SIZE];

    // Input data
    getline(cin, plaintext);

    // Sanity Check
    cout << "p = " << p << ", q = " << q << endl;
    cout << "Plaintext: " << plaintext << endl; 
    fflush(stdout);

    // Define n and z
    unsigned long int n = p*q;
    unsigned long int z = (p-1)*(q-1);

    // Chose a number d | gcd(z,d) = 1
    unsigned long int d;
    default_random_engine generator;
    uniform_int_distribution<unsigned long int> distribution(LOWER,UPPER);
    do{
        d = distribution(generator);
    }while(d == 0 | gcd(d,z)!=1);

    // Find e such that (e*d) = 1 mod z
    unsigned long int e;
    do{
        e = distribution(generator);
    }while(e == 0 | (e*d)%z != 1);

    // Sanity Check
    cout << "d = " << d << ", e = " << e << endl;
    cout << "n = " << n << ", z = " << z << endl;
    for(int i=0; i < plaintext.size(); i++){
        cout << (unsigned long int)plaintext[i]-SUB << ", ";
    }
    cout << endl;

    // Encrypt message
    for(int i=0; i < plaintext.size(); i++){
        ciphertext[i] = (pow(((unsigned long int)plaintext[i])-SUB,e))%n;
    }
    
    cout << "Encrypted message: ";
    print_array(ciphertext,plaintext.size());

    // Decrypt message
    for(int i=0;i<plaintext.size(); i++){
       deciphertext[i] = (pow(ciphertext[i],d))%n;
    }
    cout << "Decrypted message: ";
    print_array(deciphertext, plaintext.size());

    return 0;    
}
