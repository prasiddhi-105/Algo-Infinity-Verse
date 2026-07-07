using System;
using System.Collections.Generic;

namespace CSharpBasicsSample
{
    // 1. Interface (Abstraction)
    public interface INotificationService
    {
        void Send(string message);
    }

    // 2. Implementation of Interface
    public class ConsoleNotificationService : INotificationService
    {
        public void Send(string message)
        {
            Console.WriteLine($"[Notification] {message}");
        }
    }

    // 3. Base Class (Inheritance)
    public class Account
    {
        public string Owner { get; set; }
        protected double Balance { get; set; } // Accessible by derived classes

        public Account(string owner, double initialBalance)
        {
            Owner = owner;
            Balance = initialBalance;
        }

        public virtual void DisplayInfo()
        {
            Console.WriteLine($"Account Owner: {Owner}, Balance: ${Balance}");
        }
    }

    // 4. Derived Class (Polymorphism & Encapsulation)
    public class SavingsAccount : Account
    {
        private double _interestRate; // Encapsulated field

        public SavingsAccount(string owner, double initialBalance, double interestRate) 
            : base(owner, initialBalance)
        {
            _interestRate = interestRate;
        }

        // Overriding base method (Polymorphism)
        public override void DisplayInfo()
        {
            Console.WriteLine($"Savings Account Owner: {Owner}, Balance: ${Balance}, Interest Rate: {_interestRate}%");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("--- Running C# Basics Sample Application ---\n");

            // Using the polymorphic class structures
            Account genericAccount = new Account("Alice", 1000.00);
            Account savingsAccount = new SavingsAccount("Bob", 2500.00, 4.5);

            genericAccount.DisplayInfo();
            savingsAccount.DisplayInfo();

            Console.WriteLine("\n--- Triggering Notification Service ---");
            // Using the interface
            INotificationService notifier = new ConsoleNotificationService();
            notifier.Send("C# Basics sample app executed successfully!");
        }
    }
}