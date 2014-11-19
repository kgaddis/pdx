//Kainoa Gaddis (c)
//Lab 2 Problem 1

#include <stdio.h>
#include <stdlib.h>

int main() {
  
  //Get size of matrix
  int size;
  
  FILE* data_file = fopen("Data4.txt", "r");
  fscanf(data_file, "%d", &size);    


  //Create matrix
  int matrix_1[size][size];
  int matrix_2[size][size];
  int matrix_3[size][size];

  
  //Read in matrix from file
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      fscanf(data_file, "%d", &matrix_1[i][j]);
    }
  }

  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      fscanf(data_file, "%d", &matrix_2[i][j]);
    }
  }

  fclose(data_file);

  //Matrix Multiplication Algorithm
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      matrix_3[i][j] = 0;
      for (int k = 0; k < size; k++) {
	matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j];
      }
    }
  }


  //Print cross product matrix
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("%d ", matrix_3[i][j]);
    }
    printf("\n");
  }

  
  return 0;
}


/* Questions
a. Yes it matters if the elements in the matricies are positive or negative because it will
   change the cross product result becasue there is multiplication

b. The matrix cross product uses the dot product to calculate each value of the resulting matrix

c. If thew matrix values were separated by commas nothing would need to be modified becasue
   I imported the values by selecting the next integer. It would just pass over the commas
*/
