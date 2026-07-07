# Module 06: Authentication & Authorization

Securing endpoints is a foundational part of modern backend engineering. ASP.NET Core splits security into two distinct phases:

1. **Authentication (Who are you?)**: Verifying identity (e.g., matching a username and password, or validating a signed cryptographic token).
2. **Authorization (What are you allowed to do?)**: Verifying permissions or roles (e.g., checking if an authenticated user is an "Admin" before allowing them to delete data).

## 1. Token-Based Authentication (JWT)
In modern web applications and APIs, stateless **JSON Web Tokens (JWT)** are widely used. 
* A user logs in with their credentials.
* The server verifies them and issues a signed, cryptographically secure JWT string.
* The client sends this token inside the HTTP `Authorization: Bearer <token>` header for all subsequent requests.

## 2. Securing Routes with Attributes
ASP.NET Core makes protecting controllers completely declarative via attributes.

### Securing an entire Controller:
```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
[Authorize] // 🔒 Every endpoint inside this controller now requires a valid JWT
public class SecureDashboardController : ControllerBase
{
    [HttpGet("metrics")]
    public IActionResult GetMetrics()
    {
        return Ok("Sensitive management metrics dashboard data.");
    }

    [HttpDelete("purge")]
    [Authorize(Roles = "Admin")] // ❌ Only authenticated users with the 'Admin' role can run this
    public IActionResult DeleteAllRecords()
    {
        return Ok("Database purged successfully.");
    }
}
