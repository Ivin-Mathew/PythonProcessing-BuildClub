import cv2
import numpy as np
import time

def draw_scene(circle_y, obstacle_x, score):
    game_over = False
    line = np.zeros((500, 500, 3), dtype=np.uint8)
    line[:] = (255, 255, 255)

    cv2.putText(line, f"Score = {score}", (300, 75), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))

    floorStart = [0, 400]
    floorEnd = [500, 400]
    cv2.line(line, floorStart, floorEnd, (0, 0, 0), 2)

    obstacle1Start = [obstacle_x, 400]
    obstacle1End = [obstacle_x + 10, 360]
    cv2.rectangle(line, obstacle1Start, obstacle1End, (0, 0, 0), 2)
    cv2.circle(line, (100, circle_y), 25, (0, 255, 0), 2)

    # Collision detection
    if 373> circle_y > 330 and 75 < obstacle_x < 125:
        cv2.putText(line, "GAME OVER", (200, 250), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
        game_over = True

    cv2.imshow("Assignment 3", line)
    return game_over

circle_y = 373
jump_height = 75
obstacle_x = 350
score = 0
game_over=False

cv2.namedWindow("Assignment 3", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Assignment 3", 500, 500)


while True:
    if not game_over:  # Game is not over
        game_over = draw_scene(circle_y, obstacle_x, score)
        key = cv2.waitKey(1)

        obstacle_x -= 1
        if obstacle_x < -10:
            obstacle_x = 500

        if obstacle_x % 50 == 0:
            score += 1

        if key == ord(' '):
            for _ in range(jump_height):
                circle_y -= 1
                obstacle_x -= 1
                if obstacle_x % 50 == 0:
                    score += 1
                if draw_scene(circle_y, obstacle_x, score):
                    break
                cv2.waitKey(1)

            for _ in range(jump_height):
                circle_y += 1
                obstacle_x -= 1
                if obstacle_x % 50 == 0:
                    score += 1
                if draw_scene(circle_y, obstacle_x, score):
                    break
                cv2.waitKey(1)

    else:  # Game is over
        if key == ord('q'):
            break

    if key == ord('q'):
        break

cv2.destroyAllWindows()