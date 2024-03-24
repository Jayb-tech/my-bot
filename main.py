import logging
import asyncio
import sys 
from asyncio import run as arun
from highrise.__main__ import *
import time
from flask import Flask
from keep_alive import keep_alive
keep_alive()
from threading import Thread
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task

from highrise import *
from highrise import BaseBot, Position, __main__
from highrise.models import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
import asyncio
import sys
from asyncio import run as arun

from highrise import *
from highrise import BaseBot, Position, __main__
from highrise.models import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)


vip = [
    "iced_yu", "raavitheriver", "QueenKirsty02", "Vulps", "PunkAngel3",
    "yankii_gg", "__.Mami.__", "iGraceGiselle", "LaceyWolf12345",
    "m.jamie"
]


class Bot(BaseBot):

  def __init__(self):
    self.user_teleport_position = Position(x=1.5,
                                           y=0.25,
                                           z=14.5,
                                           facing='FrontRight')
    self.user_teleport_position2 = Position(x=5.5,
                                            y=10.0,
                                            z=3.5,
                                            facing='FrontRight')
    self.user_teleport_position3 = Position(x=10.5,
                                            y=14.75,
                                            z=4.5,
                                            facing='FrontLeft')
    self.user_loops = {}
    self.position_emote_state = {
    }  # Dictionary to track emote state per position

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    import asyncio
    # asyncio.ensure_future(self.dance())

    print("hi im alive?")
    self.highrise.tg.create_task(
        self.highrise.teleport(
            session_metadata.user_id,
            Position(x=13.5, y=1.0, z=6.5, facing='FrontRight')))

    # users = await self.get_users(['m.jamies'], '22331')
    # print(users)

  async def get_users(self, selected_users, default_user):
    target_users = []
    if len(selected_users) == 0:
      return [default_user]

    users = await self.highrise.get_room_users()
    for user in users.content:
      if user[0].username in selected_users:
        target_users.append(user[0])
    return target_users

  # async def dance(self):
  #   import asyncio
  #   counter = 0
  #   while True:
  #     for emote in emotes:
  #       for user in vvip:
  #         send emote
  #     await asyncio.sleep(1)
  #     counter += 1

  # Fix indentation for on_user_join method
  async def on_user_join(self, user: User,
                         position: Position | AnchorPosition) -> None:
    print(user.usernaname)
  pos_emote_dict = {
    
    "blow": {
                       "emote": "emote-headblowup",
                       "delay": 11.667537
                   },
                   "skate": {
                       "emote": "emote-iceskating",
                       "delay": 7.299156
                   },
                   "boxer": {
                       "emote": "emote-boxer",
                       "delay": 5.555702
                   },
                   "tired": {
                       "emote": "emote-tired",
                       "delay": 10
                   },
                   "dance": {
                       "emote": "dance-macarena",
                       "delay": 12.5
                   },
                   "loopsit": {
                       "emote": "idle-loop-sitfloor",
                       "delay": 10
                   },
                   "weird": {
                       "emote": "dance-weird",
                       "delay": 22
                   },
                   "laugh": {
                       "emote": "emote-laughing",
                       "delay": 3
                   },
                   "kiss": {
                       "emote": "emote-kiss",
                       "delay": 3
                   },
                   "wave": {
                       "emote": "emote-wave",
                       "delay": 10
                   }
  }

  
  emote_dict = {
      "blow": {
          "emote": "emote-headblowup",
          "delay": 11.667537
      },
      "skate": {
          "emote": "emote-iceskating",
          "delay": 7.299156
      },
      "boxer": {
          "emote": "emote-boxer",
          "delay": 5.555702
      },
      "tired": {
          "emote": "emote-tired",
          "delay": 10
      },
      "dance": {
          "emote": "dance-macarena",
          "delay": 12.5
      },
      "loopsit": {
          "emote": "idle-loop-sitfloor",
          "delay": 10
      },
      "weird": {
          "emote": "dance-weird",
          "delay": 22
      },
      "laugh": {
          "emote": "emote-laughing",
          "delay": 3
      },
      "kiss": {
          "emote": "emote-kiss",
          "delay": 3
      },
      "wave": {
          "emote": "emote-wave",
          "delay": 10
      },
      "teleport": {
          "emote": "emote-teleporting",
          "delay": 12.5
      },
      "hot": {
          "emote": "emote-hot",
          "delay": 4.8
      },
      "shopping": {
          "emote": "dance-shoppingcart",
          "delay": 5
      },
      "greedy": {
          "emote": "emote-greedy",
          "delay": 4.8
      },
      "float": {
          "emote": "emote-float",
          "delay": 9.3
      },
      "yes": {
          "emote": "emote-yes",
          "delay": 10
      },
      "celebrate": {
          "emote": "emoji-celebrate",
          "delay": 4
      },
      "no": {
          "emote": "emote-no",
          "delay": 10
      },
      "swordfight": {
          "emote": "emote-swordfight",
          "delay": 6
      },
      "shy": {
          "emote": "emote-shy",
          "delay": 10
      },
      "tiktok2": {
          "emote": "dance-tiktok2",
          "delay": 11
      },
      "charging": {
          "emote": "emote-charging",
          "delay": 8.5
      },
      "worm": {
          "emote": "emote-snake",
          "delay": 6
      },
      "russian": {
          "emote": "dance-russian",
          "delay": 10.3
      },
      "sad": {
          "emote": "emote-sad",
          "delay": 10
      },
      "cursing": {
          "emote": "emoji-cursing",
          "delay": 2.5
      },
      "flex": {
          "emote": "emoji-flex",
          "delay": 3
      },
      "gagging": {
          "emote": "emoji-gagging",
          "delay": 6
      },
      "tiktok8": {
          "emote": "dance-tiktok8",
          "delay": 11
      },
      "kpop": {
          "emote": "dance-blackpink",
          "delay": 7
      },
      "pennywise": {
          "emote": "dance-pennywise",
          "delay": 1.5
      },
      "bow": {
          "emote": "emote-bow",
          "delay": 3.3
      },
      "curtsy": {
          "emote": "emote-curtsy",
          "delay": 2.8
      },
      "snowangel": {
          "emote": "emote-snowangel",
          "delay": 6.8
      },
      "energyball": {
          "emote": "emote-energyball",
          "delay": 8.3
      },
      "frog": {
          "emote": "emote-frog",
          "delay": 15
      },
      "cute": {
          "emote": "emote-cute",
          "delay": 7.3
      },
      "tiktok9": {
          "emote": "dance-tiktok9",
          "delay": 13
      },
      "shuffle": {
          "emote": "dance-tiktok10",
          "delay": 9
      },
      "pose7": {
          "emote": "emote-pose7",
          "delay": 5.3
      },
      "pose8": {
          "emote": "emote-pose8",
          "delay": 4.6
      },
      "casual": {
          "emote": "idle-dance-casual",
          "delay": 9.7
      },
      "pose1": {
          "emote": "emote-pose1",
          "delay": 3
      },
      "pose3": {
          "emote": "emote-pose3",
          "delay": 4.7
      },
      "pose5": {
          "emote": "emote-pose5",
          "delay": 5
      },
      "cutey": {
          "emote": "emote-cutey",
          "delay": 3.5
      },
      "model": {
          "emote": "emote-model",
          "delay": 6.3
      },
      "astro": {
          "emote": "emote-astronaut",
          "delay": 0
      },  # No delay specified, set to 0
      "guitar": {
          "emote": "emote-punkguitar",
          "delay": 10
      },
      "fashionista": {
          "emote": "emote-fashionista",
          "delay": 6
      },
      "uwu": {
          "emote": "idle-uwu",
          "delay": 25
      },
      "wrong": {
          "emote": "dance-wrong",
          "delay": 13
      },
      "sayso": {
          "emote": "idle-dance-tiktok4",
          "delay": 16
      },
      "maniac": {
          "emote": "emote-maniac",
          "delay": 5.5
      },
      "enthused": {
          "emote": "idle-enthusiastic",
          "delay": 16.5
      },
      "happy": {
          "emote": "emote-happy",
          "delay": 0
      },  # No delay specified, set to 0
      "timejump": {
          "emote": "emote-timejump",
          "delay": 1.9
      },  # No delay specified, set to 0
      "creepy": {
          "emote": "dance-creepypuppet",
          "delay": 10
      },
      "sleigh": {
          "emote": "emote-sleigh",
          "delay": 9
      },  # No delay specified, set to 0
      "singing": {
          "emote": "idle_singing",
          "delay": 12
      },
      "anime": {
          "emote": "dance-anime",
          "delay": 8.4
      },  # No delay specified, set to 0
      "hyped": {
          "emote": "emote-hyped",
          "delay": 6.7
      },  # No delay specified, set to 0
      "jingle": {
          "emote": "dance-jinglebell",
          "delay": 11.8
      },  # No delay specified, set to 0
      "snowball": {
          "emote": "emote-snowball",
          "delay": 6
      },
      "sit": {
          "emote": "idle-loop-sitfloor",
          "delay": 22.321055
      },
      "enthused": {
          "emote": "idle-enthusiastic",
          "delay": 15.941537
      },
      "yes": {
          "emote": "emote-yes",
          "delay": 2.565001
      },
      "pushit": {
          "emote": "dance-employee",
          "delay": 8
      },
      "gift": {
          "emote": "emote-gift",
          "delay": 5.8
      },
      "touch": {
          "emote": "dance-touch",
          "delay": 10.000
      },
      "creepycute": {
          "emote": "emote-creepycute",
          "delay": 7.902453
      },
      "kawaii": {
          "emote": "dance-kawai",
          "delay": 7.9
      },
  }

  async def send_emote_continuously(self, emote_data: dict,
                                    user_id: int) -> None:
    try:
      while user_id in self.user_loops:
        await self.highrise.send_emote(emote_data["emote"], user_id)
        await asyncio.sleep(emote_data["delay"])
    except asyncio.CancelledError:
      pass
    except Exception as e:
      print(f"An error occurred in send_emote_continuously: {e}")
      self.user_loops.pop(user_id, None)

  def _get_emote_commands_list(self):
    emotes_list = list(self.emote_dict.keys())
    unique_emotes = set(emotes_list)  # To ensure there are no duplicates
    formatted_list = ', '.join(unique_emotes)
    return f"You can use the following emotes: {formatted_list}. Just type the emote you want to use in the chat!"

  # async def on_user_move(self, user: User, pos: Position) -> None:
  #   """On a user moving in the room."""
  #   if user.username == "iced_yu":
  #       # Adjust the x-coordinate to be slightly to the right of iced_yu
  #       x_offset = 2  # You can adjust this value as needed
  #       new_x = pos.x + x_offset

  #       # Walk to the adjusted position
  #       await self.highrise.walk_to(Position(new_x, pos.y, pos.z, pos.facing))

  async def on_whisper(self, user: User, message: str) -> None:
    print(f"[WHISPER] {user.username}: {message}")
    if user.username.lower() in ["iced_yu", "m.jamie"]:
      message = message.strip().lower()
      if message == "stop":
        # Cancel all ongoing loops for all users
        for _user_id, loop_data in list(self.user_loops.items()):
          loop_data['loop'].cancel()
        self.user_loops = {}  # Clear the loops dictionary
      else:
        words = message.split()
        if words and words[0] in self.emote_dict:
          command = self.emote_dict[words[0]]
          if len(words) > 1 and words[1] == "loop":
            # Loop command detected, initiate emote loop for all users
            room_users_res = await self.highrise.get_room_users()
            for item in room_users_res.content:
              room_user = item[0]
              if room_user.id not in self.user_loops:
                loop_task = asyncio.create_task(
                    self.send_emote_continuously(command, room_user.id))
                self.user_loops[room_user.id] = {
                    'command': command,
                    'loop': loop_task
                }
            # Notify all users that the emote loop has started
            await self.highrise.chat(
                f"Emote loop for '{words[0]}' started by {user.username}.")
          elif not words[1:]:
            # If no additional commands after the emote, send it once
            room_users_res = await self.highrise.get_room_users()
            for item in room_users_res.content:
              room_user = item[0]
              await self.highrise.send_emote(command["emote"], room_user.id)

  async def on_chat(self, user: User, message: str) -> None:
    message = message.strip().lower()
    print(user.username + ": " + message)
    operation = message.split('@')
    command = operation[0].strip()
    selected_users = [u.strip() for u in operation[1:]]

    target_users = await self.get_users(selected_users, user)
    for target_user in target_users:
      print(target_user, user.username in vip)
      if command == "!teleport" and user.username in vip:
        print('yes')
        await self.highrise.teleport(target_user.id,
                                     self.user_teleport_position2)
      elif command == "!down" and user.username in vip:
        await self.highrise.teleport(target_user.id,
                                     self.user_teleport_position)
      elif command == "!vip" and user.username in vip:
        await self.highrise.teleport(target_user.id,
                                     self.user_teleport_position3)

    if message == "emotes":
      emotes_list = list(self.emote_dict.keys())
      chunk_size = 10  # This is an example, adjust the chunk size based on the game's limits
      chunks = [
          emotes_list[i:i + chunk_size]
          for i in range(0, len(emotes_list), chunk_size)
      ]
      for chunk in chunks:
        emote_message = ', '.join(chunk)
        await self.highrise.chat(emote_message)
        await asyncio.sleep(1)

    elif message.lower() == "stop":
      # Handle stop command in a case-insensitive manner
      loop_data = self.user_loops.pop(user.id, None)
      if loop_data is not None:
        loop_data['loop'].cancel()

    # elif message.lower().startswith("/dress") and user.username == "iced_yu":
    #   await self.highrise.set_outfit(outfit=[
    #       Item(type='clothing',
    #            amount=1,
    #            id='body-flesh',
    #            account_bound=False,
    #            active_palette=1),
    #       Item(type='clothing',
    #            amount=4,
    #            id='hair_front-n_basic2020overshoulderpony',
    #            account_bound=False,
    #            active_palette=4),
    #       Item(type='clothing',
    #            amount=4,
    #            id='eyebrow-n_basic2018newbrows16',
    #            account_bound=False,
    #            active_palette=4),
    #       Item(type='clothing',
    #            amount=1,
    #            id='mouth-basic2018unimpressed',
    #            account_bound=False,
    #            active_palette=1),
    #       Item(
    #           type='clothing',
    #           amount=1,
    #           id='nose-n_room22019nosestud',
    #       ),
    #       Item(type='clothing',
    #            amount=1,
    #            id='shirt-n_philippineday2019filipinotop',
    #            account_bound=False,
    #            active_palette=-1),
    #       Item(type='clothing',
    #            amount=1,
    #            id='skirt-f_gianttutu',
    #            account_bound=False,
    #            active_palette=-1),
    #       Item(type='clothing',
    #            amount=1,
    #            id='shoes-n_starteritems2019flatswhite',
    #            account_bound=False,
    #            active_palette=-1),
    #       Item(type='clothing',
    #            amount=1,
    #            id='eye-n_basic2018malediamondsleepy',
    #            account_bound=False,
    #            active_palette=1),
    #       Item(type='clothing',
    #            amount=3,
    #            id='freckle-n_basic2018freckle35',
    #            account_bound=False,
    #            active_palette=3),
    #       Item(type='clothing',
    #            amount=3,
    #            id='blush-f_blush01',
    #            account_bound=False,
    #            active_palette=3),
    #       Item(type='clothing',
    #            amount=4,
    #            id='hair_back-n_basic2020overshoulderpony',
    #            account_bound=False,
    #            active_palette=4),
    #   ])
    else:
      words = message.split()
      if len(words) >= 1 and words[0] in self.emote_dict:
        command = self.emote_dict[words[0]]
        if "loop" in words:
          # Check if there is already an active loop for the user
          if user.id in self.user_loops:
            # If there's an existing loop, cancel it before starting a new one
            self.user_loops[user.id]['loop'].cancel()
          # Start a new loop
          loop_task = asyncio.create_task(
              self.send_emote_continuously(command, user.id))
          self.user_loops[user.id] = {'command': command, 'loop': loop_task}
        else:
          # Send the emote only once if the message contains only the emote name
          await self.highrise.send_emote(command["emote"], user.id)


bot_file_name = "main"
bot_class_name = "Bot"
room_id = "65a8236a0aa6b497a9b328a8"
bot_token = "637cc3e1dc30d3a2a377a3384a62f66220cfdf855eca608fba58c164d7e5bba0"

my_bot = BotDefinition(
    getattr(import_module(bot_file_name), bot_class_name)(), room_id,
    bot_token)

while True:
  try:
    definitions = [my_bot]
    arun(main(definitions))
  except Exception as e:
    print(f"An exception occourred: {e}")
    time.sleep(2)
