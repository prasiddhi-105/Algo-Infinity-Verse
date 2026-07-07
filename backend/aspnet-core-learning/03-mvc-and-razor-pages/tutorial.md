# Module 03: MVC Architecture & Razor Pages

ASP.NET Core provides two primary ways to build server-rendered user interfaces: **MVC (Model-View-Controller)** and **Razor Pages**.

## 1. MVC Architecture
MVC is an architectural pattern that separates an application into three main components:
* **Model**: Represents the shape of the data and business logic (e.g., a `Product` class).
* **View**: The user interface displayed to the user (written in `.cshtml` files using HTML and Razor syntax).
* **Controller**: Handles user requests, interacts with the Model, and selects a View to render.

### A Sample MVC Controller:
```csharp
public class ProductController : Controller
{
    // GET: /Product/Details/5
    public IActionResult Details(int id)
    {
        Product product = new Product { Id = id, Name = "Laptop", Price = 999.99 };
        return View(product); // Passes the model data to the View
    }
}
### 2. Razor Pages
While MVC works perfectly for massive applications, it can sometimes feel scattered with files split between three folders. Razor Pages is a page-focused alternative that groups the UI logic and presentation together.

Instead of a Controller class, a Razor Page uses a PageModel class file code-behind (Page.cshtml.cs) attached directly to the visual structure (Page.cshtml).

A Sample Razor PageModel (Index.cshtml.cs):
C#
public class IndexModel : PageModel
{
    public string WelcomeMessage { get; set; }

    public void OnGet()
    {
        WelcomeMessage = "Welcome to our Razor Pages learning module!";
    }
}