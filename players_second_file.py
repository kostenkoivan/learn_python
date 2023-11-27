from players_class import Player

Player.set_cls_field(10)
x = Player()
print(x.lvl)

Player.set_cls_field()
y = Player()
y.lvl = 10
print(y.lvl)