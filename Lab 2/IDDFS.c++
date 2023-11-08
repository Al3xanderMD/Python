#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

class Puzzle {
public:
    int Board[3][3];
    int EmptyRow;
    int EmptyCol;

    Puzzle(const int board[3][3]) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                Board[i][j] = board[i][j];
                if (board[i][j] == 0) {
                    EmptyRow = i;
                    EmptyCol = j;
                }
            }
        }
    }

    bool IsFinalState() {
        int value = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (Board[i][j] == 0) {
                    continue;
                }
                if (Board[i][j] != value % (3 * 3)) {
                    return false;
                }
                value++;
            }
        }
        return true;
    }

    // Custom comparison operator for Puzzle
    bool operator<(const Puzzle& other) const {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (Board[i][j] != other.Board[i][j]) {
                    return Board[i][j] < other.Board[i][j];
                }
            }
        }
        return false; // Boards are equal
    }
};

class PuzzleSolver {
public:
    std::vector<Puzzle> Solve(Puzzle initial, int maxDepth) {
        for (int depth = 0; depth <= maxDepth; depth++) {
            std::map<Puzzle, Puzzle> cameFrom;
            std::vector<Puzzle> solution;
            bool foundSolution = DepthLimitedSearch(initial, depth, cameFrom, solution);

            if (foundSolution) {
                std::reverse(solution.begin(), solution.end());
                return solution;
            }
        }

        return std::vector<Puzzle>();
    }

private:
    bool DepthLimitedSearch(Puzzle state, int depth, std::map<Puzzle, Puzzle>& cameFrom, std::vector<Puzzle>& solution) {
        if (depth == 0 && state.IsFinalState()) {
            solution.push_back(state);
            return true;
        }

        if (depth > 0) {
            for (Puzzle neighbor : GetValidTransitions(state)) {
                if (cameFrom.find(neighbor) == cameFrom.end()) {
                    cameFrom[neighbor] = state;
                    if (DepthLimitedSearch(neighbor, depth - 1, cameFrom, solution)) {
                        solution.push_back(state);
                        return true;
                    }
                }
            }
        }

        return false;
    }

    std::vector<Puzzle> GetValidTransitions(Puzzle state) {
        int dr[] = { -1, 1, 0, 0 };
        int dc[] = { 0, 0, -1, 1 };
        std::vector<Puzzle> transitions;

        for (int i = 0; i < 4; i++) {
            int newRow = state.EmptyRow + dr[i];
            int newCol = state.EmptyCol + dc[i];

            if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
                int newBoard[3][3];
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        newBoard[i][j] = state.Board[i][j];
                    }
                }
                newBoard[state.EmptyRow][state.EmptyCol] = state.Board[newRow][newCol];
                newBoard[newRow][newCol] = 0;
                transitions.push_back(Puzzle(newBoard));
            }
        }

        return transitions;
    }
};

void PrintPuzzleState(const int state[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << state[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int initialState[3][3] = {
        {2, 5, 3},
        {0, 1, 6},
        {4, 7, 8}
    };

    Puzzle initialPuzzle(initialState);
    int maxDepth = 30;

    PuzzleSolver solver;
    std::vector<Puzzle> solution = solver.Solve(initialPuzzle, maxDepth);

    if (!solution.empty()) {
        std::cout << "Solution found!" << std::endl;

        for (int i = 0; i < solution.size(); i++) {
            std::cout << "Step " << i << ":" << std::endl;
            PrintPuzzleState(solution[i].Board);
            std::cout << std::endl;
        }
    }
    else {
        std::cout << "No solution found." << std::endl;
    }

    return 0;
}
