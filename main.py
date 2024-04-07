import os

# Get the operating system name
os_name = os.name
print("Operating System:", os_name)

# Get more detailed information about the operating system
os_info = os.uname() if os_name == 'posix' else None

if os_info:
    print("\nOS Information:")
    print("System:", os_info.sysname)
    print("Node Name:", os_info.nodename)
    print("Release:", os_info.release)
    print("Version:", os_info.version)
    print("Machine:", os_info.machine)

    # Check if the processor information is available before accessing it
    if hasattr(os_info, 'processor'):
        print("Processor:", os_info.processor)
    else:
        print("Processor information is not available.")
else:
    print("\nDetailed OS information is not available on this platform.")