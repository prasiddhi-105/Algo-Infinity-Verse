### Practice Exercises (`exercises/README.md`)
Create a sub-folder structure `exercises/` inside Module 05 and add a `README.md` with this task:

```markdown
# Module 05 Exercises: EF Core

### Exercise 1: Course Enrollment Table Extension
* **Goal**: Add a new entity model to the DbContext structure.
* **Requirements**: 
    * Create a new C# class named `Course` containing properties for `Id` (integer), `Title` (string), and `Credits` (integer).
    * Add this model as a new `DbSet<Course>` collection within the `ApplicationDbContext` class.
    * Write down the exact two terminal CLI commands you would run to generate a migration titled `AddCourseTable` and apply it to the database safely.