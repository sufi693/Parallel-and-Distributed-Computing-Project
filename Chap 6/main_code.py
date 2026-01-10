def find_gcd(n1, n2):
    """Calculates the Greatest Common Divisor using recursion."""
    if n2 == 0:
        return n1
    return find_gcd(n2, n1 % n2)

def find_lcm(n1, n2):
    """Calculates the Least Common Multiple using the GCD relationship."""
    # Logic: (n1 * n2) / GCD = LCM
    absolute_product = abs(n1 * n2)
    return absolute_product // find_gcd(n1, n2)

# --- Execution Block ---
if __name__ == "__main__":
    print("--- LCM Calculator ---")
    
    val1 = int(input("Enter first integer: "))
    val2 = int(input("Enter second integer: "))

    result = find_lcm(val1, val2)
    
    print(f"The LCM of {val1} and {val2} is: {result}")