import java.util.Scanner;

public class hi {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        System.out.print("enter Your name: ");
        String name = sc.nextLine();

        System.out.print("ener your age: ");
        int age = sc.nextInt();

        System.out.println("Hello " + name + " ! your are " + age + " years old");

        sc.close();
}
}