using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace EfCoreDatabasesSample
{
    // 1. The Entity Model (Database Table Structure)
    public class ProductItem
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public double Price { get; set; }
    }

    // 2. The Database Context Session Bridge
    public class InventoryDbContext : DbContext
    {
        public InventoryDbContext(DbContextOptions<InventoryDbContext> options) : base(options) { }

        public DbSet<ProductItem> Products { get; set; }
    }

    // 3. API Controller managing Data Persistent Actions
    [ApiController]
    [Route("api/[controller]")]
    public class InventoryController : ControllerBase
    {
        private readonly InventoryDbContext _context;

        public InventoryController(InventoryDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<IActionResult> GetAvailableProducts()
        {
            // Using LINQ to query the database collection context safely
            var items = await _context.Products
                                     .Where(p => p.Price > 0)
                                     .OrderBy(p => p.Name)
                                     .ToListAsync();
            return Ok(items);
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // 4. Register DbContext using an In-Memory Database provider for sandbox execution
            builder.Services.AddDbContext<InventoryDbContext>(options =>
                options.UseInMemoryDatabase("SandboxInventoryDb"));

            builder.Services.AddControllers();

            var app = builder.Build();

            app.UseRouting();
            app.MapControllers();

            app.Run();
        }
    }
}
