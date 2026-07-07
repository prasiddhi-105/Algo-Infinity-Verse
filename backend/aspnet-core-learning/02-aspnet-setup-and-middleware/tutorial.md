# Module 02: ASP.NET Core Setup & Middleware

Now that we understand C# basics, let's look at how an ASP.NET Core web application initializes and processes incoming HTTP requests.

## 1. Project Initialization & Structure
When you create a web application using the .NET CLI command `dotnet new web`, a minimalistic backend server structure is generated. 

The entry point of the application is **Program.cs**. This single file is responsible for configuration, setting up services, and defining the middleware pipeline.

```csharp
var builder = WebApplication.CreateBuilder(args);

// 1. Add services to the container (Dependency Injection setup)
builder.Services.AddControllers(); 

var app = builder.Build();

// 2. Configure the HTTP request pipeline (Middleware)
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}

app.UseHttpsRedirection();
app.UseRouting();
app.UseAuthorization();

// 3. Map endpoints
app.MapControllers();

app.Run();
### 2. The Middleware Pipeline
Middleware is software components assembled into an application pipeline to handle requests and responses. Each component:  

Chooses whether to pass the request to the next component in the pipeline.  

Can perform work before and after the next component is invoked.  

Incoming Request ──> [Middleware A] ──> [Middleware B] ──> [Routing/Endpoint]
                                                                  │
Outgoing Response <── [Middleware A] <── [Middleware B] <─────────┘
For example, if an unauthorized user sends a request, the UseAuthorization() middleware can short-circuit the pipeline immediately and return a 401 Unauthorized status code without letting the request reach your database or controller