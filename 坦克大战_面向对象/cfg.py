import os

SCREEN_X=800
SCREEN_Y=600
SCREEN_SICE = [SCREEN_X,SCREEN_Y]

'''字体''' #创建具有自定义的一种字体格式
FONTPATH = os.path.join(os.getcwd(), 'resources/font/font.ttf')
'''子弹图片'''
BULLET_IMAGE_PATHS = {
    'up': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_up.png'),
    'down': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_down.png'),
    'left': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_left.png'),
    'right': os.path.join(os.getcwd(), 'resources/images/bullet/bullet_right.png')
}
'''敌对坦克的图片路径 4种不同的坦克'''
ENEMY_TANK_IMAGE_PATHS = {
    '1': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_3.png')
    ],
    '2': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_3.png')
    ],
    '3': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_3.png')
    ],
    '4': [
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_0.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_1.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_2.png'),
        os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_4_3.png')
    ]
}
'''玩家坦克图片的路径'''
PLAYER_TANK_IMAGE_PATHS = {
    'player1': [
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_0.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_1.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T1_2.png')
    ],
    'player2': [
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_0.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_1.png'),
        os.path.join(os.getcwd(), 'resources/images/playerTank/tank_T2_2.png')
    ]
}

'''道具图片的路径'''
FOOD_IMAGE_PATHS = {
    'boom': os.path.join(os.getcwd(), 'resources/images/food/food_boom.png'),
    'clock': os.path.join(os.getcwd(), 'resources/images/food/food_clock.png'),
    'gun': os.path.join(os.getcwd(), 'resources/images/food/food_gun.png'),
    'iron': os.path.join(os.getcwd(), 'resources/images/food/food_iron.png'),
    'protect': os.path.join(os.getcwd(), 'resources/images/food/food_protect.png'),
    'star': os.path.join(os.getcwd(), 'resources/images/food/food_star.png'),
    'tank': os.path.join(os.getcwd(), 'resources/images/food/food_tank.png')
}
'''玩家自己基地图片的路径'''
HOME_IMAGE_PATHS = [
    os.path.join(os.getcwd(), 'resources/images/home/home1.png'),
    os.path.join(os.getcwd(), 'resources/images/home/home_destroyed.png')
]
'''背景图片的路径'''
SCENE_IMAGE_PATHS = {
    'brick': os.path.join(os.getcwd(), 'resources/images/scene/brick.png'),
    'ice': os.path.join(os.getcwd(), 'resources/images/scene/ice.png'),
    'iron': os.path.join(os.getcwd(), 'resources/images/scene/iron.png'),
    'river1': os.path.join(os.getcwd(), 'resources/images/scene/river1.png'),
    'river2': os.path.join(os.getcwd(), 'resources/images/scene/river2.png'),
    'tree': os.path.join(os.getcwd(), 'resources/images/scene/tree.png')
}
'''其他图片的路径'''
OTHER_IMAGE_PATHS = {
    'appear': os.path.join(os.getcwd(), 'resources/images/others/appear.png'),
    'background': os.path.join(os.getcwd(), 'resources/images/others/background.png'),
    'boom_dynamic': os.path.join(os.getcwd(), 'resources/images/others/boom_dynamic.png'),
    'boom_static': os.path.join(os.getcwd(), 'resources/images/others/boom_static.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/images/others/gameover.png'),
    'logo': os.path.join(os.getcwd(), 'resources/images/others/logo.png'),
    'mask': os.path.join(os.getcwd(), 'resources/images/others/mask.png'),
    'protect': os.path.join(os.getcwd(), 'resources/images/others/protect.png'),
    'tip': os.path.join(os.getcwd(), 'resources/images/others/tip.png'),
    'gamebar': os.path.join(os.getcwd(), 'resources/images/others/gamebar.png')
}
'''音效的路径'''
AUDIO_PATHS = {
    'add': os.path.join(os.getcwd(), 'resources/audios/add.wav'),
    'bang': os.path.join(os.getcwd(), 'resources/audios/bang.wav'),
    'blast': os.path.join(os.getcwd(), 'resources/audios/blast.wav'),
    'fire': os.path.join(os.getcwd(), 'resources/audios/fire.wav'),
    'Gunfire': os.path.join(os.getcwd(), 'resources/audios/Gunfire.wav'),
    'hit': os.path.join(os.getcwd(), 'resources/audios/hit.wav'),
    'start': os.path.join(os.getcwd(), 'resources/audios/start.wav')
}