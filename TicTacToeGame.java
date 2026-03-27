import java.util.Random;

public class TicTacToeGame {
    private static final int SIZE = 3;
    private char[][] board;
    private char currentPlayer;

    public TicTacToeGame() {
        board = new char[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                board[i][j] = ' ';
            }
        }
        currentPlayer = 'X';
    }

    public void printBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
        }
    }

    public boolean makeMove(int row, int col) {
        if (row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == ' ') {
            board[row][col] = currentPlayer;
            return true;
        }
        return false;
    }

    public boolean checkWin(char player) {
        for (int i = 0; i < SIZE; i++) {
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
                (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
                return true;
            }
        }
        if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
            (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
            return true;
        }
        return false;
    }

    public boolean checkDraw() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

    public void switchPlayer() {
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    public char getCurrentPlayer() {
        return currentPlayer;
    }

    public static void main(String[] args) {
        TicTacToeGame game = new TicTacToeGame();
        Random random = new Random();

        while (true) {
            game.printBoard();

            if (game.getCurrentPlayer() == 'X') {
                System.out.println("Player X's turn. Enter row and column (0-2): ");
                int row = random.nextInt(SIZE);
                int col = random.nextInt(SIZE);
                while (!game.makeMove(row, col)) {
                    row = random.nextInt(SIZE);
                    col = random.nextInt(SIZE);
                }
            } else {
                System.out.println("Player O's turn. Enter row and column (0-2): ");
                int row = random.nextInt(SIZE);
                int col = random.nextInt(SIZE);
                while (!game.makeMove(row, col)) {
                    row = random.nextInt(SIZE);
                    col = random.nextInt(SIZE);
                }
            }

            if (game.checkWin(game.getCurrentPlayer())) {
                game.printBoard();
                System.out.println("Player " + game.getCurrentPlayer() + " wins!");
                break;
            } else if (game.checkDraw()) {
                game.printBoard();
                System.out.println("It's a draw!");
                break;
            }

            game.switchPlayer();
        }
    }
}
