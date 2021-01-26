import  os

FPS =100  #定义帧率
SCREENSIZE = (800, 600)
'''使用绝对地址，这种方法不方便移植'''
IMAGE_PATHS={   # 不方便移植
    'rabbit':os.path.join(os.getcwd(),'resous/images/dude2.png'),
    'grass' :os.path.join(os.getcwd(),'resous/images/grass.png'),
    'castle':os.path.join(os.getcwd(),'resous/images/castle.png'),
    'arrow' :os.path.join(os.getcwd(),'resous/images/bullet.png'),
    'badguy': os.path.join(os.getcwd(),'resous/images/badguy.png'),
    'healthbar': os.path.join(os.getcwd(),'resous/images/healthbar.png'),
    'health': os.path.join(os.getcwd(),'resous/images/health.png'),
    'gameover': os.path.join(os.getcwd(), 'resous/images/gameover.png'),
    'youwin': os.path.join(os.getcwd(), 'resous/images/youwin.png')
}

SOUNDS_PATHS={
    'hit': os.path.join(os.getcwd(), 'resous/audio/explode.wav'),
    'enemy': os.path.join(os.getcwd(), 'resous/audio/enemy.wav'),
    'shoot': os.path.join(os.getcwd(), 'resous/audio/shoot.wav'),
    'moonlight': os.path.join(os.getcwd(), 'resous/audio/moonlight.wav')
}