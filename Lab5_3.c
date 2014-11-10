//Kainoa Gaddis (c)
//Lab 5 Problem 3

#include <stdio.h>
#include <stdlib.h>


int function1(int a, int n) {

  if (n == 1) {
    return a;
  }
  else if (n == 0) {
    return 0;
  }
  else {
    return function1(a, n - 1) * a;
  }
}

float function2(float a, int n) {
  
  if (n == 1) {
    return a;
  }
  else if (n == 0) {
    return 0;
  }
  else {
    return function2(a, n - 1) * a;
  }
  
}

float function3(float a, int n) {
  
  if (n == -1) {
    return 1 / a;
  }
  else if (n == 1) {
    return a;
  }
  else if (n == 0) {
    return 0;
  }
  else if (n < 0) {
    return  function3(a, n + 1) * 1 / a;
  }
  else {
    return function3(a, n - 1) * a;
  }
  
}


int main() {

  int version;
  printf("Enter version (1, 2, or 3): ");
  scanf("%d", &version);

  if (version == 1) {
    int a, n;
    printf("Enter \"a\" value: ");
    scanf("%d", &a);
    printf("Enter \"n\" value: ");
    scanf("%d", &n);
    
    
    if (n < 0 || a < 0) {
      printf("Invalid Inputs\n");
    }
    else {
      int answer = function1(a, n);
      printf("Answer: %d\n", answer);
    }

  }
  else if (version == 2) {
    float a;
    int n;
    printf("Enter \"a\" value: ");
    scanf("%f", &a);
    printf("Enter \"n\" value: ");
    scanf("%d", &n);
    
    
    if (n < 0 ) {
      printf("Invalid Inputs\n");
    }
    else {
      float answer = function2(a, n);
      printf("Answer: %f\n", answer);
    }

  }
  else if (version == 3) {
    float a;
    int n;
    printf("Enter \"a\" value: ");
    scanf("%f", &a);
    printf("Enter \"n\" value: ");
    scanf("%d", &n);
    
    float answer = function3(a, n);
    
    printf("Answer: %f\n", answer);
       
  }
  else {
    printf("Invalid version input\n");
  }

  return 0;

}
