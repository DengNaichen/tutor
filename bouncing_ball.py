import pygame
import sys
import random

# 初始化 pygame
pygame.init()

# 设置窗口大小
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# 颜色定义
black = (0, 0, 0)
# 随机颜色
ball_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# 球的属性
radius = 30  # 中等大小

# '从窗口的左下角开始出现'
# Pygame的坐标系原点(0,0)在左上角，所以左下角的y值接近height
x = radius
y = height - radius

# '向上移动' (给一个向上的y速度，和一个向右的x速度，这样才能移动并发生不断反弹)
speed_x = 5
speed_y = -7

# 限制帧率的Clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新球的位置
    x += speed_x
    y += speed_y

    # 模拟物理碰撞 - 边缘检测
    # 碰到左右边缘反弹
    if x - radius <= 0 or x + radius >= width:
        speed_x = -speed_x

    # 碰到上下边缘反弹
    if y - radius <= 0 or y + radius >= height:
        speed_y = -speed_y

    # 绘制背景
    screen.fill(black)

    # 绘制球
    pygame.draw.circle(screen, ball_color, (int(x), int(y)), radius)

    # 刷新屏幕显示
    pygame.display.flip()

    # 控制帧率为60FPS
    clock.tick(60)
