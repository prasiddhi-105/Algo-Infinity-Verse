## 4. Practice Exercises

To complete the acceptance criteria for this first module, let's create an `exercises/` folder inside `01-csharp-basics/` and add a `README.md` containing these practice challenges for the learners:

### Exercise 1: The Banking System (Encapsulation & OOP)
* **Goal**: Create a `BankAccount` class.
* **Requirements**: 
    * It should have private fields for `AccountNumber` and `Balance`.
    * Provide a public method `Deposit(double amount)` and `Withdraw(double amount)`.
    * Prevent withdrawals if the amount exceeds the current balance.

### Exercise 2: The Notification Engine (Interfaces)
* **Goal**: Implement a basic notification system.
* **Requirements**:
    * Define an interface `INotificationService` with a method `void SendNotification(string message)`.
    * Implement two classes that realize this interface: `SmsNotificationService` and `PushNotificationService`.
    * In your main execution loop, call both using a list of type `List<INotificationService>`.