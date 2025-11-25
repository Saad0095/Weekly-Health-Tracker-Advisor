#include <stdio.h>

#define DAYS 7 // constant

void inputData(float water[], float sleep[], float workout[]);
void calculateAverages(float water[], float sleep[], float workout[],
                       float *avgWater, float *avgSleep, float *avgWorkout);
void getAdvice(float avgWater, float avgSleep, float avgWorkout);
void displaySummary(float water[], float sleep[], float workout[],
                    float avgWater, float avgSleep, float avgWorkout);
void mainMenu(float water[], float sleep[], float workout[]);
void saveRecord(float water[], float sleep[], float workout[]);
void viewPastRecords();

// ** Main Function **

int main() {
  float water[DAYS], sleep[DAYS], workout[DAYS];
  mainMenu(water, sleep, workout);
  return 0;
}

// ** Main Menu **

void mainMenu(float water[], float sleep[], float workout[]) {
  int choice;
  float avgWater = 0, avgSleep = 0, avgWorkout = 0;
  printf("\n\nWelcome to Weekly Health Tracker & Advisor!\n\n");
  do {
    printf("\n--- Main Menu ---\n");
    printf("1. Enter/Update Weekly Data\n");
    printf("2. View Summary & Advice\n");
    printf("3. View Previous Records\n");
    printf("4. Exit Program\n");
    printf("Enter your choice (1-4): ");
    scanf("%d", &choice);

    switch (choice) {
    case 1:
      inputData(water, sleep, workout);
      calculateAverages(water, sleep, workout, &avgWater, &avgSleep,
                        &avgWorkout);
      saveRecord(water, sleep, workout);
      printf("\n--- Data Input Completed! ---\n");
      printf("Select option 2 to view the results.\n");
      break;

    case 2:
      if (avgWater == 0 && avgSleep == 0 && avgWorkout == 0) {
        printf("\nNo data found. Please select option 1 first.\n");
      } else {
        displaySummary(water, sleep, workout, avgWater, avgSleep, avgWorkout);
        getAdvice(avgWater, avgSleep, avgWorkout);
      }
      break;

    case 3:
      viewPastRecords();
      break;

    case 4:
      printf("\nProgram Exited successfully!\n");
      break;

    default:
      printf("\nInvalid choice. Please enter 1, 2, or 3.\n");
      break;
    }
  } while (choice != 3);
}

// ** Take inputs **

void inputData(float water[], float sleep[], float workout[]) {
  int i;
  printf("\nEnter your water intake per day (in litres): \n");
  for (i = 0; i < DAYS; i++) {
    printf("\nEnter water intake Day %d: ", i + 1);
    scanf("%f", &water[i]);
    if (water[i] < 0 || water[i] > 6) {
      printf("Water intake cannot be negative or more than 6 litres a day!\n");
      i--;
      continue;
    }
  }

  printf("\nEnter hours you sleep per day (in hrs): \n");
  for (i = 0; i < DAYS; i++) {
    printf("\nEnter sleep Day %d: ", i + 1);
    scanf("%f", &sleep[i]);
    if (sleep[i] < 0 || sleep[i] > 24) {
      printf("\n\nEnter hours within 0-24!!");
      i--;
      continue;
    }
  }

  printf("\nEnter your workout time (in hours): \n");
  for (i = 0; i < DAYS; i++) {
    printf("\nEnter workout duration Day %d: ", i + 1);
    scanf("%f", &workout[i]);
    if (workout[i] < 0 || workout[i] > 24 || (24 - sleep[i] < workout[i])) {
      printf("\n\nEnter hours within 0-%.0f!!", (24 - sleep[i]));
      i--;
      continue;
    }
  }
}

// ** Calculates averages **

void calculateAverages(float water[], float sleep[], float workout[],
                       float *avgWater, float *avgSleep, float *avgWorkout) {
  float sumWater = 0, sumSleep = 0, sumWorkout = 0;
  int i;
  for (i = 0; i < DAYS; i++) {
    sumWater += water[i];
    sumSleep += sleep[i];
    sumWorkout += workout[i];
  }
  *avgWater = sumWater / DAYS;
  *avgSleep = sumSleep / DAYS;
  *avgWorkout = sumWorkout / DAYS;
}

// ** Display weekly summary **
void displaySummary(float water[], float sleep[], float workout[],
                    float avgWater, float avgSleep, float avgWorkout) {
  int i;
  printf("\nDays\t\tWater (L/day)\tSleep (hrs/day)\tWorkout (hrs/day)");
  for (i = 0; i < DAYS; i++) {
    printf("\nDay %d:\t\t%.2f\t\t%.2f\t\t%.2f", i + 1, water[i], sleep[i],
           workout[i]);
  }
  printf("\n\nAverage:\t\t%.2f\t\t%.2f\t\t%.2f", avgWater, avgSleep,
         avgWorkout);
}

// ** Displays Advice **
void getAdvice(float avgWater, float avgSleep, float avgWorkout) {
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

// ** Save Record **

void saveRecord(float water[], float sleep[], float workout[]) {
  FILE *fp = fopen("weekly_records.txt", "a");

  if (fp == NULL) {
    printf("Unable to save file.\n");
    return;
  }

  fprintf(fp, "Start of Week\n");

  for (int i = 0; i < DAYS; i++) {
    fprintf(fp, "%.2f %.2f %.2f\n", water[i], sleep[i], workout[i]);
  }

  fprintf(fp, "End of Week\n\n");

  fclose(fp);
}

// ** View Past Records **

void viewPastRecords() {
  FILE *fp = fopen("weekly_records.txt", "r");
  char line[200];

  if(fp == NULL){
    printf("No records found.\n");
    return;
  }
  
  while (fgets(line, sizeof(line), fp))
  {
    printf("%s", line);
  }
  
  fclose(fp);
}