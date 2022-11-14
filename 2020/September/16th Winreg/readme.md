Modifying the windows registry can be complicated, generally the documentation available on the topic is less than ideal, hence this tutorial. In the video I am broudly discussing using python to update the windows registry using a simple pattern. 

[Link to Video](https://youtu.be/MdshNIw_ZRM)

## Terms

See my [Practical Windows Registry Explanation](https://www.youtube.com/watch?v=tBwAHqqPoQY&feature=youtu.be) video for a more in depth look, but here is the terminology you should be aware of:

- Key: A key in the context of the registry is essentially a folder that contains values
- Values: Can be thought of as variables that store a representation of some state within windows
- Hkey: The top level keys of the registry, through which all other sub-keys are accessed
- sub-key: Any key that is stored within a Hkey
- winreg: A python module for accessing the registry documentation is available [here](https://docs.python.org/3/library/winreg.html)
- ctypes: A module for interfacing with low-level C code in python

## Problem

In particular we are looking at updating the [PATH variable](https://en.wikipedia.org/wiki/PATH_(variable)#:~:text=PATH%20is%20an%20environment%20variable,has%20its%20own%20PATH%20setting.) on windows, which is stored in the registry. As (essentially) a string of folder paths.

## Solution
Below is a step-by-step breakdown of the solution to the problem. See the corresponding files in this repo for the full code version.

Before the soltion we need to do some setup for the file by importing our modules, and setting up the folder path we want to add to our PATH variable:

```python
import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents" # File path to the folder containing our desired executable
```

### Step 1. Connect to the registry with winreg.ConnectRegistry()

Much like you would open a file, you need to initialize your connection to the registry by accessing a Hkey. In our case we want ```HKEY_CURRENT_USER```. Luckily this hkey is a built in variable in winreg (```winreg.HKEY_CURRENT_USER```), so lets connect using ```ConnectRegistry()``` and our hkey:

```python
import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents" # File path to the folder containing our desired executable

with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
```

### Step 2. Connect to the sub-key with winreg.OpenKey()
Now that we're in the Hkey we need, lets get into the sub-key we want. In this case it's the ```Environment``` key. Much like our hkey, we need to "open" it:

```python
import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents"


with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
    with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key: # Go to the environment key
```

There are a few new parameters we need to contend with on this step, namely ```key```, ```reserved```, and ```access```. In this like ```key``` refers to our open hkey, ```reserved``` should always be 0, and ```access``` refers to winreg's access constants (link to docs in [references](#references))

### Step 3. Get a value in the sub-key with winreg.EnumValue()

Next we can access the current path value. To do this we can use ```winreg.EnumValue()```:

```python

import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents"


with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
    with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key: # Go to the environment key
        existing_path_value = winreg.EnumValue(sub_key, 3)[1] # Grab the current path value
```

```winreg.EnumValue()``` returns a tuple for a given value of ```(name, data, type)``` where the type is represented by an int. So notice I selected the 3rdth index and took the 1sth index of the resulting tuple (which is the data). **Keep in mind** This is a cheap solution, for some people the PATH variable will be at a different index, I would recommend iterating through the subkeys and searching for the right name to get the index as a general solution.

### Step 4. Modify our data however we want

Now that we have the current path value in ```existing_path_value``` we need to update it with our new program path, and a semicolon to indicate termination:

```python

import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents"


with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
    with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key: # Go to the environment key
        existing_path_value = winreg.EnumValue(sub_key, 3)[1] # Grab the current path value
        new_path_value = existing_path_value + program_path + ";" # Takes the current path value and appends the new program path
```

### Step 5. Update registry with new data using SetValueEx()

Now that we have our new value stored in ```new_path_value``` we need to actually update the registry. This can be done through ```winreg.SetValueEx()```:

```python
import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents"


with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
    with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key: # Go to the environment key
        existing_path_value = winreg.EnumValue(sub_key, 3)[1] # Grab the current path value
        new_path_value = existing_path_value + program_path + ";" # Takes the current path value and appends the new program path
        winreg.SetValueEx(sub_key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value) # Updated the path with the updated path
```

For parameters we need to pass the open subkey, the name of the value to update, reverved (always 0), the value type (see [references](#references) for details), and the new data for the value (```new_path_value``` in our case).

**BUT WAIT**, if you run the code nothing changes. There is one more step to get it to work.

### Step 6. Tell the registry to save the changes with ctypes

I am not going to explain this code, the only thing that matters is the 4th parameter on the last line. Update that param to your sub-key you modified, otherwise just copy pase the new code:

```python
import winreg # Allows access to the windows registry
import ctypes # Allows interface with low-level C API's


program_path = f"%USERPROFILE%\\Documents"


with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey: # Get the necessary HKEY
    with winreg.OpenKey(hkey, "Environment", 0, winreg.KEY_ALL_ACCESS) as sub_key: # Go to the environment key
        existing_path_value = winreg.EnumValue(sub_key, 3)[1] # Grab the current path value
        print(f"{existing_path_value=}")
        new_path_value = existing_path_value + program_path + ";" # Takes the current path value and appends the new program path
        print(f"{new_path_value=}")
        winreg.SetValueEx(sub_key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value) # Updated the path with the updated path

        # Tell other processes to update their environment
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x1A
        SMTO_ABORTIFHUNG = 0x0002
        result = ctypes.c_long()
        SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
        SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, u"Environment", SMTO_ABORTIFHUNG, 5000, ctypes.byref(result),) 
```

This code essentially says "Hey, the registry has been updated. You mind saving the changes please".

## References

- [ConnectRegistry()](https://docs.python.org/3/library/winreg.html#winreg.ConnectRegistry)
- [HKEY_* Constants](https://docs.python.org/3/library/winreg.html#hkey-constants)
- [OpenKey()](https://docs.python.org/3/library/winreg.html#winreg.OpenKey)
- [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights)
- [EnumValue()](https://docs.python.org/3/library/winreg.html#winreg.EnumValue)
- [SetValueEx()](https://docs.python.org/3/library/winreg.html#winreg.SetValueEx)
- [Value Types](https://docs.python.org/3/library/winreg.html#value-types)
- [Practical Windows Registry Explanation](https://www.youtube.com/watch?v=tBwAHqqPoQY&feature=youtu.be)