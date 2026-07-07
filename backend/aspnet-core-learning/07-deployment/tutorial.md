# Module 07: Deployment

Once your application is written and tested, the final step is compiling it into an optimized, self-contained package and hosting it on a live production server.

### 1. Production Publishing
During development, you run your app using `dotnet run` or `dotnet watch`. However, for production hosting, you need to compile optimized, pre-compiled binaries using the `dotnet publish` command:

dotnet publish -c Release -o ./publish
-c Release: Compiles code with optimizations turned on and debugging symbols stripped out.

-o ./publish: Outputs the clean, deployment-ready assets into a folder named publish.

### 2. Hosting Strategies

ASP.NET Core comes built-in with a lightweight, high-performance web server called Kestrel. In production environments, it is best practice to place Kestrel behind a fully-featured Reverse Proxy (like Nginx, Apache, or IIS) to handle SSL termination, traffic routing, and load balancing.

### Popular Hosting Options:

1. **Cloud Container Hosting (Docker/Kubernetes)**: Packaging the app into a lightweight container image to run anywhere.
2. **PaaS (Platform as a Service)**: Direct deployment to managed platforms like Azure App Services or AWS Elastic Beanstalk.
3. **Linux Virtual Machines**: Running the compiled binary as a background system service behind an Nginx proxy layer.