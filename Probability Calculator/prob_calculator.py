import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)  # Create a deep copy of the hat for each experiment
        drawn_balls = copy_hat.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
        match = all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items())

        if match:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
print(f"Estimated Probability: {probability:.4f}")