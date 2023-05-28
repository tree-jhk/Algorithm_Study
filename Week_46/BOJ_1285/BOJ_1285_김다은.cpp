// 1% 틀림

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> board;
int n;
int answer = 401;
vector<int> reversedCol;

// 행 또는 열 뒤집기. status=1이면 행, 2면 열 뒤집음
void reverse(int rc, int status) {
    for (int i=0; i<n; i++) {
        if (status == 1)
            board[rc][i] = (board[rc][i] + 1) % 2;
        else
            board[i][rc] = (board[i][rc] + 1) % 2;
    }
}

// 열 뒤집어보면서 뒤집었을 때 head가 많아지면 뒤집음
void reverseCol() {
    for (int i=0; i<n; i++) {   // 열
        int cnt[] = {0, 0}; // prev, after
        for (int j=0; j<n; j++) {
            if (board[j][i] == 1) {
                cnt[0]++;
            }
        }
        reverse(i, 2);
        for (int j=0; j<n; j++) {
            if (board[j][i] == 1) {
                cnt[1]++;
            }
        }
        // 뒤집기 전에 head가 더 많다면 다시 뒤집음
        if (cnt[0] > cnt[1]) {
            reverse(i, 2);
        }
        else {
            reversedCol.push_back(i);
        }
    }
}

// 다시 열들을 다시 뒤집음
void rereverseCol() {
    for (int i=0; i<reversedCol.size(); i++) {
        reverse(reversedCol[i], 2);
    }
    reversedCol.clear();
}

void solution(int row) {
    if (row == n) {
        reverseCol();
        int cnt = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == 0) {
                    cnt++;
                }
            }
        }
        answer = min(answer, cnt);
        rereverseCol();
        return;
    }
    reverse(row, 1);
    solution(row + 1);
    reverse(row, 1);
}

int main() {
    cin >> n;
    board.resize(n, vector<int>(n, 0));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            char tmp;
            cin >> tmp;
            // head : 1, tail : 0
            if (tmp == 'H')
                board[i][j] = 1;
            else
                board[i][j] = 0;
        }
    }
    for (int i=0; i<n; i++) {
        solution(i);
    }
    cout << answer << "\n";
}