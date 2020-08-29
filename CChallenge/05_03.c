#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    int total = 0;
    for (int i = 0; i < pricesSize-1; i++) {
        if (prices[i] < prices[i+1]) {
            total += prices[i+1] - prices[i];
        }
    }
    return total;
}

int main() {
    int prices[6] = {7, 1, 5, 3, 6, 4};
    printf(">>> maxProfit(prices, 6) = %d\n", maxProfit(prices, 6));

    return 0;
}
