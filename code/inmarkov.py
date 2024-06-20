import random
from collections import defaultdict, deque

class InhomogeneousMarkovChain:
    def __init__(self, order):
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.state_counts = defaultdict(int)

    def train(self, notes):
        queue = deque(maxlen=self.order)
        
        for _ in range(self.order):
            queue.append(None)
        
        for note in notes:
            current_state = tuple(queue)
            self.transitions[current_state][note] += 1
            self.state_counts[current_state] += 1
            queue.append(note)
        
        for _ in range(self.order):
            current_state = tuple(queue)
            self.transitions[current_state][None] += 1
            self.state_counts[current_state] += 1
            queue.append(None)

    def generate_next_note_probabilistically(self, current_state):
        next_note_probs = self.transitions[current_state]
        total = self.state_counts[current_state]
        rand_val = random.uniform(0, total)
        cumulative = 0
        
        for note, count in next_note_probs.items():
            cumulative += count
            if rand_val < cumulative:
                return note
        return None

    def generate(self, num_notes):
        queue = deque([None] * self.order, maxlen=self.order)
        generated_notes = []
        
        for _ in range(num_notes):
            current_state = tuple(queue)
            next_note = self.generate_next_note_probabilistically(current_state)
            if next_note is None:
                break
            generated_notes.append(next_note)
            queue.append(next_note)
        
        return generated_notes

notes = []

with open('comb.txt', 'r') as file:
    notes = file.read().split(" ")

order = 3
markov_chain = InhomogeneousMarkovChain(order)
markov_chain.train(notes)
generated_notes = markov_chain.generate(10)
print(generated_notes)

