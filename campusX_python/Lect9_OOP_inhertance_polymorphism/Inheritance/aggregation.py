class Address:

    # Constructor
    def __init__(self, city, pin, state):
        self.__city = city      # Private Attribute
        self.pin = pin
        self.state = state

    # Display Address
    def print_address(self):
        print("City :", self.__city)
        print("Pin  :", self.pin)
        print("State:", self.state)

    # Getter Method
    def get_city(self):
        return self.__city

    # Setter Method
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


# ==========================================
# Customer Class
# ==========================================

class Customer:

    # Constructor
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address      # Aggregation (HAS-A Relationship)

    # Display Customer Details
    def print_customer(self):
        print("Name   :", self.name)
        print("Gender :", self.gender)

    # Edit Customer Profile
    def edit_profile(self, new_name, new_gender,new_city, new_pin, new_state):
        self.name = new_name
        self.gender=new_gender

        # Calling Address class method
        self.address.edit_address(new_city, new_pin, new_state)


# ==========================================
# Creating Address Object
# ==========================================

addr = Address("Amravati", 444604, "Maharashtra")

# ==========================================
# Creating Customer Object
# ==========================================

c1 = Customer("Nishant", "Male", addr)

# ==========================================
# Before Editing
# ==========================================

print("===== Customer Details =====")
c1.print_customer()

print("\n===== Address Details =====")
c1.address.print_address()

# Accessing Private Attribute using Getter
print("\nCity using Getter :", c1.address.get_city())

# ==========================================
# Editing Customer Profile
# ==========================================

c1.edit_profile("Tanvi",'Female', "Pune", 411001, "Maharashtra")

# ==========================================
# After Editing
# ==========================================

print("\n===== Updated Customer Details =====")
c1.print_customer()

print("\n===== Updated Address Details =====")
c1.address.print_address()

print("\nUpdated City :", c1.address.get_city())
