# Module 01: C# Basics for Backend Development

Welcome to the foundation of ASP.NET Core! ASP.NET Core is built entirely on **C#**, a modern, object-oriented, type-safe programming language developed by Microsoft.

## 1. The .NET Ecosystem
Before writing code, it is important to understand the components that make it run:
* **C#**: The programming language you write.
* **.NET Core / .NET**: The cross-platform, open-source development platform.
* **CLR (Common Language Runtime)**: The execution engine that handles running the application, managing memory (Garbage Collection), and enforcing security.

When you compile C# code, it doesn't compile directly into machine code. It compiles into **IL (Intermediate Language)**, which the CLR then compiles into native machine code at runtime using a **JIT (Just-In-Time) compiler**.

## 2. Basic Syntax & Type System
C# is a **strongly-typed** language. Every variable must have a defined data type.

```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        // Core Data Types
        int age = 22;
        double gpa = 3.8;
        string developerName = "Prasiddhi";
        bool isBackendDeveloper = true;

        Console.WriteLine($"Hello, World! My name is {developerName}.");
    }
}

## 3. Object-Oriented Programming (OOP) in C#

ASP.NET Core relies heavily on OOP paradigms. Here is how the 4 core pillars of OOP look in C#:

### A. Encapsulation
Encapsulation means hiding internal data and exposing it only through public methods or properties. C# uses **Properties** with getters and setters to achieve this elegantly.

```csharp
public class UserProfile
{
    // Private backing field
    private string _email; 

    // Public property with validation logic
    public string Email 
    {
        get { return _email; }
        set 
        {
            if (value.Contains("@"))
                _email = value;
            else
                throw new ArgumentException("Invalid email format");
        }
    }
}
### B. Inheritance & Polymorphism
Inheritance allows a class to inherit members from a parent class. Polymorphism lets a derived class provide a specific implementation of a method defined in its base class using the virtual and override keywords.

C#
// Parent Class
public class BaseController
{
    public virtual void LogRequest()
    {
        Console.WriteLine("Logging generic request details...");
    }
}

// Child Class inheriting from BaseController
public class ApiController : BaseController
{
    // Overriding the parent behavior
    public override void LogRequest()
    {
        Console.WriteLine("Logging specialized API route performance metric...");
    }
}
### C. Abstraction via Interfaces
Interfaces are arguably the most important concept to master for ASP.NET Core because they form the basis of Dependency Injection. An interface defines a contract (what a class should do) without implementing the details (how it does it).

C#
// The Contract
public interface IEmailSender
{
    void SendEmail(string to, string subject, string body);
}

// The Implementation
public class SendGridEmailSender : IEmailSender
{
    public void SendEmail(string to, string subject, string body)
    {
        Console.WriteLine($"Email sent to {to} using SendGrid client API.");
    }
}