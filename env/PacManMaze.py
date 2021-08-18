import pygame
from env.Ghost import *
from utils.Graph import *
from Agent import *

# SCORE
score = 0
# FONT
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
font = pygame.font.SysFont('consolas', 20)
# SCREEN SIZES
tile_size = 16
width = 28 * tile_size
height = 31 * tile_size
screen = pygame.display.set_mode((width + 400, height))
cols, rows = (28, 31)
grid = [[0 for i in range(cols)] for j in range(rows)]

pygame.init()
done = False
# MAP
FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
GRAY = (255 // 2, 255 // 2, 255 // 2)
BLACK = (0, 0, 0)

#print(grid)
sprites = pygame.image.load("../images/map.png")
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




coin_grid = copy_arr(grid)
rewards = copy_arr(grid)

print("AICI")
print(rows, cols)

for i in range(rows):
    for j in range(cols):
        if rewards[i][j] == 1:
            rewards[i][j] = 10
        else:
            rewards[i][j] = -10
copy_rewards = copy_arr(rewards)

# print("Avem : {}\n".format(get_number_of_nodes_from_grid(grid)))

def draw_coins(g):
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x] == 1:
                pygame.draw.circle(screen, WHITE, (x * tile_size + tile_size / 2, y * tile_size + tile_size / 2), 1)


def draw_path(path, ghost_1):
    for x in range(len(path) - 1):
        pygame.draw.line(screen, (225, 255, 0), (graph.nodes[ghost_1.heading].y * tile_size + tile_size / 2,
                                                 graph.nodes[ghost_1.heading].x * tile_size + tile_size / 2), (
                             graph.nodes[path[-1]].y * tile_size + tile_size / 2,
                             graph.nodes[path[-1]].x * tile_size + tile_size / 2)
                         )

        pygame.draw.line(screen, (255, 255, 0), (
            graph.nodes[path[x]].y * tile_size + tile_size / 2, graph.nodes[path[x]].x * tile_size + tile_size / 2), (
                             graph.nodes[path[x + 1]].y * tile_size + tile_size / 2,
                             graph.nodes[path[x + 1]].x * tile_size + tile_size / 2))


def draw_map(screen, grid):
    for k in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            # if grid[k][j] == 1:
            #     pygame.draw.rect(screen, GRAY, pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))
            if grid[k][j] == 2:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))
            if grid[k][j] == 3:
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(j * tile_size, k * tile_size, tile_size, tile_size))

    return


def draw_line(at, to, grid):
    #print(to, at)
    if at[0] == to[0]:
        if at[1] - to[1] > 0:
            for x in range(to[1], at[1] + 1):
                grid[x][at[0]] = 1
            return

        for x in range(at[1], to[1] + 1):
            grid[x][at[0]] = 1
        return
    elif at[1] == to[1]:

        if at[0] - to[0] > 0:
            for x in range(to[0], at[0] + 1):
                grid[at[1]][x] = 1
            return

        for x in range(at[0], to[0] + 1):
            grid[at[1]][x] = 1
        return


mouseCounter = 0
mouseRes = [0, 0]
at = 0
to = 0

n_nodes, node_grid = get_number_of_nodes_from_grid(grid)
graph = Graph(n_nodes)
graph.make_graph(node_grid)

#player = Player(1, 1, grid, screen)
ghosts = []




# ghost_1 = Ghost(screen, graph.nodes[65].x, graph.nodes[65].y, grid)
# ghost_1.head_to_node(pick_next_node(graph, 65), graph)
# ghosts.append(ghost_1)
# ghost_2 = Ghost(screen, graph.nodes[64].x, graph.nodes[64].y, grid)
# ghost_2.head_to_node(pick_next_node(graph, 64), graph)
# ghosts.append(ghost_2)
# ghost_3 = Ghost(screen, graph.nodes[63].x, graph.nodes[63].y, grid)
# ghost_3.head_to_node(pick_next_node(graph, 63), graph)
# ghosts.append(ghost_3)
# ghost_4 = Ghost(screen, graph.nodes[62].x, graph.nodes[62].y, grid)
# ghost_4.head_to_node(pick_next_node(graph, 62), graph)
# ghosts.append(ghost_4)
player = ApproximateQAgent(1, 1, grid, screen,ghosts,coin_grid)
def create_reset_ghost():
    player.ghosts.clear()
    ghost_1 = Ghost(screen, graph.nodes[22].x, graph.nodes[22].y, grid)
    ghost_1.head_to_node(pick_next_node(graph, 22,ghost_1), graph)
    player.ghosts.append(ghost_1)

    ghost_2 = Ghost(screen, graph.nodes[25].x, graph.nodes[25].y, grid)
    ghost_2.head_to_node(pick_next_node(graph, 25,ghost_2), graph)
    player.ghosts.append(ghost_2)
    ghost_3 = Ghost(screen, graph.nodes[32].x, graph.nodes[32].y, grid)
    ghost_3.head_to_node(pick_next_node(graph, 32,ghost_3), graph)
    player.ghosts.append(ghost_3)
    ghost_4 = Ghost(screen, graph.nodes[33].x, graph.nodes[33].y, grid)
    ghost_4.head_to_node(pick_next_node(graph, 33,ghost_4), graph)
    player.ghosts.append(ghost_4)


