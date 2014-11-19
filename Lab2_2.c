//Kainoa Gaddis (c)
//Lab 2 Problem 2

#include <stdio.h>
#include <stdlib.h>


int main() {

  int number;
  int digits = 1;
  printf("Enter a positive integer: ");
  scanf("%d", &number);

  //Binary Algorithm
  while (number > 1) {
    digits++;
    number = number / 2;
  }

  printf("Binary digits: %d\n", digits); 

  return 0;

}

