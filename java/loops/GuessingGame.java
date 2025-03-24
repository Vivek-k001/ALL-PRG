import java.util.Scanner;

public class GuessingGame {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int secretNumber = 7;
        int guess;


        do {
            System.out.print("Guess a number between 1 and 10 :" );
            guess = sc.nextInt();
        } while (guess != secretNumber);

        System.out.println("Congratulatios !!! you guesses the right number !!");

        sc.close();
    }
}