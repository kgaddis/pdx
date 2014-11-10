//Kainoa Gaddis (c)
//Lab 5 Problem 2

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Binary Search Algorithm
int BinarySearch (int* A, int K, int n) {
  
  float l = 0;
  float r = n - 1;
  int m;
  while (l <= r) {
    m = floor((l + r) / 2);
    if (K == A[m]) {
      return m;
    }
    else if (K < A[m]) {
      r = m - 1;
    }
    else {
      l = m + 1;
    }
  }

  return -1;

}

//Main Function
int main() {

  //Import data from file
  int size;
  FILE* data_file = fopen("Data8.txt", "r");
  fscanf(data_file, "%d", &size);
  
  int* array = (int*) malloc(sizeof(int) * size);
  for (int i = 0; i < size; i++) {
    fscanf(data_file, "%d", &array[i]);
  }

  fclose(data_file);

  //Get Key from user
  int key;
  printf("Enter Search Key: ");
  scanf("%d", &key);

  
  //Call Binary Search Algorithm
  printf("%d\n", BinarySearch(array, key, size));

  free(array);

  return 0;

}
