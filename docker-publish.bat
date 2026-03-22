@echo off
REM Docker Image Build & Push Script for MRCHRYS (Windows)
REM Usage: docker-publish.bat [version]
REM Example: docker-publish.bat v1.0.0

setlocal enabledelayedexpansion

set VERSION=%1
if "%VERSION%"=="" set VERSION=latest

set REGISTRY=enunekwu
set IMAGE_NAME=mrchrys

echo ================================
echo MRCHRYS Docker Publish Script
echo ================================
echo Registry: %REGISTRY%
echo Image Name: %IMAGE_NAME%
echo Version: %VERSION%
echo.

REM Check Docker is installed
where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Docker not found. Please install Docker Desktop first.
    echo Visit: https://www.docker.com/products/docker-desktop
    exit /b 1
)

REM Check Docker daemon is running
docker ps >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Docker daemon not running. Start Docker Desktop.
    exit /b 1
)

echo.
echo Step 1: Building Docker image...
docker build -t %IMAGE_NAME%:%VERSION% -t %IMAGE_NAME%:latest .
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Build failed
    exit /b 1
)
echo ✅ Build successful

echo.
echo Step 2: Tagging image for Docker Hub...
docker tag %IMAGE_NAME%:%VERSION% %REGISTRY%/%IMAGE_NAME%:%VERSION%
docker tag %IMAGE_NAME%:latest %REGISTRY%/%IMAGE_NAME%:latest
echo ✅ Tagged: %REGISTRY%/%IMAGE_NAME%:%VERSION% and %REGISTRY%/%IMAGE_NAME%:latest

echo.
echo Step 3: Checking Docker Hub login...
docker info | findstr /I "Username" >nul
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️  Not logged in. Running: docker login
    call docker login
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Docker login failed
        exit /b 1
    )
)

echo.
echo Step 4: Pushing to Docker Hub...
call docker push %REGISTRY%/%IMAGE_NAME%:%VERSION%
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Push version tag failed
    exit /b 1
)

call docker push %REGISTRY%/%IMAGE_NAME%:latest
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Push latest tag failed
    exit /b 1
)

echo ✅ Push successful

echo.
echo ================================
echo ✅ COMPLETE!
echo ================================
echo Image available at: https://hub.docker.com/r/%REGISTRY%/%IMAGE_NAME%
echo Pull with: docker pull %REGISTRY%/%IMAGE_NAME%:%VERSION%
echo.

pause
