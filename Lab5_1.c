//Kainoa Gaddis
//Lab 5 Problem 1

#include <stdio.h>
#include <stdlib.h>


int main() {

  int integer;
  
  printf("Enter Positive Integer: ");
  scanf("%d", &integer);
  
  //Gray Code Algorithm
  if (integer < 0) {
    printf("Integer is not positive\n");
    return 0;
  }
  else {
    integer  = (integer >> 1) ^ integer;
  }

  //Convert from decimal to binary
  //Find number of digits to malloc array
  int digits = 1;
  int num = integer;

  while (num > 1) {
    digits++;
    num = num / 2;
  }
  
  int* answer = (int*) malloc(sizeof(int) * (digits + 1));

  for (int i = 0; i < digits; i++) {
    answer[i] = integer % 2;
    integer = integer / 2;
  }
  

  //Print Gray Code
  printf("Gray Code: ");
  
  for (int i = (digits - 1); i  >= 0; i--) {
    printf("%d", answer[i]);
  }

  printf("\n");
  
  return 0;

}
