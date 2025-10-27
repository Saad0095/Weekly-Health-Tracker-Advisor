#include <stdio.h>
void inputData(int water[], int sleep[], int workout[]);
void calculateAverages(int water[], int sleep[], int workout[]);
void getAdvise();
void displaySummary();
void mainMenu(int water[], int sleep[], int workout[]);

int main() {
  int water[7], sleep[7], workout[7];
  mainMenu(water, sleep, workout);

  return 0;
}

void mainMenu(int water[], int sleep[], int workout[]) {
  int choice;
  do {
    printf("Welcome to Weekly Health Tracker & Advisor!\n");
    printf("1. Enter Weekly Data\n");
    printf("2. Show Weekly Summary\n");
    printf("3. Exit\n");
    printf("Enter you choice (1-3): ");
    scanf("%d", &choice);

    switch (choice) {
    case 1:
      inputData(water, sleep, workout);
      break;
    case 2:
      calculateAverages(water, sleep, workout);
      break;
    case 3:
      printf("Exiting program. \n");
      break;

    default:
      printf("Invalid Choice\n");
      break;
    }
  } while (choice != 3);
}

void inputData(int water[], int sleep[], int workout[]) {}
void calculateAverages(int water[], int sleep[], int workout[]) {}
void getAdvise() {}
void displaySummary() {}