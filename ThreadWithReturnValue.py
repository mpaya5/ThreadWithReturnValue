from threading import Thread

class ThreadWithReturnValue(Thread):
    """
    ThreadMul class inherits from the Thread class in the threading library.
    It's used to create threads to execute tasks concurrently.
    """
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        """
        Constructor for the ThreadMul class.
        
        :param target: function that will be executed in the thread. Default is None.
        :param name: name of the thread. Default is None.
        :param args: tuple with arguments for the target function. Default is ().
        :param kwargs: dictionary with keyword arguments for the target function. Default is None.
        """
        super().__init__(target=target, name=name, args=args, kwargs=kwargs if kwargs else {})
        self._return = None  # Attribute to store the result of the thread execution
    
    def run(self):
        """
        The run method that gets executed when the thread starts. If a function is associated with the thread (self._target), it executes.
        """
        if self._target is not None: 
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args, **kwargs):
        """
        Method that blocks the calling thread until the thread whose join() method is called is terminated.
    
        :param *args: additional arguments that can be passed to the join method of the parent class (Thread).
        :param **kwargs: additional keyword arguments that can be passed to the join method of the parent class (Thread).
        """
        super().join(*args, **kwargs)  # Call the join method of the parent class (Thread)
        return self._return  # Return the result of the thread execution

