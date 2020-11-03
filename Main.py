import pygame
from pyautogui import size
from time import time
from Button import *
from Label import *
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
fonts = {
	"PixelArt": pygame.font.Font("SFPixelate.ttf", 20)
}
quit_button_image = pygame.image.load("quit_button_image.png")
quit_button_image_hover = pygame.image.load("quit_button_image_hover.png")
quit_button = Button(window_width - 20 - quit_button_image.get_width(), 20, quit_button_image, quit_button_image_hover, 0, 0)
def Quiz(timer, number, question, buttons_num, buttons_texts, true_answer):
	number_label = Label(20, 20, window_width // 2, number, fonts["PixelArt"], (255, 255, 255))
	question_label = Label(window_width // 2, window_height // 2, window_width // 2, question, fonts["PixelArt"], (255, 255, 255), "yes")
	space = 20
	buttons = []
	x = 0
	button_width = 100
	button_height = 100
	heights = []
	widths = []
	for button_text in buttons_texts:
		answer = Label(0, 0, button_width, button_text, fonts["PixelArt"], (255, 255, 255))
		heights.append(answer.height * 2)
		widths.append(answer.width * 2)
	button_height = max(heights)
	button_width = max(widths) * 2
	buttons_surface_width = button_width * buttons_num + space * (buttons_num - 1)
	buttons_surface = pygame.Surface((buttons_surface_width, button_height))
	buttons_surface.fill((45 - 5, 5 - 5, 42 - 5))
	buttons_surface_x = window_width // 2 - buttons_surface_width // 2
	buttons_surface_y = window_height - button_height
	question_label.y = buttons_surface_y - question_label.height
	for button_text in buttons_texts:
		button_image = pygame.Surface((button_width, button_height))
		button_image.fill((253, 176, 30))
		answer = Label(button_width // 2, button_height // 2, button_width, button_text, fonts["PixelArt"], (0, 0, 0), "yes")
		answer.draw(button_image)
		buttons.append([button_text, Button(x, 0, button_image, button_image, buttons_surface_x, buttons_surface_y)])
		x += button_width + space
	second_width = round(window_width / timer)
	time_1 = time()
	while True:
		time_2 = time()
		if window_width - (round(time_2 - time_1) * second_width) == 0:
			return False
		window.fill((45, 5, 42))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			for button in buttons:
				button[-1].update(event)
				if button[-1].pressed:
					if button[0] == true_answer:
						return True
					else:
						return False
			quit_button.update(event)
			if quit_button.pressed:
				pygame.quit()
		pygame.draw.rect(window, (45 - 5, 5 - 5, 42 - 5), (0, buttons_surface_y, window_width, window_height - buttons_surface_y))
		for button in buttons:
			button[-1].draw(buttons_surface)
		window.blit(buttons_surface, (buttons_surface_x, buttons_surface_y))
		question_label.draw(window)
		number_label.draw(window)
		quit_button.draw(window)
		pygame.draw.rect(window, (255, 255, 255), (0, 0, window_width - (round(time_2 - time_1) * second_width), 10))
		pygame.display.flip()
# "How long is everest?"
levels = [
	[10, "What is the number 16 of 16.1?", 4, ["16.01", "16.10001", "16.11", "16.99"], "16.01"],
	[30, "16 - (91 + 9) = 5x", 2, ["-16.8", "16.8"], "-16.8"],
	[30, "The speed of the ship in the direction of the river current = 18 km / h. The speed of the ship in the opposite direction to the river current = 15 km / h. river flow velocity-?", 4, ["3km/h", "1.5km/h", "1.55km/h", "3.5km/h"], "1.5km/h"],
	[30, "Two cars started moving towards each other. The speed of the first car is 30 km / h. The speed of the second car is 15 km / h. S = 90 km. How many hours after they start moving?", 4, ["2", "1", "3", "4"], "2"],
	[30, "The day began. How many hours later will the clock return to where it stood at the beginning of the day?", 3, ["12", "24", "6"], "12"],
	[30, "The car crossed the road in 6 hours. S = 60 km car speed-?", 3, ["10km/h", "15km/h", "6km/h"], "10km/h"]
]
max_rating = 10
rating = 0
num = 1
for level in levels:
	answer = Quiz(level[0], f"{num} of {len(levels)}", level[1], level[2], level[3], level[4])
	if answer:
		rating += max_rating / len(levels)
	num += 1
rating_label = Label(window_width // 2, window_height // 2, window_width // 2, f"rating is {round(rating)} from {max_rating}", fonts["PixelArt"], (255, 255, 255), "yes")
while True:
	window.fill((45, 5, 42))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		quit_button.update(event)
		if quit_button.pressed:
			pygame.quit()
	quit_button.draw(window)
	rating_label.draw(window)
	pygame.display.flip()