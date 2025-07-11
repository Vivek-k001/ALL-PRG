public class ArrayDemo {
    public static void main(String[] args) {
        int[] marks = {85, 90, 78, 88, 95};

        // Print all marks
        for(int i = 0; i < marks.length; i++) {
            System.out.println("Mark " + (i + 1) + ": " + marks[i]);
        }
    }
}
