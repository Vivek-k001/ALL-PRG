import java.util.Scanner;

public class JacketDecision {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Eneter the temperature : ");
        int temperature = sc.nextInt();

        if (temperature < 20) {
            System.out.println("its cold !! Wear a jacket ");
    }

    System.out.println("Enjoy your day !!");
    sc.close();
    }
}