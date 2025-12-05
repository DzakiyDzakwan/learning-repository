# 1. Initialization
# The dictionary is created as a collection of key-value pairs
# Keys: Department Name (string) | Values: Employee Count (integer)
department_employees = {
    "Sales": 50,
    "Marketing": 35,
    "Engineering": 120
}

print("--- 1. Initialization ---")
print(f"Initial HashMap (Dictionary): {department_employees}")
print("-" * 30)

# --- 2. Insertion / Adding a New Key-Value Pair ---
# Operation: new_map[new_key] = new_value
department_employees["HR"] = 25
print("--- 2. Insertion ---")
print("Added 'HR' with 25 employees.")
print(f"Updated HashMap: {department_employees}")
print("-" * 30)

# --- 3. Lookup / Accessing a Value by Key (GET) ---
# Operation: value = map[key]
engineering_count = department_employees["Engineering"]
print("--- 3. Lookup (Get) ---")
print(f"The 'Engineering' department has {engineering_count} employees.")

# Safe Lookup using .get() - avoids a KeyError if the key doesn't exist
finance_count = department_employees.get("Finance", 0) # Returns 0 if 'Finance' is not found
print(f"The 'Finance' department has {finance_count} employees (using .get() with default).")
print("-" * 30)

# --- 4. Updating an Existing Value ---
# Operation: map[existing_key] = new_value (same syntax as insertion)
# The old value (50) for 'Sales' is overwritten by the new value (55)
department_employees["Sales"] = 55
print("--- 4. Update ---")
print("Updated 'Sales' employee count from 50 to 55.")
print(f"Updated HashMap: {department_employees}")
print("-" * 30)

# --- 5. Deletion / Removing a Key-Value Pair ---
# Operation: del map[key]
del department_employees["Marketing"]
print("--- 5. Deletion ---")
print("Removed the 'Marketing' department.")
print(f"Updated HashMap: {department_employees}")
print("-" * 30)

# --- 6. Checking for Key Existence ---
# Operation: key in map
is_hr_present = "HR" in department_employees
is_marketing_present = "Marketing" in department_employees
print("--- 6. Key Existence Check ---")
print(f"Is 'HR' present? {is_hr_present}")
print(f"Is 'Marketing' present? {is_marketing_present}")
print("-" * 30)

# --- 7. Iterating Over the HashMap ---

print("--- 7. Iteration ---")
print("A. Iterate over Keys:")
for department_name in department_employees.keys():
    print(f"  Key: {department_name}")

print("\nB. Iterate over Values:")
for count in department_employees.values():
    print(f"  Value: {count}")

print("\nC. Iterate over Key-Value Pairs (most common):")
for department_name, count in department_employees.items():
    print(f"  The {department_name} department has {count} employees.")

print("-" * 30)