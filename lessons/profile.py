"""Practice Writing a Class"""

class Profile:

    username: str
    private: bool

    def __int__ (self, username_input: str):
        """Create a new Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If profile is public, print msg."""
        if self.private is False:
            print(msg)
#Instantiation: 
user1: Profile = Profile("110_rulez)")#calls __init__
user1.private = False
user1.tweet("OOP is cool!")
