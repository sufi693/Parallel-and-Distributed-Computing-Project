import Pyro4

name = input("What is your name? ").strip()

# Connect using the Name Server lookup shortcut
try:
    server = Pyro4.Proxy("PYRONAME:server")    
    
    # 1. Original welcome message
    print(server.welcomeMessage(name))

    # 2. Project Math Logic
    val1, val2 = 48, 18
    print(f"\nRequesting GCD of {val1} and {val2}...")
    gcd_res = server.calculate_gcd(val1, val2)
    print(f"GCD Result: {gcd_res}")

    print(f"Requesting LCM of 12 and 15...")
    lcm_res = server.calculate_lcm(12, 15)
    print(f"LCM Result: {lcm_res}")

except Exception as e:
    print(f"Communication error: {e}")