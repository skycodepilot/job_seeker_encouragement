IMAGE_NAME=jobjoblift
CONTAINER_NAME=jobjoblift_container

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the container
run:
	docker run --rm -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Rebuild and run in one go
dev: build run

# Stop container (if running in detached mode later)
stop:
	docker stop $(CONTAINER_NAME) || true
