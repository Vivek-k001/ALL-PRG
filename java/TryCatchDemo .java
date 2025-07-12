import java.util.Scanner;

public class TryCatchDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter a number: ");
            int num = sc.nextInt(); // May throw exception if not a number
            System.out.println("You entered: " + num);
        } catch(Exception e) {
            System.out.println("Invalid input! Please enter a number.");
        }
    }
}
