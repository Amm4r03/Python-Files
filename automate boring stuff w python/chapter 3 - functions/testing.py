import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.attack = random.randint(1, 10)
        self.agility = random.randint(1, 10)
        self.strength = random.randint(1, 10)
        self.magic = random.randint(1, 10)
        self.experience = 0
        self.health = 100
        self.defense_count = 0  # Track consecutive defense moves
        self.special_ability = random.choice(["Heal", "Fireball", "Shield"])
        self.critical_chance = 10  # Base critical hit chance

    def display_special_ability(self):
        print(f"{self.name}'s special ability: {self.special_ability}")

    def use_special_ability(self, opponent):
        if self.special_ability == "Heal":
            self.health += random.randint(10, 20)
            print(f"{self.name} uses Heal and restores some health.")
        elif self.special_ability == "Fireball":
            damage = random.randint(15, 25)
            opponent.health -= damage
            print(f"{self.name} casts Fireball for {damage} damage!")
        elif self.special_ability == "Shield":
            self.critical_chance += 10
            print(f"{self.name} raises a Shield and increases critical hit chance.")

def display_health_bars(player1, player2):
    os.system('clear')  # For Linux/Unix
    # os.system('cls')  # For Windows
    print(f"{player1.name}: {'#' * (player1.health // 2)} ({player1.health}HP)")
    print(f"{player2.name}: {'#' * (player2.health // 2)} ({player2.health}HP)")

def calculate_damage(attacker, defender):
    # Calculate damage based on the health difference
    health_difference = defender.health - attacker.health
    damage = attacker.attack + random.randint(0, 4) - defender.agility

    if health_difference > 0:
        damage += int(health_difference / 10)  # Easier to attack a weaker opponent

    # Implement critical hit
    if random.randint(1, 100) <= attacker.critical_chance:
        damage *= 2  # Critical hit deals double damage

    return max(1, damage)  # Ensure the minimum damage is at least 1

def player_turn(attacker, defender):
    attacker.defense_count += 1
    print(f"{attacker.name}'s turn:")
    print("1. Attack")
    print("2. Defend")
    print("3. Use Special Ability")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        damage = calculate_damage(attacker, defender)
        defender.health -= damage
        print(f"{attacker.name} attacks for {damage} damage!")
    elif choice == 2:
        # Add a small amount of damage to defenders when health difference is large
        health_difference = attacker.health - defender.health
        if health_difference > 20:
            damage = random.randint(1, 5)
            defender.health -= damage
            print(f"{defender.name} defends and takes {damage} damage.")
    elif choice == 3:
        attacker.use_special_ability(defender)
        attacker.defense_count = 0  # Reset defense count after using a special ability

    if defender.health <= 0:
        print(f"{defender.name} is knocked out! {attacker.name} wins!")
        return True

    return False

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    current_player = player1

    while True:
        display_health_bars(player1, player2)
        player1.display_special_ability()
        if current_player == player1:
            if player_turn(player1, player2):
                break
            current_player = player2
        else:
            if player_turn(player2, player1):
                break
            current_player = player1

if __name__ == "__main__":
    main()
