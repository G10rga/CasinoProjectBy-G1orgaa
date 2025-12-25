import pygame
import sys
import time
import random


# სირთულეები
# ადვილი        ->  10
# საშუალო       ->  25
# ცოტათი ძნელი ->  40
# ძნელი         ->  60
# შეუძლებელი   ->  120

difficulty = 15
#შეცვალეთ  difficulty = თქვენთვის სასურველი სირთულით 



#ბოტის სირთულე  
# სირთულეები
# ადვილი        ->  1-4
# საშუალო       ->  5-8
# ცოტათი ძნელი ->  10
# ძნელი         ->  10-20
# შეუძლებელი   ->  >20

bot_difficulty = 5
#შეცვალეთ  bot_difficulty = თქვენთვის სასურველი სირთულით 


# ფანჯრის სიდიდე
frame_size_x = 600
frame_size_y = 600


# შეცდომების შემოწმება
pygame.init()

# თამაშის ფანჯრის ინიციალიზაცია
pygame.display.set_caption('SnakeGame By G1orgaa')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# ფერები (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS კონტროლერი
fps_controller = pygame.time.Clock()


# თამაშის ცვლადები
snake_pos = [100, 50]
snake_body = [[150, 50], [100-10, 50], [100-(2*10), 50]]
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
goal= 3
snakegoal = 3



# მოთამაშის ქულების ასახვა

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


#ბოტის ქულების ასახვა
def show_botscore(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Bot Score : ' + str(bot_snake.botscore), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/8, 40)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)




# დაჯახებით წაგების ინიციალიზაცია
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#მოგების ინიციალიზაცია
def game_win():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU WIN', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#ბოტის მიერ წაგების ინიცალიზაცია
def game_lose():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU LOSE', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()    



#ავტომატური ბოტი 
class BotSnake():
    def __init__(self):
        self.pos = [100, 50]
        self.body = [[150, 50], [100 - 10, 50], [100 - (2 * 10), 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.botscore = 0

    def update_direction(self, food_pos):
        if self.pos[0] < food_pos[0] and self.direction != 'LEFT':
            self.change_to = 'RIGHT'
        if self.pos[0] > food_pos[0] and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if self.pos[1] < food_pos[1] and self.direction != 'UP':
            self.change_to = 'DOWN'
        if self.pos[1] > food_pos[1] and self.direction != 'DOWN':
            self.change_to = 'UP'
    
    
    def move(self):
        global food_spawn
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        
        
        if self.direction == 'UP':
            self.pos[1] -= (bot_difficulty)
        if self.direction == 'DOWN':
            self.pos[1] += (bot_difficulty)
        if self.direction == 'LEFT':
            self.pos[0] -= (bot_difficulty)
        if self.direction == 'RIGHT':
            self.pos[0] += (bot_difficulty)
        
        
        self.body.insert(0, list(self.pos))
        botscore = 0
        
        if self.pos[0] == food_pos[0] and self.pos[1] == food_pos[1]:
            self.botscore += 1
            food_spawn = False
        else:
            self.body.pop()
    
    def draw(self, game_window):
        for pos in self.body:
            pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))
    
    
    def check_collision(self, frame_size_x, frame_size_y):
        if self.pos[0] < 0 or self.pos[0] > frame_size_x - 10:
            game_over()
        if self.pos[1] < 0 or self.pos[1] > frame_size_y - 10:
            game_over()
        for block in self.body[1:]:
            if self.pos[0] == block[0] and self.pos[1] == block[1]:
                game_over()
        if snake_pos in bot_snake.body:
            game_over()

bot_snake = BotSnake()



# მთავარი ციკლი
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # კლავიშების ინიციალიზაცია
        elif event.type == pygame.KEYDOWN:
            # W -> მაღლა; S -> დაბლა; A -> მარცხნივ; D -> მარჯვნივ
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> თამშის გამორთვა
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


    # სნეიკის მოძრაობა
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # ტანის გაზრდის მექანიზმი ჭამის მერე
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()


    # საჭმლის გაჩენა 
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True



    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    bot_snake.draw(game_window)



    #ავტომატური ბოტი
    bot_snake.update_direction(food_pos)
    bot_snake.move()
    bot_snake.check_collision(frame_size_x, frame_size_y)
    bot_snake.draw(game_window)




    # საჭმელი
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # თამაშის დასრულების პირობები
    # საზღვრებს გარეთ გასვლა
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # თავის და ტანის თანაკვეთა
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()



        #წაგება და მოგება ქულებით
    if score >= goal :
       game_win()

    if bot_snake.botscore >= snakegoal :
        game_lose()

    show_score(1, white, 'consolas', 20)
    show_botscore(1, white, 'consolas', 20)
    pygame.display.update()

    
        
    fps_controller.tick(difficulty)