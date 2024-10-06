import java.util.Scanner;

class StarPrinter {
    public StarPrinter() {}

    public void printStars(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        StarPrinter starPrinter = new StarPrinter();
        starPrinter.printStars(n);

        scanner.close();
    }
}
