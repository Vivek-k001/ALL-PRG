// File: InheritanceExample.java

// Parent class
class Animal {
    String name;

    // Constructor
    Animal(String name) {
        this.name = name;
    }

    // Method
    void makeSound() {
        System.out.println(name + " makes a sound.");
    }
}

// Child class
class Dog extends Animal {
    String breed;

    // Constructor
    Dog(String name, String breed) {
        super(name); // Call parent constructor
        this.breed = breed;
    }

    // Additional method in child
    void bark() {
        System.out.println(name + " is a " + breed + " and it barks!");
    }
}

// Main class with main method
public class InheritanceExample {
    public static void main(String[] args) {
        Dog myDog = new Dog("Tommy", "Labrador");

        // Call methods
        myDog.makeSound(); // inherited from Animal
        myDog.bark();      // defined in Dog
    }
}
