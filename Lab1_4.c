#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

  int intSize = 0;
  int* intVect1 = NULL;
  int* intVect2 = NULL;
  int intDotVect = 0;

  FILE* fileHandle = fopen("Data3.txt", "r");
  
  fscanf(fileHandle, "%d", &intSize);

  // Get memory space for vector data
  intVect1 = (int*) (malloc(sizeof(int) * intSize));
  intVect2 = (int*) (malloc(sizeof(int) * intSize));
 
  // Copy vector data into separate vectors
  for (int i = 0; i < intSize; i++) {
    fscanf(fileHandle, "%d", &intVect1[i]);
  }
 
  for (int i = 0; i < intSize; i++) {
    fscanf(fileHandle, "%d", &intVect2[i]);
  }
 
  // Dot Product
  for (int i = 0; i < intSize; i++) {
    intDotVect += intVect1[i] * intVect2[i];
    }

  printf("Dot Product: %d\n", intDotVect);

  return 0;
}
