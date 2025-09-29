class Player:
    def __init__(self, name, player_class="Warrior", level=1, hp=100, xp=0, gold=0, inventory=None):
        self.name = name
        self.player_class = player_class
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.xp = xp
        self.gold = gold
        self.inventory = inventory or []

        if player_class == "Warrior":
            self.attack = 10
            self.defense = 8
        elif player_class == "Mage":
            self.attack = 6
            self.defense = 4
        elif player_class == "Rogue":
            self.attack = 8
            self.defense = 5
        else:
            self.attack = 5
            self.defense = 5

    def show_stats(self):
        print(f"\n{self.name} the {self.player_class}")
        print(f"Level: {self.level} | XP: {self.xp}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack} | Defense: {self.defense}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

    def to_dict(self):
        return {
            "name": self.name,
            "player_class": self.player_class,
            "level": self.level,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "xp": self.xp,
            "gold": self.gold,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory,
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(
            name=data["name"],
            player_class=data["player_class"],
            level=data["level"],
            hp=data["max_hp"],
            xp=data["xp"],
            gold=data["gold"],
            inventory=data["inventory"],
        )
        player.hp = data["hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.max_hp = data["max_hp"]
        return player