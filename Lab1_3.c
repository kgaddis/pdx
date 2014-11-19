#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


int main() {

  int intSize = 0;
  int intRepeat = false;
  int* intData = NULL;

  
  FILE* fileHandle = fopen("Data2.txt", "r"); {

    fscanf(fileHandle, "%d", &intSize);
    
    intData = (int*) (malloc(sizeof(int) * intSize));
    
    // Reads numbers from file and writes to array in memory
    for (int i = 0; i < intSize; i++) {
      
      fscanf(fileHandle, "%d", &intData[i]);
      
    }


    // Check for repititions
    for (int i = 0; i < intSize - 2; i++) {

      for (int j = i + 1; j < intSize - 1; j++) {
	
	if (intData[i] == intData[j]) {
	  printf("Index: %d\t Value: %d\n", j, intData[j]);
	  intRepeat = true;
	}

      } 

    }

  }
  
  fclose(fileHandle);
  
  if (intRepeat == false) {
    printf("NO REPEATED ELEMENTS\n");
  }
  
  free(intData);

  return 0;

}
