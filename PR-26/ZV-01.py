class Hero:
    def __init__(self, name, health, damage, armour):
        self.name = name
        self.health = health
        self.damage = damage
        self.armour = min(armour, 100)
        
    def show_name(self):
        print(f"Имя героя: {self.name}")

    def show_health(self):
        print(f"Его здоровье: {self.health}")

    def show_damage(self):
        print(f"Наносимый урон: {self.damage}")

    def show_armour(self):
        print(f"Активная защита: {self.armour}")

    def up_armour(self):
        self.armour = min(self.armour * 1.5, 100)
        print(f"\nЗащита увеличена до: {self.armour}")

    def take_damage(self, coming_damage):
        blocked_damage = coming_damage * self.armour / 100
        net_damage = coming_damage - blocked_damage
        self.health -= net_damage
        self.health = max(self.health, 0)
        print(f"\n{self.name} получил {net_damage:.2f} чистого урона.\nЗаблокированно урона: {blocked_damage}\nОставшееся здоровье: {self.health}")

hero = Hero("Владимир", 100, 52, 50)

hero.show_name()
hero.show_health()
hero.show_damage()
hero.show_armour()

hero.up_armour()
hero.take_damage(50)
