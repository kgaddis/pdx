//Kainoa Gaddis (c)
//Lab 5 Problem 5

#include <stdio.h>
#include <stdlib.h>


int main() {

  int m,n;
  printf("Enter first positive integer: ");
  scanf("%d", &m);
  printf("Enter second positive integer: ");
  scanf("%d", &n);

  if (m < 1 || n < 1) {
    printf("Invalid Inputs\n");
    return 0; 
  }
  
  //Euclid's Algorithm
  int r;
  while (n != 0) {
    r = m % n;
    m = n;
    n = r;
  }
  
  printf("gcd: %d\n", m);

  return 0;

}
