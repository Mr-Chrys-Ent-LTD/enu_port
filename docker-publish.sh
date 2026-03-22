#!/bin/bash
# Docker Image Build & Push Script for MRCHRYS
# Usage: ./docker-publish.sh [version]
# Example: ./docker-publish.sh v1.0.0

VERSION=${1:-latest}
REGISTRY=enunekwu
IMAGE_NAME=mrchrys

echo "================================"
echo "MRCHRYS Docker Publish Script"
echo "================================"
echo "Registry: $REGISTRY"
echo "Image Name: $IMAGE_NAME"
echo "Version: $VERSION"
echo ""

# Check Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker Desktop first."
    exit 1
fi

# Check Docker daemon is running
if ! docker ps &> /dev/null; then
    echo "❌ Docker daemon not running. Start Docker Desktop."
    exit 1
fi

# Check User is logged in to Docker Hub
if ! docker info | grep -q "Username"; then
    echo "⚠️  Not logged in to Docker. Running: docker login"
    docker login
    if [ $? -ne 0 ]; then
        echo "❌ Docker login failed"
        exit 1
    fi
fi

echo ""
echo "Step 1: Building Docker image..."
docker build -t $IMAGE_NAME:$VERSION -t $IMAGE_NAME:latest .
if [ $? -ne 0 ]; then
    echo "❌ Build failed"
    exit 1
fi
echo "✅ Build successful"

echo ""
echo "Step 2: Tagging image for Docker Hub..."
docker tag $IMAGE_NAME:$VERSION $REGISTRY/$IMAGE_NAME:$VERSION
docker tag $IMAGE_NAME:latest $REGISTRY/$IMAGE_NAME:latest
echo "✅ Tagged: $REGISTRY/$IMAGE_NAME:$VERSION and $REGISTRY/$IMAGE_NAME:latest"

echo ""
echo "Step 3: Pushing to Docker Hub..."
docker push $REGISTRY/$IMAGE_NAME:$VERSION
if [ $? -ne 0 ]; then
    echo "❌ Push failed"
    exit 1
fi

docker push $REGISTRY/$IMAGE_NAME:latest
if [ $? -ne 0 ]; then
    echo "❌ Push latest tag failed"
    exit 1
fi

echo "✅ Push successful"

echo ""
echo "================================"
echo "✅ COMPLETE!"
echo "================================"
echo "Image available at: https://hub.docker.com/r/$REGISTRY/$IMAGE_NAME"
echo "Pull with: docker pull $REGISTRY/$IMAGE_NAME:$VERSION"
echo ""
