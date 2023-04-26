class anime:
    def __init__(self,Na,MC):
        self.name = Na
        self.main_character = MC

    def anime_name(self):
        if self.name == "jujutsu kaisen":
            print(self.name,"is the best new gen anime")
        elif self.name == "attack on titan":
            print(self.name, "is the best anime of all")

    def anime_MC(self):
        if self.main_character == "itadori yuji":
            print(self.main_character,"is the main character of jjk")
        elif self.main_character =="eren jeager":
            print(self.main_character, "is the main character of AOT")

eren = anime("attack on titan","eren jeager")
eren.anime_name()
eren.anime_MC()
gojo = anime("jujutsu kaisen","itadori yuji")
gojo.anime_name()
gojo.anime_MC()