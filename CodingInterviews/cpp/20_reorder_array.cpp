#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        int left = 0, right = array.size() - 1;
        while (left < right)
        {
            while (array[left] % 2 == 1) left ++ ;
            while (array[right] % 2 == 0) right -- ;
            if (left < right) swap(array[left], array[right]);
        }
    }
};

int main() {
    vector<int> array{1, 2, 3, 4, 5};
    Solution s;
    s.reOrderArray(array);
    for (int x : array) cout << x << ' ';
    cout << endl;

    return 0;
}
