### Practice Exercises (`exercises/README.md`)
Create an `exercises/README.md` file inside the `02-aspnet-setup-and-middleware` directory to give learners a quick challenge:

```markdown
# Module 02 Exercises: Middleware

### Exercise 1: Request Logging Middleware
* **Goal**: Write a custom inline middleware using `app.Use()`.
* **Requirements**: 
    * Intercept every HTTP request.
    * Log the HTTP Method (GET, POST, etc.) and the Path requested to the console using `Console.WriteLine()`.
    * Ensure the request successfully continues to the next middleware in line.