create_reset_ghost()

#
# dfs(graph, 0, node_grid)
# print(pick_next_node(graph, 0))
# parent = dijkstra(graph, 0)
# print_path(parent, 0, 65)
# print(pygame.font.get_fonts())
# path = create_path(parent, 0, 65)
# ghost_1.head_to_node(path.pop(-1), graph)
target_grid = copy_arr(grid)
def winGame(coin_grid):
    rows = len(coin_grid)
    cols = len(coin_grid[0])

    for i in range(rows):
        for j in range(cols):
            if coin_grid[i][j]==1:
                return 1
    return 0
#"""
while done < 50:
    print("Episode ", done)
    game_over = 0
    rewards=copy_arr(copy_rewards)
    state = player.get_pos()
    while not game_over:

        if player.coin_grid[player.y][player.x] == 1:
            player.coin_grid[player.y][player.x] = 0
            score += 10

        # CHECK FOR DEATH AND RESET ENV
        for ghost in player.ghosts:
            if player.x == ghost.y and player.y == ghost.x:
                player.x = 1
                player.y = 1
                player.coin_grid = copy_arr(grid)
                score = 0
                game_over = 1
                done+=1
                create_reset_ghost()
        if winGame(player.coin_grid) == 0:
            player.x = 1
            player.y = 1
            player.coin_grid = copy_arr(grid)
            print("WIN at ", score)
            score = 0
            game_over = 1
            done += 1
            create_reset_ghost()

        for ghost in player.ghosts:
            # DELETE ghos.check_delay() FOR PICKING AND MOVING THE NEXT STEP
            #if ghost.check_delay():
            hasArrived = ghost.run(graph)
            if hasArrived:
                ghost.head_to_node(pick_next_node(graph, ghost.heading,ghost.depart), graph)
        #print(state)
        action = player.getAction(state,-1)
        #print(action)
        new_state = player.take_action(action)

        reward = rewards[new_state[1]][new_state[0]]
        for g in player.ghosts:
            if new_state == g.get_pos():
                reward = -1
        if reward > 0:
            rewards[new_state[1]][new_state[0]] = -1
        player.update(state,action,new_state,reward)
        state = new_state
        # draw_path(path)
        # if ghost_1.check_delay():
        #     hasArrived = ghost_1.run(graph)
        #     if hasArrived and len(path):
        #         print(path)
        #         ghost_1.head_to_node(path.pop(-1), graph)

#"""
        # print(pygame.mouse.get_pressed(1))

