import java.util.Scanner;

class StarPrinter {
    // 생성자
    public StarPrinter() {}

    // 메서드: 입력된 숫자만큼 별을 출력하는 메서드
    public void printStars(int n) {
        for (int i = 1; i <= n; i++) {
            // i번째 줄에 i개의 별 출력
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println(); // 개행
        }
    }
}

public class Main {  // 클래스 이름을 Main으로 수정
    public static void main(String[] args) {
        // 사용자로부터 입력 받기
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // StarPrinter 객체 생성 및 별 출력
        StarPrinter starPrinter = new StarPrinter();
        starPrinter.printStars(n);

        scanner.close();
    }
}
