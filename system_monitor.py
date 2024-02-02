import psutil

# Define thresholds
thresholds = {
    'cpu_usage': 80,       # CPU usage threshold (%)
    'memory_usage': 80,    # Memory usage threshold (%)
    'disk_usage': 80,      # Disk usage threshold (%)
}

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > thresholds['cpu_usage']:
        print(f"High CPU usage detected: {cpu_usage}%")

# Function to check memory usage
def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > thresholds['memory_usage']:
        print(f"High memory usage detected: {memory_usage}%")

# Function to check disk usage
def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > thresholds['disk_usage']:
        print(f"High disk usage detected: {disk_usage}%")

# Function to check running processes
def check_running_processes():
    # Get a list of running processes
    running_processes = len(psutil.pids())
    print(f"Number of running processes: {running_processes}")

# Main function
def main():
    print("System Health Monitoring Script")
    print("=" * 30)
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()

