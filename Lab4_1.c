//Kainoa Gaddis
//Lab 4 Problem 1

#include <stdio.h>
#include <stdlib.h>

int main() {

  //Import Data
  int size;
  FILE* data_file = fopen("Data7.txt", "r");
  fscanf(data_file, "%d", &size);

  
  //Create matrix using malloc
  int ** graph = malloc(sizeof(int*) * size);
  for (int i = 0; i < size; i++) {
    graph[i] = (int*) malloc(sizeof(int) * size);
  }
  
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      fscanf(data_file, "%d", &graph[i][j]);
    }
  } 

  fclose(data_file);

  
  //DFS Algorithm
  int count = 0;

  void dfs(int i) {
    count++;
    graph[i][i] = count;
    for (int j = 0; j < size; j++) {
      if (graph[i][j] == 1 && graph[j][j] == 0) {
	dfs(j);
      }
    }
  }

  //Initial function call
  for (int i = 0; i < size; i++) {
    if (graph[i][i] == 0) {
      dfs(i);
    }
  }
  

  //Print Final Matrix
  printf("\n");
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("%d  ", graph[i][j]);
    }
    printf("\n");
  }
  

  //Free mallocs
  for (int i = 0; i < size; i++) {
    free(graph[i]);
  }
  free(graph);
  
  return 0;

}


