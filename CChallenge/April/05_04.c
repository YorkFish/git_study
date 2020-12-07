#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    int ans = 0;
    int min = prices[0];
    int max = prices[0];
    for (int i = 0; i < pricesSize; i++) {
        if (max <= prices[i]) {  // 有最大值就替换
            max = prices[i];
            if (prices[i] < min) {  // 有最小值就替换
                min = prices[i];
            }
        }
        else {  // 算上一轮
            ans += max - min;
            min = max = prices[i];
        }
        if (i == pricesSize - 1 && max - min > 0)  // 算最后一轮
            ans += max - min;
    }

    return ans;
}

int main() {
    int prices[6] = {7, 1, 5, 3, 6, 4};
    printf(">>> maxProfit(prices, 6) = %d\n", maxProfit(prices, 6));

    return 0;
}
