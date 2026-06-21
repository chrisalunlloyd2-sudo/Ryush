import subprocess
import json

def run_termux_api(command, *args):
    """Executes a termux-api command and returns the output."""
    full_command = [f"termux-{command}"] + list(args)
    try:
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing {full_command}: {e.stderr.strip()}"

# Example wrapper for telemetry
def get_device_telemetry():
    return {
        "battery": run_termux_api("battery-status"),
        "wifi": run_termux_api("wifi-connectioninfo"),
        "audio": run_termux_api("audio-info")
    }

if __name__ == "__main__":
    print("Termux API Manager initialized.")
    # Example: print(get_device_telemetry())
