using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Authorization;

namespace AuthenticationAuthorizationSample
{
    // 1. Secure Resource Controller
    [ApiController]
    [Route("api/[controller]")]
    public class AdminPanelController : ControllerBase
    {
        [HttpGet("public-announcement")]
        public IActionResult GetAnnouncement()
        {
            return Ok("Welcome to the student learning portal!");
        }

        [HttpGet("secure-vault")]
        [Authorize] // 🔒 Requires a verified, valid authentication token header
        public IActionResult GetSecretData()
        {
            return Ok("Confidential database access granted via verified token.");
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // 2. Add Security Services to the Container Pipeline
            builder.Services.AddAuthentication(options =>
            {
                options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
            })
            .AddJwtBearer(options =>
            {
                // Configuration rules for validating incoming cryptographic token payloads
                options.Authority = "https://auth.example.com";
                options.Audience = "api://learning-portal";
            });

            builder.Services.AddAuthorization();
            builder.Services.AddControllers();

            var app = builder.Build();

            app.UseRouting();

            // 3. Authenticate first, then Authorize rights
            app.UseAuthentication(); 
            app.UseAuthorization();  

            app.MapControllers();

            app.Run();
        }
    }
}
