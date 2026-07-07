# ASP.NET Core Learning Track: Final Quiz

Test your knowledge on backend development with C# and ASP.NET Core. Review the questions below and select the correct answers.

---

### Question 1: C# Type System
**What does it mean that C# is a "strongly-typed" language?**
- [ ] A) Variables can dynamically change their data type at runtime.
- [ ] B) Every variable and constant must have a declared, explicit, or inferred data type verified at compile-time.
- [ ] C) The language only supports integer and string primitive types.

### Question 2: Middleware Pipeline
**How does the ASP.NET Core Middleware pipeline process an incoming HTTP request?**
- [ ] A) It executes all components simultaneously in parallel threads.
- [ ] B) It processes components sequentially, where each piece of middleware can execute logic both before and after the next component is invoked.
- [ ] C) It skips straight to the database layer without checking authorization rules.

### Question 3: Dependency Injection
**Which service lifetime instantiation rule creates a new instance *once per individual HTTP request context*?**
- [ ] A) Transient
- [ ] B) Singleton
- [ ] C) Scoped

### Question 4: Entity Framework Core
**In an EF Core Code-First workflow, what is the purpose of running a "Migration"?**
- [ ] A) To move the hosted application from an on-premise server to a cloud provider.
- [ ] B) To generate a historical tracking file that syncs structural modifications made to C# entity classes directly into database tables.
- [ ] C) To convert JSON API request datasets into HTML view templates.

### Question 5: Authentication vs Authorization
**A user attempts to delete a record and receives an HTTP 403 Forbidden status code because they lack the "Admin" role. Which security phase blocked this request?**
- [ ] A) Authentication
- [ ] B) Authorization
- [ ] C) Resource Publishing

---
## Answer Key Reference
1. **B** | 2. **B** | 3. **C** | 4. **B** | 5. **B**