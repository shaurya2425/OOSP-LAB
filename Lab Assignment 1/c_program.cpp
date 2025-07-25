#include <iostream>
using namespace std;

int main() {
    int n;  // size of the array
    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];  // declare array of size n

    cout << "Enter " << n << " elements:\n";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];  // input elements
    }

    cout << "You entered: ";
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";  // output elements
    }
    cout << endl;

    return 0;
}
