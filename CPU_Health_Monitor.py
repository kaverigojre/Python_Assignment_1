
import psutil
def monitor_cpu_health():
    print("Monitoring CPU usage...")
    try:
        threshold_cpu = 80
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)  #current CPU usgae info FROM the psutil method
            print("Current CPU Usage:",cpu_usage,"%") 
            if cpu_usage > threshold_cpu: # Checking CPU trashhold
                print("Alert! CPU usage exceeds threshold:",cpu_usage,"%")
            
    except KeyboardInterrupt:  #exceptin incase user stopps the excecution
        print("User stopped the execution by pressing a keyboard Key")
    except Exception as e:
        print("An error occurred:",str(e))

if __name__ == "__main__":
    monitor_cpu_health()
