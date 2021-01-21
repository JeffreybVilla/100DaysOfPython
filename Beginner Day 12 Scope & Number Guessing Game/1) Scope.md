![](https://github.com/JeffreybVilla/100DaysOfPython/blob/main/images/python-variable-scope-resolution-legb.png)

# What is Python Namespace?
    Python namespaces are containers to map names to objects.
    In Python, Everything is an object and we specify a name to the object so that we can access it later.

    Namespaces are like a dictionary of key-value pairs. The key is the variable and the value is the object associated with it. 
    namespace = {"name1":object1, "name2":object2}

    In python, multiple namespaces can exist at same time. 
    Variable names can be reused in these namespaces.
    function_namespace = {"name1":object1, "name2":object2}
    for_loop_namespace = {"name1":object3, "name2":object4}

    Example with multiple namespaces.
![](https://github.com/JeffreybVilla/100DaysOfPython/blob/main/images/python-namespace-example.png)



## Python Namespace Types & Lifecycle
    1. Local Namespace:
    A function, for-loop, try-except block.
    The local namespace is deleted when the function or the code block finishes its execution. 

    2. Enclosed Namespace:
    When a function is defined inside a function, it creates an enclosed namespace.
    Its lifecycle is the same as the local namespace.

    3. Global Namespace:
    Belongs to the Python script or the current module.
    Global namespace for a module is created when the module definition is read.
    Generally, module namespaces also last until the interpreter quits.

    4. Built-in Namespace:
    Created when the Python interpreter starts up and it's never deleted. 



# Python Variable Scope
