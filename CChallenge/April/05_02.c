#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize < 2) return 0;
    int profits[pricesSize+1];
    profits[1] = 0;
    for (int i = 2; i < pricesSize+1; i++) {
        int profit = profits[i-1];
        int max = profit;
        for (int j = 1; j < i; j++) {
            profit = profits[j] + prices[i-1] - prices[j-1];
            if (max < profit) max = profit;
        }
        profits[i] = max;
    }
    return profits[pricesSize];
}

int main() {
    int prices[6] = {7, 1, 5, 3, 6, 4};
    printf(">>> maxProfit(prices, 6) = %d\n", maxProfit(prices, 6));

    return 0;
}
