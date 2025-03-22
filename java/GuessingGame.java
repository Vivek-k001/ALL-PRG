import java.util.Random;
import java.util.Scanner;

public class GuessingGame {
    public static void main (String[]args) {
        Random random = new Random();
        int numberToGuess = random.nextInt(10) + 1;
        int numberOfTries = 0;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Guess a number between 1 and 10");
        
        while (true) {
            int guess = scanner.nextInt();
            nummberOfTries++;

            if(guess == numberToGuess) {
                System.out.println("Coongratulations! you found the number in " + numberOfTries = "tries..");
                break;
            } else if (guess < numberToGuess) {
                System.out.println("Your guess is too low..Try agaim..");
            } else {
                System.out.println("Your guess is too high.. Try agian!");
            }
        }
    }
}