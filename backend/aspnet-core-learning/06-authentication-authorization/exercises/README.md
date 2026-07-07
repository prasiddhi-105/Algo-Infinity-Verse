### Practice Exercises (`exercises/README.md`)
Create a sub-folder structure `exercises/` inside Module 06 and add a `README.md` with this task:

```markdown
# Module 06 Exercises: Security

### Exercise 1: Role-Based Routing Safeguard
* **Goal**: Protect a specialized management API route.
* **Requirements**: 
    * Set up a mock `SettingsController`.
    * Apply metadata rules so that generic authenticated users can execute an HTTP `GET` to view configuration settings.
    * Restrict HTTP `POST` modification queries completely so that only users bound to a verified `"Manager"` role can update settings.