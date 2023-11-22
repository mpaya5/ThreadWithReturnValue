# ThreadWithReturnValue
The ThreadWithReturnValue class extends Python's Thread class from the threading module, allowing threads to return a value after they have been executed. This enhancement facilitates the retrieval of results from threads, which is not directly possible with the standard Thread class.

## Usage
Here's how you can use the ThreadWithReturnValue class:
```
from ThreadWithReturnValue import ThreadWithReturnValue

def example_function(param1, param2):
    # Replace the following line with the function's implementation
    return param1 + param2

# Create a new thread instance passing the target function and its arguments
thread = ThreadWithReturnValue(target=example_function, args=(10, 20))

# Start the thread
thread.start()

# Join the thread and retrieve the return value
result = thread.join()

# Output the result
print(f"Result from thread: {result}")
```

## Installation
To use this class, simply include ThreadWithReturnValue.py in your project directory and import it as shown in the usage example.

## Features
Easy to use and integrate with existing code that uses standard Python threads.
Allows retrieval of results from thread execution, similar to Future or Promise in other languages.
Improves the efficiency of handling concurrent tasks where the main thread requires the result of the computations.

## Contributing
Contributions to ThreadWithReturnValue are welcome! Please feel free to submit pull requests, suggest features, or report bugs.