done = 0
while done < 200:
    print("Episode ", done)
    game_over = 0
    state = player.get_pos()
    rewards=copy_arr(copy_rewards)
    player.alpha=0
    player.epsilon=0
    while not game_over:

        textsurface = font.render(
            "Heading to x:{:2d} y:{:2d} id:{:2d}".format(ghosts[0].heading_x, ghosts[0].heading_y, ghosts[0].heading),
            False,
            (255, 255, 255))
        scoresurface = font.render(
           "Score: {:6d}".format(score), False,
           (255, 255, 255))
        screen.fill(BLACK)
        screen.blit(sprites, (0, 0), (0, tile_size * 3, width, height))
        draw_map(screen, target_grid)
        # for k in range(0, 28):
        #     pygame.draw.line(screen, GRAY, (k * tile_size, 0), (k * tile_size, height))
        # for k in range(0, 31):
        #     pygame.draw.line(screen, GRAY, (0, k * tile_size), (width, k * tile_size))
        player.circle = pygame.Rect(consts.tile_size * player.x ,consts.tile_size * player.y ,consts.tile_size*2,consts.tile_size *2)
        player.circle.center = player.x * consts.tile_size,player.y*consts.tile_size
        pygame.draw.rect(screen,(245,65,35),player.circle,16)
        for ghost in player.ghosts:
            ghost.rect = pygame.Rect(consts.tile_size * ghost.y ,
                                    consts.tile_size * ghost.x , consts.tile_size*2,
                                    consts.tile_size*2)
            ghost.rect.center= ghost.y*consts.tile_size,ghost.x*consts.tile_size
            pygame.draw.rect(screen,(245,65,35),ghost.rect,16)

            #if player.x == ghost.y and player.y == ghost.x:
            if player.circle.colliderect(ghost.rect):
                print(player.circle)
                print(ghost.rect)
                player.x = 1
                player.y = 1
                player.coin_grid = copy_arr(grid)
                print("LOST at ", score)
                score = 0
                game_over = 1
                done += 1
                create_reset_ghost()


            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     res = pygame.mouse.get_pos()
            #     print(res)
            #     if node_grid[res[1] // tile_size][res[0] // tile_size] == 3:
            #         print("Is node idx: {}".format(graph.find_node_index(get_id(res[1] // tile_size, res[0] // tile_size))))
            #         to_node = graph.find_node_index(get_id(res[1] // tile_size, res[0] // tile_size))
            #         at_node = ghost_1.heading
            #         print("At: {:2d} To:{:2d}".format(at_node, to_node))
            #         parent = dijkstra(graph, at_node)
            #         print_path(parent, at_node, to_node)
            #         path = create_path(parent, at_node, to_node)
            #         print(parent)
            # if mouseCounter % 2 == 0:
            #     res = pygame.mouse.get_pos()
            #     at = res
            #     print("Pressed at {} , {}\t that is at {},{}\n".format(res[0], res[1], res[0] // tile_size,
            #                                                            res[1] // tile_size))
            # if mouseCounter % 2 == 1:
            #     res = pygame.mouse.get_pos()
            #     to = res
            #     print("Pressed at {} , {}\t that is at {},{}\n".format(res[0], res[1], res[0] // tile_size,
            #                                                            res[1] // tile_size))
            #     draw_line([at[0] // tile_size, at[1] // tile_size],
            #               [to[0] // tile_size, to[1] // tile_size],
            #               grid)
            #     print("Line Draw")
            # mouseCounter += 1
            #if event.type == pygame.KEYDOWN:
             #   pressed = pygame.key.get_pressed()

              #  if pressed[pygame.K_a]:
               #     print("A")
                #    player.set_pos(player.x - 1, player.y)
               # if pressed[pygame.K_d]:
                #    print("D")
                 #   player.set_pos(player.x + 1, player.y)

                #if pressed[pygame.K_w]:
                 #   print("W")
                  #  player.set_pos(player.x, player.y - 1)

                #if pressed[pygame.K_s]:
                 #   print("S")
                  #  player.set_pos(player.x, player.y + 1)

        # COIN COLLECT
        if player.coin_grid[player.y][player.x] == 1:
            player.coin_grid[player.y][player.x] = 0
            score += 10

        # CHECK FOR DEATH AND RESET ENV


        if winGame(player.coin_grid) == 0:
            player.x = 1
            player.y = 1
            player.coin_grid = copy_arr(grid)
            print("WIN at ", score)
            score = 0
            game_over = 1
            done += 1
            create_reset_ghost()


        draw_coins(player.coin_grid)



        #print(state)
        #print( player.getLegalActions(state))
        action = player.getAction(state,-1)
        #print(action)
        new_state = player.take_action(action)


       # print(player.getQValue(state,action))
        reward = rewards[new_state[1]][new_state[0]]
        for g in player.ghosts:
            if new_state == g.get_pos():
                print("reward negativ")
                reward = -5
        #for f in player.featExtractor.getFeatures(state,action,player.ghosts,player.coin_grid,player.grid):
         #   print(f, player.featExtractor.getFeatures(state, action, player.ghosts, player.coin_grid, player.grid).get(f),
          #        player.weights[f],reward)
        if reward > 0 :
            rewards[new_state[1]][new_state[0]] = -1
        player.update(state,action,new_state,reward)
        state = new_state

        # draw_path(path)
        # if ghost_1.check_delay():
        #     hasArrived = ghost_1.run(graph)
        #     if hasArrived and len(path):
        #         print(path)
        #         ghost_1.head_to_node(path.pop(-1), graph)
        print("player")
        print(player.circle)
        for ghost in player.ghosts:

            print(ghost.rect)
            # DELETE ghos.check_delay() FOR PICKING AND MOVING THE NEXT STEP
            # if ghost.check_delay():
            hasArrived = ghost.run(graph)
            if hasArrived:
                ghost.head_to_node(pick_next_node(graph, ghost.heading, ghost.depart), graph)

        for ghost in player.ghosts:
            ghost.draw()
        player.draw()

        # print(pygame.mouse.get_pressed(1))

        screen.blit(textsurface, (width + 20, 20))
        screen.blit(scoresurface, (width + 20, 50))
        pygame.display.flip()
        fpsClock.tick(60)
    # print("x: {} y:{} x:{} y:{}".format(player.x,player.y,ghost_1.,ghost_1.y))
# for x in graph.dTable:
#     print(x)
