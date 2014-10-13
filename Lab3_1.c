//Kainoa Gaddis (c)
//Lab 3 Problem 3

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {

  int text_size;

  //Open file and input text size
  FILE* data_file = fopen("Data5.txt", "r");
  fscanf(data_file, "%d", &text_size);

  
  //Input text
  char text[text_size + 1];
  fscanf(data_file, "%s", text);

  
  //Input Pattern size and pattern
  int pattern_size;
  fscanf(data_file, "%d", &pattern_size);

  char pattern[pattern_size +1];
  fscanf(data_file, "%s", pattern);


  //Brute Force String Match Algorithm
  int StringMatch() {
    for (int i = 0; i < text_size - pattern_size; i++) {
      int j = 0;
      while (j < pattern_size && pattern[j] == text[i + j]) {
	j++;
      }
      if (j == pattern_size) {
	return i;
      }
    }
    return -1;
  }

  //Prints
  printf("%s\n", pattern);
  printf("%s\n", text);

  //Call Algorithm function
  int answer = StringMatch();
  if (answer == -1) {
    printf("No Match Found.");
  }
  else {
    for (int i = 0; i < answer; i++) {
      printf(" ");
    }

    printf("^");
    for (int i = 0; i < text_size - answer; i++) {
      printf(" ");
    }

    printf("\n");
  }
  
  return 0;

}


/* 
In order for "^" to be directly under the correct character, 
the text must print on one long line in the terminal.
*/
