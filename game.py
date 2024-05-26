class Dice:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
        self.pdist = [1/sides for _ in range(sides)]
        # Note: pdist = probability distribution

    def modify_distribution(self, new_dist: list) -> bool:
        if len(new_dist) != self.sides:
            print(f'Error: The new probability distribution list must have length {self.sides}.')
            return False
        for item in new_dist:
            try:
                # try to typecase as float, if it fails it means we did not receive a real number
                _ = float(item)
            except ValueError:
                print('Error: The elements of the probability distribution list must be floats')
                return False
        # Here the round function is used to prevent rounding error
        # e.g. 0.1 + 0.2 + 0.3 + 0.3 + 0.05 + 0.05 = 1.0000000000000002
        if round(sum([float(i) for i in new_dist]), 5) != 1:
            print('Error: The elements of the probability distibution must sum to 1.')
            return False
        # If it passes all the checks, the distribution is valid -- update the dist.
        self.pdist = [float(i) for i in new_dist]
        return True


class Square:
    def __init__(self, number: int = 0) -> None:
        self.number = number
        self.to = number

    def __str__(self) -> str:
        return f'{self.number} -> {self.to}'
    
    def modify_destination(self, new_dest: int) -> None:
        self.to = new_dest

class Game:
    def __init__(self, size) -> None:
        # Use [None] as part of self.arr to prevent indexing problems later on
        self.arr = [None] + [Square(i+1) for i in range(size)]
        self.size = size

    def __str__(self):
        temp = [str(i) for i in self.arr[1:]]
        return '\n'.join(temp)

