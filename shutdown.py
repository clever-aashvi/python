import sys
import subprocess

def shut_down():
    """
    Triggers an immediate system shutdown based on the host operating system.
    """
    platform = sys.platform
    
    try:
        if platform == "win32":
            # Windows immediate shutdown
            subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
        elif platform in ["linux", "linux2", "darwin"]:
            # Linux and macOS immediate shutdown (may require root privileges)
            subprocess.run(["sudo", "shutdown", "now"], check=True)
        else:
            print(f"Unsupported operating system: {platform}")
            return False
        return True
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        print(f"Failed to execute shutdown: {e}")
        return False

