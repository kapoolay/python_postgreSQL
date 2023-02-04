# Class inheritance allows you to take methods and properties from another class

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)              # Device 'Printer' (USB)
printer.disconnect()        # Disconnected.


'''
Printer class inheriting Device class
Use the "super()." class within a class, to access the parent class's methods
'''

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


'''Inheritance calls'''
printInheritance = Printer("Printer", "USB", 500)
printInheritance.print(20)      # Printing 20 pages
print(printInheritance)         # Device 'Printer' (USB) (480 pages remaining)

printInheritance.print(320)     # Printing 320 pages
print(printInheritance)         # Device 'Printer' (USB) (160 pages remaining)

printInheritance.disconnect()   # Disconnected.
printInheritance.print(160)     # Your printer is not connected!
print(printInheritance)         # Device 'Printer' (USB) (160 pages remaining)


