//Kainoa Gaddis (c)
//Lab 3 Problem 2


#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {

  //Input file and data points
  int size;
  FILE* data_file = fopen("Data6.txt", "r");
  fscanf(data_file, "%d", &size);

  int x_values[size + 1];
  int y_values[size + 1];

  for (int i = 0; i < size; i++) {
    fscanf(data_file, "%d", &x_values[i]);
    fscanf(data_file, "%d", &y_values[i]);
  }
  
  //Closest Points Algorithm
  double d_min = INFINITY;
  int index1;
  int index2;
  for (int i = 0; i < size - 1; i++) {
    for (int j = i + 1; j < size; j++) {
      int d = sqrt(pow(x_values[i] - x_values[j], 2) + pow(y_values[i] - y_values[j], 2));
      
      if (d < d_min) {
	d_min = d;
	index1 = i;
	index2 = j;
      }
    }
  }

  
  //Print
  printf("Index 1: %d\n", index1);
  printf("Index 2: %d\n", index2);
  printf("Point[%d]: %d, %d\n", index1, x_values[index1], y_values[index1]);
  printf("Point[%d]: %d, %d\n", index2, x_values[index2], y_values[index2]);

  return 0;
}


/*
If there is more than one closest pair then the program will only
return the indexes of the first pair to occur. This is because
the d_min value if only changed if d is less than d_min, not less than or equal to.
*/
