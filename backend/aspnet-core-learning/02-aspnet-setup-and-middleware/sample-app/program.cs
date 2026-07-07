using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Hosting;
using System;
using System.Threading.Tasks;

namespace SetupAndMiddlewareSample
{
    // Custom Middleware to log request path and execution time
    public class RequestLoggingMiddleware
    {
        private readonly RequestDelegate _next;

        public RequestLoggingMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context)
        {
            // 1. Logic before the next component runs
            string method = context.Request.Method;
            string path = context.Request.Path;
            Console.WriteLine($"[Request Log] Incoming: {method} {path} at {DateTime.UtcNow}");

            // 2. Call the next middleware in the pipeline
            await _next(context);

            // 3. Logic after the next component runs
            Console.WriteLine($"[Request Log] Completed processing for: {path} with Status Code: {context.Response.StatusCode}");
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            var app = builder.Build();

            // Registering our custom middleware in the HTTP pipeline
            app.UseMiddleware<RequestLoggingMiddleware>();

            // A simple default endpoint routing response
            app.MapGet("/", async (context) =>
            {
                await context.Response.WriteAsync("Hello! Look at your terminal console to see the custom logging middleware in action.");
            });

            app.Run();
        }
    }
}