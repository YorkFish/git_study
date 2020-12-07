#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize < 2) return 0;
    int tmp = maxProfit(prices, pricesSize-1);
    int max = tmp < 0 ? 0 : tmp;
    for (int i = 0; i < pricesSize-1; i++) {
        int sum = maxProfit(prices, i+1) + (prices[pricesSize-1] - prices[i]);
        if (max < sum) max = sum;
    }
    return max;
}

int main() {
    int prices[6] = {7, 1, 5, 3, 6, 4};
    printf(">>> maxProfit(prices, 6) = %d\n", maxProfit(prices, 6));

    return 0;
}
