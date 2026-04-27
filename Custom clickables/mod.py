import os

# MOD_DIR  — absolute path to your mod folder, set automatically by the loader
# MANIFEST — contents of manifest.json as a dict, set automatically by the loader

def register(game):
    # all mod setup goes here
    
    custom_clickable = os.path.join(MOD_DIR, "assets", "clickable.png")
    if os.path.exists(custom_clickable):
         game.set_flesh_image(custom_clickable)
         game.load_flesh_image()

    pass