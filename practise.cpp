#include<iostream>
#include<omp.h>

using namespace std;

void sBubble(int arr[], int n){
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n-1; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void pBubble(int arr[], int n){
    for(int i = 0; i<n; ++i){
        #pragma omp parallel for
        for(int j = 1; j<n; j+=2){
            if(arr[j] < arr[j-1]){
                swap(arr[j], arr[j-1]);
            }
        }

        #pragma omp barrier

        #pragma omp parallel for
        for(int j = 2; j<n; j+=2){
            if(arr[j] < arr[j-1]){
                swap(arr[j], arr[j-1]);
            }
        }
    }
}

void printArray(int arr[], int n){
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int n = 5;
    int arr[n] = {3, 6, 1, 8, 4};
    cout<<"Array before sorting:"<<endl;
    printArray(arr, n);
    cout<<"Array after sorting"<<endl;
    pBubble(arr,n);
    printArray(arr, n);

    double start, end;
    start = omp_get_wtime();
    end = omp_get_wtime();
}