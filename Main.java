public class Main {
    public static void main(String[] args) {
        // Print a message to the console
        System.out.println("Hello, World!");

        // Variables and data types
        int myInt = 10;
        double myDouble = 5.5;
        char myChar = 'A';
        boolean myBool = true;
        String myString = "Java Basics";

        // Print variables
        System.out.println("Integer: " + myInt);
        System.out.println("Double: " + myDouble);
        System.out.println("Character: " + myChar);
        System.out.println("Boolean: " + myBool);
        System.out.println("String: " + myString);

        // Conditional statements
        if (myInt > 5) {
            System.out.println("myInt is greater than 5");
        } else {
            System.out.println("myInt is not greater than 5");
        }

        // Loops
        for (int i = 0; i < 5; i++) {
            System.out.println("For loop iteration: " + i);
        }

        int j = 0;
        while (j < 5) {
            System.out.println("While loop iteration: " + j);
            j++;
        }

        // Arrays
        int[] myArray = {1, 2, 3, 4, 5};
        for (int num : myArray) {
            System.out.println("Array element: " + num);
        }

        // Methods
        int sum = addNumbers(5, 10);
        System.out.println("Sum of 5 and 10 is: " + sum);
    }

    // Method to add two numbers
    public static int addNumbers(int a, int b) {
        return a + b;
    }
}