import Pyro4

# Integrating math logic into the Remote Object
class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        return ("Hi welcome " + str(name))

    @Pyro4.expose
    def calculate_gcd(self, a, b):
        print(f"Server: Calculating GCD for {a}, {b}")
        while b != 0:
            a, b = b, a % b
        return a

    @Pyro4.expose
    def calculate_lcm(self, a, b):
        print(f"Server: Calculating LCM for {a}, {b}")
        # Logic: (a * b) // gcd(a, b)
        a_val, b_val = int(a), int(b)
        res_gcd = self.calculate_gcd(a_val, b_val)
        return (a_val * b_val) // res_gcd

def startServer():
    server = Server()
    # Create the Pyro daemon
    daemon = Pyro4.Daemon()             
    
    try:
        # Locate the Name Server
        ns = Pyro4.locateNS()
        # Register the server object
        uri = daemon.register(server)  
        # Register the object with the name "server"
        ns.register("server", uri)   
        
        print("--- Pyro4 Math Server Ready ---")
        print("Object URI =", uri)
        daemon.requestLoop()
    except Exception as e:
        print(f"Error: Could not locate Name Server. {e}")
        print("Tip: Run 'python -m Pyro4.naming' in a separate terminal.")

if __name__ == "__main__":
    startServer()