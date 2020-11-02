class Label():
	def __init__(self, x, y, width, text, font, color, center = "no"):
		self.x = x
		self.y = y
		self.width = width
		self.font = font
		self.color = color
		self.lines = [""]
		self.center = center
		self.height = self.font.render("f", True, (255, 56, 123)).get_height()
		width = 0
		for letter in text:
			text_render = self.font.render(letter, True, (255, 255, 255))
			width += text_render.get_width()
			if width > self.width:
				width = 0
				self.lines.append("")
				self.height += text_render.get_height()
			self.lines[-1] += letter
	def draw(self, window):
		if self.center == "yes":
			y = self.y - self.height // 2
		else:
			y = self.y
		for line in self.lines:
			text_render = self.font.render(line, True, self.color)
			if self.center == "yes":
				window.blit(text_render, (self.x - text_render.get_width() // 2, y))
			else:
				window.blit(text_render, (self.x, y))
			y += text_render.get_height()