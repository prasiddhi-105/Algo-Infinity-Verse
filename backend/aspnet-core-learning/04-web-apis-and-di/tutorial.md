# Module 04: Web APIs & Dependency Injection

Modern software relies heavily on decoupled APIs that communicate using JSON payloads. ASP.NET Core makes building these fast, secure, and manageable via **Dependency Injection**.

## 1. Dependency Injection (DI)
Dependency Injection is a design pattern used to achieve Inversion of Control (IoC) between classes and their dependencies. Instead of a class creating instances of its dependencies using the `new` keyword, dependencies are provided (injected) at runtime, usually through the constructor.
### Service Lifetimes
When registering a service in `Program.cs`, you must choose a lifetime:
* **Transient**: Created each time they are requested. Best for lightweight, stateless services.
* **Scoped**: Created once per client request (HTTP connection). Ideal for database contexts.
* **Singleton**: Created the first time they are requested and stay alive for the entire lifecycle of the application.

```csharp
// Registering services in Program.cs
builder.Services.AddTransient<IEmailService, EmailService>();

### 2. Web APIs
Web APIs handle endpoints that return structured JSON data instead of UI views. Controllers inherit from ControllerBase and are decorated with [ApiController] attributes to enable smart binding and validation rules.

Sample API Controller with Injected Service:
C#
[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    private readonly IUserService _userService;

    // Injecting the required service through the constructor
    public UsersController(IUserService userService)
    {
        _userService = userService;
    }

    [HttpGet]
    public IActionResult GetAllUsers()
    {
        var users = _userService.GetUsersList();
        return Ok(users); // Returns HTTP 200 with JSON payload
    }
}