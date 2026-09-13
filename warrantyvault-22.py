# === Stage 22: Add favorite records and quick favorite listing ===
# Project: WarrantyVault
import json
from pathlib import Path

class FavoriteItem:
    def __init__(self, item_id, favorite_index):
        self.item_id = item_id
        self.favorite_index = favorite_index

    def to_dict(self):
        return {"item_id": self.item_id, "favorite_index": self.favorite_index}

    @staticmethod
    def from_dict(d):
        return FavoriteItem(d["item_id"], d["favorite_index"])


class FavoriteList:
    def __init__(self):
        self.items = []
        self.next_index = 0

    def add(self, item_id):
        if item_id in self.items:
            return False
        self.items.append(FavoriteItem(item_id, self.next_index))
        self.next_index += 1
        return True

    def remove(self, item_id):
        for i, fav in enumerate(self.items):
            if fav.item_id == item_id:
                self.items.pop(i)
                return True
        return False

    def is_favorite(self, item_id):
        return any(fav.item_id == item_id for fav in self.items)

    def get_favorites(self):
        return [fav.to_dict() for fav in self.items]

    def clear(self):
        self.items = []
        self.next_index = 0

    def to_dict(self):
        return {"favorites": self.get_favorites()}

    @staticmethod
    def from_dict(d):
        fav_list = FavoriteList()
        fav_list.items = [FavoriteItem.from_dict(f) for f in d["favorites"]]
        fav_list.next_index = len(fav_list.items)
        return fav_list
