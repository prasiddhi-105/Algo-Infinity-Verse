# Module 07 Exercises: Deployment

### Exercise 1: Multi-Platform Docker Configuration
* **Goal**: Understand containerized deployments.
* **Requirements**: 
    * Write out a basic multi-stage production `Dockerfile` that:
        1. Utilizes the `.NET SDK` base image to restore and compile dependencies.
        2. Copies the optimized `Release` binaries into a lightweight `.NET Runtime` base image.
        3. Exposes port `8080` to receive incoming production traffic logs.