//Kainoa Gaddis (c)
//Lab 2 Problem 3

#define _BSD_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int main() {
  
  int size;

  FILE* data_file = fopen("Data1.txt", "r");
  fscanf(data_file, "%d", &size);

  //Import unsorted array
  int sort[size];

  for (int i = 0; i < size; i++) {
    fscanf(data_file, "%d", &sort[i]);
  }
  
  fclose(data_file);

  //Time to check algorithm speed
  struct timeval begin, end, diff;

  gettimeofday(&begin, NULL);
  //Selection Sort Algorithm
  for (int i = 0; i < size - 1; i++) {
    int min = i;
    for (int j = i + 1; j < size; j++) {
      if (sort[j] < sort[min]) {
	min = j;
      }
    }
    //Swap
    int temp = sort[i];
    sort[i] = sort[min];
    sort[min] = temp;
  } 
  gettimeofday(&end, NULL);
  timersub(&end, &begin, &diff);
  int diff_sec = (int) diff.tv_sec;
  int diff_usec = (int) diff.tv_usec;

  //Print sorted array
  for (int i = 0; i < size; i++) {
    printf("%d ", sort[i]);
  }

  printf("\nRun time is: %d sec %d usec\n", diff_sec, diff_usec);

  return 0;

}


/* Used timer to answer question from Lab

Average time for the selection sort algorithm was about 2232 microseconds

Average time for the bubble sort algorithm was about 3850 microseconds.

Therefore the selection sort algorithm runs faster.
*/
