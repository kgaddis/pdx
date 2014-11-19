#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


int main() {

  int intSize = 0;
  int intInput = 0;
  int intFound = false;
  int intFromFile = 0;
  
  // get input
  printf("Please input a positive integer: ");
  scanf("%d", &intInput);

  if (intInput % 2 == 0) {
    
    FILE* fileHandle = fopen("Data1.txt", "r");

    fscanf(fileHandle, "%d", &intSize);
    
    for (int intFor1 = 0; intFor1 < intSize; intFor1 ++) {
      
      fscanf(fileHandle, "%d", &intFromFile);
      if (intFromFile == intInput) {
	printf("Index: %d\n", intFor1);
	intFound = true;
      }
    }
    
    if (intFound == false) {
      printf("NOT FOUND\n");
    }
        
    fclose(fileHandle);

  }
  
  else {
    printf("Invalid Input\n");
  }

  return 0;

}
