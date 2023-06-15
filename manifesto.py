class BusinessLogic:
    def __init__(self):
        self.complexity_level = 0

    def increase_complexity(self):
        self.complexity_level += 1

    def decrease_complexity(self):
        if self.complexity_level > 0:
            self.complexity_level -= 1

    def handle_feature_request(self, feature):
        if self.complexity_level >= 2:
            print("Sorry, grug cannot build that feature. Complexity is too high.")
        else:
            print("Grug will build the requested feature.")

    def handle_abstraction_request(self, abstraction):
        if self.complexity_level >= 1:
            print("Sorry, grug cannot create that abstraction. Complexity is already high.")
        else:
            print("Grug will create the requested abstraction.")

    def handle_daily_routine(self, daily_routine):
        if self.complexity_level >= 1:
            print("No, grug will not perform the daily routine. Complexity is already high.")
        else:
            print("Grug will perform the daily routine.")

    def handle_water_drinking(self, water_amount):
        if self.complexity_level >= 2:
            print("No, grug will not drink less black think juice. Complexity is too high.")
        else:
            print("Grug will drink the specified amount of black think juice.")

    def print_complexity_level(self):
        print("Current complexity level:", self.complexity_level)


# Example usage
if __name__ == "__main__":
    logic = BusinessLogic()

    logic.handle_feature_request("User authentication")  # Grug will build the requested feature.
    logic.increase_complexity()

    logic.handle_feature_request("Social media integration")  # Grug will build the requested feature.
    logic.increase_complexity()

    logic.handle_feature_request("Machine learning algorithm")  # Sorry, grug cannot build that feature. Complexity is too high.

    logic.decrease_complexity()

    logic.handle_abstraction_request("Data access layer")  # Grug will create the requested abstraction.
    logic.increase_complexity()

    logic.handle_abstraction_request("User interface framework")  # Sorry, grug cannot create that abstraction. Complexity is already high.

    logic.handle_daily_routine("Take a shower")  # Grug will perform the daily routine.
    logic.increase_complexity()

    logic.handle_daily_routine("Exercise for 1 hour")  # No, grug will not perform the daily routine. Complexity is already high.

    logic.handle_water_drinking("2 liters")  # Grug will drink the specified amount of black think juice.
    logic.increase_complexity()

    logic.handle_water_drinking("1 liter")  # No, grug will not drink less black think juice. Complexity is too high.

    logic.print_complexity_level()  # Current complexity level: 2
