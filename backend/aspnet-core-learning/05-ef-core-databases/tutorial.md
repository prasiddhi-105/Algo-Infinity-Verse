# Module 05: Entity Framework Core (EF Core)

Most backend applications need to store data in a persistent database. **Entity Framework Core (EF Core)** is Microsoft's modern Object-Relational Mapper (ORM) for .NET. It allows you to interact with a database using strongly-typed C# objects, completely eliminating the need to write manual SQL queries for everyday operations.

## 1. Code-First Approach
With the **Code-First** workflow, you write regular C# classes (Entities) first. EF Core then analyzes those classes and automatically generates the corresponding database tables and relationships for you.

### Step A: Define the Entity Model
```csharp
public class Student
{
    public int Id { get; set; } // EF Core automatically recognizes "Id" as the Primary Key
    public string Name { get; set; }
    public string Email { get; set; }
}
Step B: Create the DbContext
The DbContext is the heart of EF Core. It acts as the bridge between your C# code and the database instance, tracking changes and executing queries.

C#
using Microsoft.EntityFrameworkCore;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

    // This property represents the table in the database
    public DbSet<Student> Students { get; set; }
}

### 2. Migrations
When you add a new property or change a class, your database needs to stay updated. Migrations keep track of these data structure changes. You apply them using the following .NET CLI tools in your terminal:

Bash
# 1. Create a migration file tracking your changes
dotnet ef migrations add InitialCreate

# 2. Apply those changes to update the live database structure
dotnet ef database update