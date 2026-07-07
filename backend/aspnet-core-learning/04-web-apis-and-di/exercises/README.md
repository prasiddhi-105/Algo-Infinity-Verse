### Practice Exercises (`exercises/README.md`)
Create the sub-folder structure `exercises/` inside Module 04 and add a `README.md` containing this challenge:

```markdown
# Module 04 Exercises: Web APIs and DI

### Exercise 1: Task Management API Endpoint
* **Goal**: Inject a repository service into an API controller.
* **Requirements**: 
    * Define an interface `ITaskRepository` containing a method `List<string> GetAllTasks()`.
    * Implement a mock class `MockTaskRepository` that fulfills the contract.
    * Register it as a **Scoped** service in the configuration container.
    * Build a `TasksController` API endpoint that injects this repository and outputs the tasks array on a `GET` request.
    