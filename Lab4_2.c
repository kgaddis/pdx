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

  
  //Create queue structures and functions
  struct vertex {
    int value;
    struct vertex* next;
  };

  struct vertex* insert(int number) {
    struct vertex* new = malloc(sizeof(struct vertex));
    new->value = number;
    new->next = NULL;
    return new;
  };


  //BFS Algorithm
  int count = 0;

  void bfs(int i) {
    count++;
    graph[i][i] = count;

    //Initialize first and last pointers and add first vertex to queue
    struct vertex* first = malloc(sizeof(struct vertex));
    struct vertex* last = malloc(sizeof(struct vertex));
    struct vertex* ii = insert(i);
    first->value = ii->value;
    first->next = NULL;
    last->value = ii->value;
    last->next = NULL;
        
    while (first != NULL) {
      for (int j = 0; j < size; j++) {
	if (graph[first->value][j] && graph[j][j] == 0) {
	  count++;
	  graph[j][j] = count;
	 
	  //Add next vertex to queue
	  struct vertex* new = insert(j);
	  last->next = new;
	  last = last->next;
	}
      }
      //Remove and free first queue vertex or if last one end while loop
      if (first->next == NULL) {
	first = NULL;
      }
      else {
	struct vertex* temp = first;
	first = first->next;
	free(temp);
      } 
    }
  }

  //Initial function call
  for (int i = 0; i < size; i++) {
    if (graph[i][i] == 0) {
      bfs(i);
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

