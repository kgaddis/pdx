//Kainoa gaddis (c)
//The Game of 31

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_lowest(int* deck) {
  for (int i = 0; i < 5; i++) {
    if (deck[i] > 0){
      return i + 1;
    }
  }

  return 0;
}

int find_highest(int* deck) {

  for (int i = 5; i >= 0; i--) {
    if (deck[i] > 0){
      return i + 1;
    }
  }

  return 0;
}

int large_empty(int* deck) {
  
  for (int i = 5; i >= 0; i--) {
    if (deck[i] == 0){
      return i + 1;
    }
  }

  return 0;
}

void play(char* game) {

  int total = 31;
  int len = strlen(game);

  //Make copy to use in function
  char* copy = malloc(len + 20);
  strcpy(copy, game);

  //Initialize deck
  int deck[6];
  for (int i = 0; i < 6; i++) {
    deck[i] = 4;
  }

  //Set total and deck from input
  for (int i = 0; i < len; i++) {
    int temp = (int) game[i] - 48;
    //printf("%d\n", temp);
    total -= temp;
    deck[temp - 1]--;
  }

  for (int i = 0; i < 6; i++) {
    //printf("%d\n", deck[i]);
  }


  //Simulate rest of game
  while (total > 0 ) {
    //printf("Total: %d\n", total);
  
    int highest = find_highest(deck);
    int lowest = find_lowest(deck);
    int empty = large_empty(deck);
    //printf("High: %d\n", highest);
    //printf("Low: %d\n", lowest);
    
    int choice;
    if (total <= 6 && deck[total - 1] > 0) {
      choice = total;
    }
    else if (total <= 6 && total < lowest) {
      break;
    }
    else if (total <= 6 && deck[total - 1] == 0) {
      choice = total - 1;
    }
    else if (total < 6 + highest && empty != 0) {
      choice = total - empty;
    }
    else if (total <  6 + highest) {
      choice = total - highest - 1;
      if (choice == 0){
	choice = lowest;
      }
    }
    else {
      choice = highest;
    }
    
    //printf("Choice: %d\n", choice);
    copy[++len -1] = choice;
    total -= choice;
    deck[choice - 1]--;
    //printf("Total: %d\n", total);
  
  }
  

  //Print Winner
  int player = len % 2;
  if (player == 0) {
    printf("%s B\n", game);
  }
  else {
    printf("%s A\n", game);
  }
}


int main() {

  //Get input data
  FILE* input_data = fopen("game_input.txt", "r");
  
  char games[5][40];

  for (int i = 0; i < 5; i++) {
    for (int j = 0; i < 40; j++) {
      char temp = fgetc(input_data);
      //printf("%c", temp);
      
      if (temp != '\n') {
	games[i][j] = temp;
      }
      else {
	games[i][j] = '\0';
	break;
      } 
    }  
  }
  
  fclose(input_data);


  //Play Games
  for (int i = 0; i < 5; i++) {
    play(games[i]);
  }

  return 0;
}


//May not work for all test cases but workes for the given ones
