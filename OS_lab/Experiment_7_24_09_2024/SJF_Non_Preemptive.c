#include <stdio.h>

int main() {
    int n;
    
    printf("Enter number of processes: ");
    scanf("%d", &n);
    
    int arrivalTime[n], burstTime[n], waitingTime[n], turnAroundTime[n], completionTime[n], responseTime[n];
    int visited[n], currentTime = 0, completed = 0;
    float totalWT = 0, totalTAT = 0;

    for (int i = 0; i < n; i++) {
        printf("Enter Arrival Time for Process %d: ", i + 1);
        scanf("%d", &arrivalTime[i]);
        printf("Enter Burst Time for Process %d: ", i + 1);
        scanf("%d", &burstTime[i]);
        visited[i] = 0;
    }

    while (completed != n) {
        int minBT = 10000, minIndex = -1;

        for (int i = 0; i < n; i++) {
            if (arrivalTime[i] <= currentTime && visited[i] == 0) {
                if (burstTime[i] < minBT) {
                    minBT = burstTime[i];
                    minIndex = i;
                }
            }
        }

        if (minIndex == -1) {
            currentTime++;
        } else {
            visited[minIndex] = 1;
            responseTime[minIndex] = currentTime - arrivalTime[minIndex];
            completionTime[minIndex] = currentTime + burstTime[minIndex];
            waitingTime[minIndex] = responseTime[minIndex];
            turnAroundTime[minIndex] = completionTime[minIndex] - arrivalTime[minIndex];
            currentTime += burstTime[minIndex];
            completed++;
            totalWT += waitingTime[minIndex];
            totalTAT += turnAroundTime[minIndex];
        }
    }

    printf("\nProcess\tAT\tBT\tRT\tWT\tTAT\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", i + 1, arrivalTime[i], burstTime[i], responseTime[i], waitingTime[i], turnAroundTime[i]);
    }

    printf("\nAverage Waiting Time: %.2f", totalWT / n);
    printf("\nAverage Turnaround Time: %.2f\n", totalTAT / n);

    return 0;
}

/*

Output

Enter number of processes: 5
Enter Arrival Time for Process 1: 3
Enter Burst Time for Process 1: 1
Enter Arrival Time for Process 2: 1
Enter Burst Time for Process 2: 4
Enter Arrival Time for Process 3: 4
Enter Burst Time for Process 3: 2
Enter Arrival Time for Process 4: 0
Enter Burst Time for Process 4: 6
Enter Arrival Time for Process 5: 2
Enter Burst Time for Process 5: 3

Process AT      BT      RT      WT      TAT
1       3       1       3       3       4
2       1       4       11      11      15
3       4       2       3       3       5
4       0       6       0       0       6
5       2       3       7       7       10

Average Waiting Time: 4.80
Average Turnaround Time: 8.00
*/