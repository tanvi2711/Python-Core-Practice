# ==========================================
# FROZENSET IN PYTHON
# ==========================================

# A frozenset is an immutable version of a set.
# Once created, elements cannot be modified,
# added, or removed.

# Syntax:
# frozenset(iterable)

# ------------------------------------------
# CREATING A FROZENSET
# ------------------------------------------

fs = frozenset([1, 2, 3])

print(fs)

# Output:
# frozenset({1, 2, 3})

# ------------------------------------------
# READ OPERATIONS (WORKS)
# ------------------------------------------

print(len(fs))      # Number of elements
print(min(fs))      # Smallest element
print(max(fs))      # Largest element
print(sum(fs))      # Sum of elements

print(2 in fs)      # Membership Test

# Output:
# 3
# 1
# 3
# 6
# True

# ------------------------------------------
# WRITE OPERATIONS (DOES NOT WORK)
# ------------------------------------------

# fs.add(4)
# fs.remove(2)
# fs.update([4, 5])

# Output:
# AttributeError

# ------------------------------------------
# SET OPERATIONS
# ------------------------------------------

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print("Union:", fs1 | fs2)
print("Intersection:", fs1 & fs2)
print("Difference:", fs1 - fs2)
print("Symmetric Difference:", fs1 ^ fs2)

# Output:
# Union: frozenset({1, 2, 3, 4, 5, 6})
# Intersection: frozenset({3, 4})
# Difference: frozenset({1, 2})
# Symmetric Difference: frozenset({1, 2, 5, 6})

# ------------------------------------------
# USING FROZENSET INSIDE A SET
# ------------------------------------------

fs = frozenset([1, 2, 3])

s = {fs}

print(s)

# Output:
# {frozenset({1, 2, 3})}

# ------------------------------------------
# 2D SETS USING FROZENSET
# ------------------------------------------

s = {
    frozenset({1, 2}),
    frozenset({3, 4})
}

print(s)

# Output:
# {frozenset({1, 2}), frozenset({3, 4})}