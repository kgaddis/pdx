#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {

  int intSize = 0;
  int intCurrent =NULL;
  int intLargest = NULL;

  FILE* fileHandle = fopen("Data1.txt", "r");
  
  fscanf(fileHandle, "%d", &intSize);
  
  for (int intFor1 = 0; intFor1 < intSize; intFor1 ++) {
    
    fscanf(fileHandle, "%d", &intCurrent);
    
    if (intCurrent > intLargest) {
      intLargest = intCurrent;
    }
  }

  
  fclose(fileHandle);
  
  printf("%d\n", intLargest);
  
  return 0;

}
