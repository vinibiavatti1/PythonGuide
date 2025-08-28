"""
Flyweight

* Flyweight is a structural design pattern that allows you to share objects to
  support a large number of similar objects efficiently.
* It is used to minimize memory usage by sharing common parts of state between
  multiple objects.
"""


###############################################################################
# Flyweight
###############################################################################


# Texture
# * The texture class below represents the shared state of the sprites.
# * Since the same texture can be used by multiple sprites, it helps to save
#   memory.
class Texture:
    def __init__(self, data: bytes) -> None:
        self.data = data


# Sprite
# * The sprite class represents the unique state of each sprite.
# * It contains the position and the texture reference.
class Sprite:
    def __init__(self, x: int, y: int, texture: Texture) -> None:
        self.x = x
        self.y = y
        self.texture = texture


# Texture Factory
# * The texture factory is responsible for managing texture instances.
# * Note that we don't need to create a new texture instance if it already
#   exists. The pre-existing instance will be reused.
class TextureFactory:
    textures: dict[str, Texture] = {
        "tree": Texture(b"tree_texture_data"),
        "stone": Texture(b"stone_texture_data"),
    }

    @classmethod
    def get_texture(cls, key: str) -> Texture:
        return cls.textures[key]


# Testing
# * In the test below, note that the same texture instance is reused for
#   different sprite objects.
# * The print statements will show that the same texture instances are used,
#   comparing their IDs.
tree_texture = TextureFactory.get_texture("tree")
stone_texture = TextureFactory.get_texture("stone")
tree_sprite_1 = Sprite(0, 0, tree_texture)
tree_sprite_2 = Sprite(0, 1, tree_texture)
stone_sprite_1 = Sprite(1, 0, stone_texture)
stone_sprite_2 = Sprite(1, 1, stone_texture)
print(id(tree_sprite_1.texture) == id(tree_sprite_2.texture))
print(id(stone_sprite_1.texture) == id(stone_sprite_2.texture))
# True
# True
