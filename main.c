#include <stdio.h>
void inputData(float water[], float sleep[], float workout[]);
void calculateAverages(float water[], float sleep[], float workout[]);
void getAdvise(float avgWater, float avgSleep, float avgWorkout);
void displaySummary(float avgWater, float avgSleep, float avgWorkout);
void mainMenu(float water[], float sleep[], float workout[]);

int main() {
  float water[7], sleep[7], workout[7];
  mainMenu(water, sleep, workout);

  return 0;
}

void mainMenu(float water[], float sleep[], float workout[]) {
  int choice;
  char ch;
  do {
    printf("\n\nWelcome to Weekly Health Tracker & Advisor!\n\n");
    printf("Do you want to track your progress (Y/N): ");
    scanf(" %c", &ch);

    if (ch != 'Y' && ch != 'y') {
      printf("Exiting program...\n");
      break;
    }
    inputData(water, sleep, workout);

  } while (1);
}

void inputData(float water[], float sleep[], float workout[]) {
  int i;
  printf("\nEnter your water intake per day (in litres): \n");
  for (i = 0; i < 7; i++) {
    if (water[i] < 0) {
      printf("Water intake cannot be negative!\n");
      i--;
      continue;
    }
    printf("Enter intake Day %d: ", i + 1);
    scanf("%f", &water[i]);
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
  calculateAverages(water, sleep, workout);
}

void calculateAverages(float water[], float sleep[], float workout[]) {
  float avgWater = 0, avgSleep = 0, avgWorkout = 0;
  int i;
  for (i = 0; i < 7; i++) {
    avgWater += water[i];
    avgSleep += sleep[i];
    avgWorkout += workout[i];
  }
  avgWater /= 7.0;
  avgSleep /= 7.0;
  avgWorkout /= 7.0;

  displaySummary(avgWater, avgSleep, avgWorkout);
  getAdvise(avgWater, avgSleep, avgWorkout);
}

void displaySummary(float avgWater, float avgSleep, float avgWorkout) {
  printf("\n\n\t\t\t\tYour Weekly Report:");
  printf("\n\nWater consumed this week: %.2f liters\nWater consumed on average "
         "daily: %.2f liters",
         (avgWater * 7), avgWater);
  printf("\n\nSleep taken this week: %.2f hours\nSleep taken on average daily: "
         "%.2f hours",
         (avgSleep * 7), avgSleep);
  printf("\n\nTotal workout this week: %.2f hours\nTotal workout on average "
         "daily: %.2f hours",
         (avgWorkout * 7), avgWorkout);
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
}