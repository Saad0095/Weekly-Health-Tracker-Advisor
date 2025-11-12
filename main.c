#include <stdio.h>
void inputData(float water[], float sleep[], float workout[]);
void calculateAverages(float water[], float sleep[], float workout[],
                       float *avgWater, float *avgSleep, float *avgWorkout);
void getAdvise(float avgWater, float avgSleep, float avgWorkout);
void displaySummary(float water[], float sleep[], float workout[],
                    float avgWater, float avgSleep, float avgWorkout);
void mainMenu(float water[], float sleep[], float workout[]);

int main() {
  float water[7], sleep[7], workout[7];
  mainMenu(water, sleep, workout);

  return 0;
}

void mainMenu(float water[], float sleep[], float workout[]) {
  int choice;
  float avgWater = 0, avgSleep = 0, avgWorkout = 0;
  printf("\n\nWelcome to Weekly Health Tracker & Advisor!\n\n");
  do {
    printf("\n--- Main Menu ---\n");
    printf("1. Enter/Update Weekly Data\n");
    printf("2. View Summary & Advice\n");
    printf("3. Exit Program\n");
    printf("Enter your choice (1-3): ");
    scanf("%d", &choice);

    switch (choice) {
    case 1:
      inputData(water, sleep, workout);
      calculateAverages(water, sleep, workout, &avgWater, &avgSleep,
                        &avgWorkout);
      printf("\n--- Data Input Completed! ---\n");
      printf("Select option 2 to view the results.\n");
      break;

    case 2:
      if (avgWater == 0 && avgSleep == 0 && avgWorkout == 0) {
        printf("\nNo data found. Please select option 1 first.\n");
      } else {
        displaySummary(water, sleep, workout, avgWater, avgSleep, avgWorkout);
        getAdvise(avgWater, avgSleep, avgWorkout);
      }
      break;

    case 3:
      printf("\nProgram Exited successfully!\n");
      break;

    default:
      printf("\nInvalid choice. Please enter 1, 2, or 3.\n");
      break;
    }
  } while(choice != 3);
}

void inputData(float water[], float sleep[], float workout[]) {
  int i;
  printf("\nEnter your water intake per day (in litres): \n");
  for (i = 0; i < 7; i++) {
    printf("\nEnter water intake Day %d: ", i + 1);
    scanf("%f", &water[i]);
    if (water[i] < 0) {
      printf("Water intake cannot be negative!\n");
      i--;
      continue;
    }
  }

  printf("\nEnter hours you sleep per day (in hrs): \n");
  for (i = 0; i < 7; i++) {
    printf("\nEnter sleep Day %d: ", i + 1);
    scanf("%f", &sleep[i]);
    if (sleep[i] < 0 || sleep[i] > 24) {
      printf("\n\nEnter hours within 0-24!!");
      i--;
      continue;
    }
  }

  printf("\nEnter your workout time (in hours): \n");
  for (i = 0; i < 7; i++) {
    printf("\nEnter workout duration Day %d: ", i + 1);
    scanf("%f", &workout[i]);
    if (workout[i] < 0 || workout[i] > 24) {
      printf("\n\nEnter hours within 0-24!!");
      i--;
      continue;
    }
  }
}

void calculateAverages(float water[], float sleep[], float workout[],
                       float *avgWater, float *avgSleep, float *avgWorkout) {
  float sumWater = 0, sumSleep = 0, sumWorkout = 0;
  int i;
  for (i = 0; i < 7; i++) {
    sumWater += water[i];
    sumSleep += sleep[i];
    sumWorkout += workout[i];
  }
  *avgWater = sumWater / 7.0;
  *avgSleep = sumSleep / 7.0;
  *avgWorkout = sumWorkout / 7.0;
}

void displaySummary(float water[], float sleep[], float workout[],
                    float avgWater, float avgSleep, float avgWorkout) {
  int i;
  printf("\nDays\t\tWater (L/day)\tSleep (hrs/day)\tWorkout (hrs/day)");
  for (i = 0; i < 7; i++) {
    printf("\nDay %d:\t\t%.2f\t\t%.2f\t\t%.2f", i + 1, water[i], sleep[i],
           workout[i]);
  }
  printf("\n\nAverage:\t\t%.2f\t\t%.2f\t\t%.2f", avgWater, avgSleep,
         avgWorkout);
}

void getAdvise(float avgWater, float avgSleep, float avgWorkout) {
  printf("\n\n\t\t\t\tHealth Advice");
  if (avgWater < 2.0)
    printf("\nIncrease your daily water intake to around 2 liters per day.");
  else
    printf("\nYour water intake is good!");

  if (avgSleep < 8.0)
    printf("\nTry to get at least 8 hours of sleep daily.");
  else
    printf("\nYour sleep hours are sufficient!");

  if (avgWorkout < 0.5)
    printf("\nIncrease workout time to at least 30 minutes per day.");
  else
    printf("\nYour workout routine is good!");
  printf("\n");
}