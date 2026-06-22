# # Lambda Function

# • A lambda function is a small anonymous function.
#   (Anonymous = function without a name)

# • Lambda functions are created using the 'lambda' keyword.

# • A lambda function can take any number of arguments.

# • A lambda function can contain only one expression.

# • The value of the expression is automatically returned.

# # Syntax

# lambda parameters : expression

# # Components

# 1. lambda
#    → Keyword used to create a lambda function.

# 2. Parameters
#    → Input values passed to the function.
#    → One or more parameters can be used.
#    → Parameters are separated by commas.

# 3. Colon (:)
#    → Separates parameters from the expression.

# 4. Expression
#    → A single valid Python expression.
#    → Evaluated and returned automatically.

# # Characteristics

# ✓ Small and concise
# ✓ Anonymous (no function name required)
# ✓ Can accept multiple arguments
# ✓ Contains only one expression
# ✓ Returns result automatically

# # Limitation

# ✗ Cannot contain multiple statements
# ✗ Cannot contain complex logic
# ✗ Limited to a single expression

# # Difference Between Normal Function and Lambda Function

# Normal Function:
# • Defined using 'def' keyword.
# • Function name is required.
# • Can contain multiple statements.
# • Requires explicit return statement (usually).
# • Suitable for complex logic and large programs.

# Lambda Function:
# • Defined using 'lambda' keyword.
# • No function name required (anonymous).
# • Can contain only one expression.
# • Returns value automatically.
# • Suitable for short and simple operations.

# # Interview Definition

# A lambda function is an anonymous, one-line function
# created using the 'lambda' keyword that can accept
# multiple arguments but contains only a single expression,
# whose result is returned automatically.

# Then why use lambda functions?
# They are used with HOF(higher order fun)


a=lambda x: x+2
print(a(2))


b=lambda x,y: x+y
print(b(3,5))

# check if a string has 'a'
c= lambda x : 'a' in x 
print(c('tanvi'))

# odd or even
d= lambda x : 'even' if x%2==0 else 'odd'
print(d(9))


