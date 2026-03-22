# Docker Image Publishing Guide - MRCHRYS

## Step 1: Install Docker

### Windows (Recommended: Docker Desktop)

1. **Download Docker Desktop for Windows**
   - Visit: https://www.docker.com/products/docker-desktop
   - Click "Download for Windows"
   - Choose your Windows version (Windows 11 Pro/Enterprise recommended)

2. **Install Docker Desktop**
   - Run the installer
   - Follow the installation wizard
   - Restart your computer when prompted
   - WSL 2 (Windows Subsystem for Linux) will be enabled automatically

3. **Verify Installation**
   ```bash
   docker --version
   docker run hello-world
   ```

4. **Enable Resource Sharing** (in Docker Desktop Settings)
   - Resources > File Sharing: Add `c:\Users\smart\Documents\projects\enu`
   - Resources > CPU/Memory: Allocate sufficient resources (4+ CPU cores, 4GB+ RAM recommended)

## Step 2: Prepare for Docker Hub

1. **Create/Login to Docker Hub Account**
   - Visit: https://hub.docker.com
   - Create an account if you don't have one
   - Use username: `enunekwu`

2. **Create a Personal Access Token** (recommended for security)
   - Docker Hub Dashboard > Account Settings > Security > New Access Token
   - Name it: `mrchrys-docker-token`
   - Copy the token (you'll need this for login)

3. **Login from Command Line**
   ```bash
   docker login
   # Username: enunekwu
   # Password: <paste your access token>
   ```

## Step 3: Build the Docker Image

1. **Navigate to Project Directory**
   ```bash
   cd c:\Users\smart\Documents\projects\enu
   ```

2. **Build the Image**
   ```bash
   docker build -t mrchrys:latest .
   ```
   
   This will:
   - Read the Dockerfile
   - Build the image with all dependencies
   - Tag it as `mrchrys:latest`
   - Takes ~5-10 minutes on first build

3. **Verify Build Success**
   ```bash
   docker images | grep mrchrys
   ```

## Step 4: Tag Image for Docker Hub

```bash
# Tag with Docker Hub registry prefix
docker tag mrchrys:latest enunekwu/mrchrys:latest
docker tag mrchrys:latest enunekwu/mrchrys:v1.0.0
```

Verify tags:
```bash
docker images | grep enunekwu/mrchrys
```

Should show:
```
enunekwu/mrchrys    latest    <image-id>    <created>
enunekwu/mrchrys    v1.0.0    <image-id>    <created>
```

## Step 5: Push to Docker Hub

1. **Push Latest Version**
   ```bash
   docker push enunekwu/mrchrys:latest
   ```

2. **Push Version Tag**
   ```bash
   docker push enunekwu/mrchrys:v1.0.0
   ```

   Monitor the push:
   - Each layer will upload
   - Takes 2-10 minutes depending on image size and internet speed
   - Success message: `Digest: sha256:...`

3. **Verify on Docker Hub**
   - Visit: https://hub.docker.com/r/enunekwu/mrchrys
   - Should see both `latest` and `v1.0.0` tags

## Step 6: Test Pulled Image (Optional)

```bash
# Pull your image from Docker Hub
docker pull enunekwu/mrchrys:latest

# Run it locally
docker run -p 8000:8000 enunekwu/mrchrys:latest
```

## Step 7: Update docker-compose.yml to Use Published Image (Optional)

Edit `docker-compose.yml`, change the `web` service:

```yaml
web:
  image: enunekwu/mrchrys:latest  # Instead of: build: .
  environment:
    # ... rest of config
```

Then run:
```bash
docker-compose pull
docker-compose up
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `docker: command not found` | Docker not installed or not in PATH. Restart after Docker Desktop installation |
| `permission denied` | Run `docker-compose up` with `winpty` on Git Bash: `winpty docker-compose up` |
| `Cannot connect to Docker daemon` | Start Docker Desktop application |
| `push: denied: requested access to the resource is denied` | Login with correct credentials: `docker login` |
| `layer already exists` | Normal message - skips unchanged layers |
| `image build failure` | Check Dockerfile, ensure all dependencies in `requirements.txt` are valid |

## One-Command Quick Start

After Docker is installed and you're logged in:

```bash
cd c:\Users\smart\Documents\projects\enu
docker build -t enunekwu/mrchrys:latest . && \
docker push enunekwu/mrchrys:latest
```

## Production Deployment

Once published, deploy anywhere:

```bash
# AWS ECS, Heroku, DigitalOcean, etc.
docker pull enunekwu/mrchrys:latest
docker run -e SECRET_KEY=your-secret \
           -e ALLOWED_HOSTS=yourdomain.com \
           -p 8000:8000 \
           enunekwu/mrchrys:latest
```

## Next Steps

1. Install Docker Desktop
2. Restart your system
3. Follow Steps 2-5 above
4. Confirm image appears on: https://hub.docker.com/r/enunekwu/mrchrys

---

**Questions?** Check Docker's official guide: https://docs.docker.com/docker-hub/
