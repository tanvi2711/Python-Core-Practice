# # **Method vs Function (Easy Notes)**

# ## **What is a Function?**
# * A **function** is a block of code that performs a specific task.
# * It **does not belong to any object**.
# * We call it **directly by its name**.

# ### **Syntax**

# function_name(arguments)

### **Example**

L = [1, 2, 3]

print(len(L))

### **Explanation**
# * `len()` is a **function**.
# * It takes the list `L` as an argument.
# * It returns the total number of elements in the list.


# **What is a Method?**
# * A **method** is also a function, but it **belongs to an object**.
# * It is called using the **dot (.) operator**.

# ### **Syntax**

# object.method(arguments)

### **Example**

L = [1, 2, 3]

L.append(4)
print(L)

### **Explanation**
# * `append()` is a **list method**.
# * It adds the element `4` at the end of the list.


# **Code with Proper Comments**

# Create a list
L = [1, 2, 3]

# ---------------- FUNCTION ----------------

# len() is a built-in function.
# It counts the total number of elements in the list.
print(len(L))      # Output: 3


# ---------------- METHOD ----------------

# append() is a list method.
# It adds a new element at the end of the list.
L.append(4)

# Print the updated list
print(L)           # Output: [1, 2, 3, 4]



# **Difference Between Function and Method**

# | Function                         | Method                          |
# | -------------------------------- | ------------------------------- |
# | Works independently.             | Belongs to an object.           |
# | Called by its name.              | Called using `.` (dot).         |
# | Object is passed as an argument. | Object calls the method itself. |
# | Example: `len(L)`                | Example: `L.append(4)`          |


# **Examples**

### Functions

len(L)
print(L)
type(L)
sorted(L)

### Methods

L.append(10)
L.pop()
L.remove(2)

name = "python"
name.upper()
name.lower()

# **One-Line Interview Answer ⭐**

# > **Function:** A reusable block of code that is called directly by its name.
# > **Method:** A function that belongs to an object and is called using the dot (`.`) operator.

