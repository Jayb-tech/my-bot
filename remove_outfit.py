from highrise import BaseBot, User
from highrise.models import *

categories = ["aura", "bag", "blush", "body", "dress", "earrings", "emote", "eye", "eyebrow", 
              "fishing_rod", "freckle", "fullsuit", "glasses", "gloves", "hair_back", 
              "hair_front", "handbag", "hat", "jacket", "lashes", "mole", "mouth", 
              "necklace", "nose", "rod", "shirt", "shoes", "shorts", "skirt", "sock", 
              "tattoo", "watch"]

async def remove(self: BaseBot, user: User, message: str):
    parts = message.split(" ")
    if len(parts) != 2:
        await self.highrise.chat("Invalid command format. You need to specify the category.")
        return

    category = parts[1].lower()
    if category not in categories:
        await self.highrise.chat("Invalid category.")
        return

    outfit = (await self.highrise.get_my_outfit()).outfit
    item_removed = False

    for outfit_item in outfit:
        item_category = outfit_item.id.split("-")[0][0:3]
        if item_category == category[0:3]:
            outfit.remove(outfit_item)
            item_removed = True

    if item_removed:
        await self.highrise.set_outfit(outfit)
        await self.highrise.chat(f"Removed items from the category '{category}'.")
    else:
        await self.highrise.chat(f"No items found in the category '{category}'.")

