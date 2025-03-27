import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
PANEL_WIDTH = 250  # Width of the input panel
BOX_COLOR = (200, 200, 200)
FPS = 60
SPEED = 3
TIMEOUT = 120  # 2 minutes timeout

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Segoe UI Emoji", 24)
pygame.display.set_caption("Rock Paper Scissors Simulation")
pygame.event.pump()  # Force Pygame to process events

# Emoji representations
ROCK = "⚫"
PAPER = "📄"
SCISSORS = "✂️"

# Particle class
class Particle:
    def __init__(self, x, y, emoji):
        self.x = x
        self.y = y
        self.emoji = emoji
        self.vx = random.choice([-SPEED, SPEED])
        self.vy = random.choice([-SPEED, SPEED])
        self.font = pygame.font.SysFont("Segoe UI Emoji", 30)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= PANEL_WIDTH or self.x >= WIDTH - 30:
            self.vx *= -1
        if self.y <= 0 or self.y >= HEIGHT - 30:
            self.vy *= -1

    def draw(self):
        text_surface = self.font.render(self.emoji, True, BLACK)
        screen.blit(text_surface, (self.x, self.y))

    def check_collision(self, other):
        if abs(self.x - other.x) < 30 and abs(self.y - other.y) < 30:
            winner = get_winner(self.emoji, other.emoji)
            if winner:
                self.emoji = winner
                other.emoji = winner

# Determine winner based on Rock-Paper-Scissors rules
def get_winner(emoji1, emoji2):
    rules = {
        ROCK: SCISSORS,
        SCISSORS: PAPER,
        PAPER: ROCK
    }
    if rules.get(emoji1) == emoji2:
        return emoji1
    elif rules.get(emoji2) == emoji1:
        return emoji2
    return None

# Draw input panel and handle input
def draw_panel(input_text, winner_text=None, counts=None):
    pygame.draw.rect(screen, GRAY, (0, 0, PANEL_WIDTH, HEIGHT))
    font = pygame.font.SysFont("arial", 24)
    screen.blit(font.render("Enter count (2-50):", True, WHITE), (20, 50))
    screen.blit(font.render(input_text, True, WHITE), (20, 100))
    
    if counts:
        screen.blit(font.render(f"Rock: {counts[ROCK]}", True, WHITE), (20, 200))
        screen.blit(font.render(f"Paper: {counts[PAPER]}", True, WHITE), (20, 230))
        screen.blit(font.render(f"Scissors: {counts[SCISSORS]}", True, WHITE), (20, 260))
    
    if winner_text:
        screen.blit(font.render(winner_text, True, WHITE), (20, HEIGHT // 2))

def main(particle_count):
    particles = []
    for _ in range(particle_count):
        particles.append(Particle(random.randint(PANEL_WIDTH + 50, WIDTH - 50), random.randint(50, HEIGHT - 50), ROCK))
        particles.append(Particle(random.randint(PANEL_WIDTH + 50, WIDTH - 50), random.randint(50, HEIGHT - 50), PAPER))
        particles.append(Particle(random.randint(PANEL_WIDTH + 50, WIDTH - 50), random.randint(50, HEIGHT - 50), SCISSORS))
    
    running = True
    clock = pygame.time.Clock()
    winner_text = ""
    start_time = time.time()
    
    while running:
        screen.fill(WHITE)
        counts = {ROCK: 0, PAPER: 0, SCISSORS: 0}
        for particle in particles:
            counts[particle.emoji] += 1
        
        draw_panel("", winner_text, counts)
        pygame.draw.rect(screen, BOX_COLOR, (PANEL_WIDTH, 0, WIDTH - PANEL_WIDTH, HEIGHT), 5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for particle in particles:
            particle.move()
            particle.draw()
        
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                particles[i].check_collision(particles[j])
        
        # Check for winner
        types = set(p.emoji for p in particles)
        if len(types) == 1:
            winner_name = "Rock" if list(types)[0] == ROCK else "Paper" if list(types)[0] == PAPER else "Scissors"
            winner_text = f"{winner_name} is the winner"
            draw_panel("", winner_text, counts)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
        
        # Check for timeout
        if time.time() - start_time > TIMEOUT:
            winner_text = "Game ended in a draw"
            draw_panel("", winner_text, counts)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

def get_input():
    input_text = ""
    active = True
    while active:
        screen.fill(WHITE)
        draw_panel(input_text)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        count = int(input_text)
                        if 2 <= count <= 50:
                            return count
                    input_text = ""  # Reset if invalid
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

count = get_input()
if count:
    main(count)