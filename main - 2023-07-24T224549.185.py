class Friend:
    def __init__(self, name, contact_info, properties_owned=None):
        self.name = name
        self.contact_info = contact_info
        self.properties_owned = properties_owned if properties_owned is not None else []

    def add_property(self, property_name):
        self.properties_owned.append(property_name)

    def __repr__(self):
        return f"Friend(name='{self.name}', contact_info='{self.contact_info}', properties_owned={self.properties_owned})"


class RealEstateNetwork:
    def __init__(self):
        self.friends = {}

    def add_friend(self, name, contact_info):
        if name in self.friends:
            print(f"{name} is already in the network.")
        else:
            self.friends[name] = Friend(name, contact_info)
            print(f"{name} has been added to the network.")

    def add_property_to_friend(self, friend_name, property_name):
        friend = self.friends.get(friend_name)
        if friend:
            friend.add_property(property_name)
            print(f"{property_name} has been added to {friend_name}'s properties.")
        else:
            print(f"{friend_name} is not in the network.")

    def get_friend_info(self, friend_name):
        friend = self.friends.get(friend_name)
        if friend:
            print(friend)
        else:
            print(f"{friend_name} is not in the network.")

    def get_friends_by_property(self, property_name):
        friends_with_property = [
            friend.name for friend in self.friends.values() if property_name in friend.properties_owned
        ]
        if friends_with_property:
            print(f"The following friends own {property_name}: {', '.join(friends_with_property)}")
        else:
            print(f"No friends own {property_name}.")

    def __repr__(self):
        return f"RealEstateNetwork({self.friends})"


if __name__ == "__main__":
    network = RealEstateNetwork()

    # Add friends to the network
    network.add_friend("John", "john@email.com")
    network.add_friend("Alice", "alice@email.com")

    # Add properties to friends
    network.add_property_to_friend("John", "Property A")
    network.add_property_to_friend("Alice", "Property B")

    # Get friend information
    network.get_friend_info("John")
    network.get_friend_info("Bob")  # Bob is not in the network

    # Get friends who own a specific property
    network.get_friends_by_property("Property A")
    network.get_friends_by_property("Property C")  # No friend owns Property C
