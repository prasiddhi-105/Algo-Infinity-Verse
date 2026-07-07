using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.DependencyInjection;
using System.Collections.Generic;

namespace MvcAndRazorPagesSample
{
    // 1. The Model representing structured application data
    public class Course
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Difficulty { get; set; }
    }

    // 2. The Controller orchestrating routing and presentation
    public class LearningController : Controller
    {
        // GET: /Learning/Courses
        public IActionResult Courses()
        {
            var activeTracks = new List<Course>
            {
                new Course { Id = 1, Title = "C# Basics", Difficulty = "Easy" },
                new Course { Id = 2, Title = "ASP.NET Setup & Middleware", Difficulty = "Medium" },
                new Course { Id = 3, Title = "MVC & Razor Pages Architecture", Difficulty = "Medium" }
            };

            // In a full application, this would pass to a .cshtml view engine file.
            // For this sandbox console preview, we simulate returning the view dataset.
            return Json(new { ViewName = "CoursesView", ModelData = activeTracks });
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Instructing framework services to enable full Controller handling
            builder.Services.AddControllersWithViews();

            var app = builder.Build();

            // Setup traditional routing configuration scheme
            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Learning}/{action=Courses}/{id?}");

            app.Run();
        }
    }
}
