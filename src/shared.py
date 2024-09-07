import ctypes


def run_as_admin(cmd):
    # Define the ShellExecuteEx function
    shell32 = ctypes.windll.shell32
    ShellExecuteEx = shell32.ShellExecuteExW
    ShellExecuteEx.argtypes = (ctypes.c_void_p,)

    # Define the SHELLEXECUTEINFO structure
    class SHELLEXECUTEINFO(ctypes.Structure):
        _fields_ = [
            ('cbSize', ctypes.c_ulong),
            ('fMask', ctypes.c_ulong),
            ('hwnd', ctypes.c_void_p),
            ('lpVerb', ctypes.c_wchar_p),
            ('lpFile', ctypes.c_wchar_p),
            ('lpParameters', ctypes.c_wchar_p),
            ('lpDirectory', ctypes.c_wchar_p),
            ('nShow', ctypes.c_int),
            ('hInstApp', ctypes.c_void_p),
            ('lpIDList', ctypes.c_void_p),
            ('lpClass', ctypes.c_wchar_p),
            ('hKeyClass', ctypes.c_void_p),
            ('dwHotKey', ctypes.c_ulong),
            ('hIcon', ctypes.c_void_p),
            ('hProcess', ctypes.c_void_p)
        ]

    # Create the SHELLEXECUTEINFO structure
    sei = SHELLEXECUTEINFO()
    sei.cbSize = ctypes.sizeof(sei)
    sei.lpVerb = 'runas'
    sei.lpFile = 'python.exe'
    sei.lpParameters = cmd
    sei.nShow = 1

    # Run the command with admin privileges
    if not ShellExecuteEx(ctypes.byref(sei)):
        raise ctypes.WinError()

def set_priority():
    # Get the current process handle
    current_process = ctypes.windll.kernel32.GetCurrentProcess()
    
    # Set the priority class to realtime
    ctypes.windll.kernel32.SetPriorityClass(current_process, 0x00000100)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

