import logging
import asyncio
import sys
from asyncio import run as arun
from highrise.__main__ import *
import time
from flask import Flask
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

vip = ["iced_yu", "raavitheriver", "Vulps", "Eve07_98", "Evy2025"]

class Bot(BaseBot):

    def __init__(self):
        self.user_teleport_position = Position(x=10.5, y=0.0, z=9.5, facing='FrontLeft')
        self.user_teleport_position2 = Position(x=5.5, y=9.0, z=2.5, facing='FrontRight')
        self.user_teleport_position3 = Position(x=16.5, y=15.0, z=14.5, facing='FrontLeft')
        self.user_loops = {}
        self.following_task = None


    async def on_start(self, session_metadata: SessionMetadata) -> None:
        logging.info("Bot is alive.")
        await self.highrise.teleport(session_metadata.user_id, Position(x=3.5, y=0.25, z=13.5, facing='FrontRight'))

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        try:
            welcome_message = f"Bienvenido/a a la sala, {user.username} ¡Para ver la lista de emotes, escribe 'emotes' en el chat!"
            pass
        except Exception as e:
            logging.error(f"An error occurred in on_user_join: {e}")
        logging.info(f"{user.username} joined the room at {position}")


    emote_dict = {
        "angry": {"emote": "emoji-angry", "delay": 10},
        "thumbsup": {"emote": "emoji-thumbsup", "delay": 10},
        "hello": {"emote": "emote-hello", "delay": 10},
        "tired": {"emote": "emote-tired", "delay": 10},
        "dance": {"emote": "dance-macarena", "delay": 12.5},
        "loopsit": {"emote": "idle-loop-sitfloor", "delay": 10},
        "weird": {"emote": "dance-weird", "delay": 22},
        "laugh": {"emote": "emote-laughing", "delay": 3},
        "kiss": {"emote": "emote-kiss", "delay": 3},
        "wave": {"emote": "emote-wave", "delay": 10},
        "teleport": {"emote": "emote-teleporting", "delay": 12.5},
        "hot": {"emote": "emote-hot", "delay": 4.8},
        "shopping": {"emote": "dance-shoppingcart", "delay": 5},
        "greedy": {"emote": "emote-greedy", "delay": 4.8},
        "float": {"emote": "emote-float", "delay": 9.3},
        "yes": {"emote": "emote-yes", "delay": 10},
        "celebrate": {"emote": "emoji-celebrate", "delay": 4},
        "no": {"emote": "emote-no", "delay": 10},
        "swordfight": {"emote": "emote-swordfight", "delay": 6},
        "shy": {"emote": "emote-shy", "delay": 10},
        "tiktok2": {"emote": "dance-tiktok2", "delay": 11},
        "charging": {"emote": "emote-charging", "delay": 8.5},
        "worm": {"emote": "emote-snake", "delay": 6},
        "russian": {"emote": "dance-russian", "delay": 10.3},
        "sad": {"emote": "emote-sad", "delay": 10},
        "cursing": {"emote": "emoji-cursing", "delay": 2.5},
        "flex": {"emote": "emoji-flex", "delay": 3},
        "gagging": {"emote": "emoji-gagging", "delay": 6},
        "tiktok8": {"emote": "dance-tiktok8", "delay": 11},
        "kpop": {"emote": "dance-blackpink", "delay": 7},
        "pennywise": {"emote": "dance-pennywise", "delay": 1.5},
        "bow": {"emote": "emote-bow", "delay": 3.3},
        "curtsy": {"emote": "emote-curtsy", "delay": 2.8},
        "snowangel": {"emote": "emote-snowangel", "delay": 6.8},
        "energyball": {"emote": "emote-energyball", "delay": 8.3},
        "frog": {"emote": "emote-frog", "delay": 15},
        "cute": {"emote": "emote-cute", "delay": 7.3},
        "tiktok9": {"emote": "dance-tiktok9", "delay": 13},
        "shuffle": {"emote": "dance-tiktok10", "delay": 9},
        "pose7": {"emote": "emote-pose7", "delay": 5.3},
        "pose8": {"emote": "emote-pose8", "delay": 4.6},
        "casual": {"emote": "idle-dance-casual", "delay": 9.7},
        "pose1": {"emote": "emote-pose1", "delay": 3},
        "pose3": {"emote": "emote-pose3", "delay": 4.7},
        "pose5": {"emote": "emote-pose5", "delay": 5},
        "cutey": {"emote": "emote-cutey", "delay": 3.5},
        "model": {"emote": "emote-model", "delay": 6.3},
        "astro": {"emote": "emote-astronaut", "delay": 0},  # No delay specified, set to 0
        "guitar": {"emote": "emote-punkguitar", "delay": 10},
        "fashionista": {"emote": "emote-fashionista", "delay": 6},
        "uwu": {"emote": "idle-uwu", "delay": 25},
        "wrong": {"emote": "dance-wrong", "delay": 13},
        "sayso": {"emote": "idle-dance-tiktok4", "delay": 16},
        "maniac": {"emote": "emote-maniac", "delay": 5.5},
        "enthused": {"emote": "idle-enthusiastic", "delay": 16.5},
        "happy": {"emote": "emote-happy", "delay": 0},  # No delay specified, set to 0
        "timejump": {"emote": "emote-timejump", "delay": 0},  # No delay specified, set to 0
        "creepy": {"emote": "dance-creepypuppet", "delay": 10},
        "sleigh": {"emote": "emote-sleigh", "delay": 0},  # No delay specified, set to 0
        "singing": {"emote": "idle_singing", "delay": 11},
        "anime": {"emote": "dance-anime", "delay": 0},  # No delay specified, set to 0
        "hyped": {"emote": "emote-hyped", "delay": 0},  # No delay specified, set to 0
        "jinglebell": {"emote": "dance-jinglebell", "delay": 0},  # No delay specified, set to 0
        "snowball": {"emote": "emote-snowball", "delay": 6},
    }


    def _get_emote_commands_list(self):
        emotes_list = list(self.emote_dict.keys())
        unique_emotes = set(emotes_list)  
        formatted_list = ', '.join(unique_emotes)
        return f"You can use the following emotes: {formatted_list}. Just type the emote you want to use in the chat!"

  
    async def send_emote_continuously(self, emote_data: dict, user_id: int) -> None:
      try:
          while user_id in self.user_loops:
              await self.highrise.send_emote(emote_data["emote"], user_id)
              await asyncio.sleep(emote_data["delay"])
      except asyncio.CancelledError:
          pass
      except Exception as e:
          print(f"An error occurred in send_emote_continuously: {e}")
          self.user_loops.pop(user_id, None)

  
    async def on_user_move(self, user: User, pos: Position) -> None:
      """On a user moving in the room."""
      if user.username == "iced_yu":
          # Offset the x-coordinate to the right by, for example, 2 units
          adjusted_pos = Position(x=pos.x + 2, y=pos.y, z=pos.z, facing=pos.facing)
          await self.highrise.walk_to(adjusted_pos)
          print(adjusted_pos)


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
                    await self.highrise.chat(f"Emote loop for '{words[0]}' started by {user.username}.")
                elif not words[1:]:
                    # If no additional commands after the emote, send it once
                    room_users_res = await self.highrise.get_room_users()
                    for item in room_users_res.content:
                        room_user = item[0]
                        await self.highrise.send_emote(command["emote"], room_user.id)




      async def following_loop():
        while True:
            room_users = (await self.highrise.get_room_users()).content
            user_position = None  # Initialize with a default value
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    break

            if user_position is not None:  # Check if user_position is assigned
                print(user_position)
                if type(user_position) != AnchorPosition:
                    await self.highrise.walk_to(Position(user_position.x + 1, user_position.y, user_position.z))
            else:
                print(f"User {user.username} not found in the room")  # Handle the case where user is not found

            await asyncio.sleep(0.5)


      if self.following_task and not self.following_task.done():
          await self.highrise.chat("Already following someone")
          return

      self.following_task = self.highrise.tg.create_task(following_loop())
      await self.highrise.chat(f"Following {user.username}")

    async def stop_follow(self, user: User, message: str) -> None:
      if self.following_task and not self.following_task.done():
          self.following_task.cancel()
          await self.highrise.chat(f"Stopping following {user.username}")
      else:
          await self.highrise.chat("Not following anyone")

    


    async def on_chat(self, user: User, message: str) -> None:
      message = message.strip().lower()
      print(user.username + ": "+ message)

      if message == "/teleport" and user.username in vip:
        await self.highrise.teleport(user.id, self.user_teleport_position2)
      elif message == "/down" and user.username in vip:
        await self.highrise.teleport(user.id, self.user_teleport_position)
      elif message == "/vip" and user.username in vip:
        await self.highrise.teleport(user.id, self.user_teleport_position3)
      elif message.startswith("/follow"):
        await self.follow(user, message)
      elif message.startswith("/stop_follow"):
        await self.stop_follow(user, message)



      if message == "emotes":
        emotes_list = list(self.emote_dict.keys())
        chunk_size = 10  # This is an example, adjust the chunk size based on the game's limits
        chunks = [emotes_list[i:i + chunk_size] for i in range(0, len(emotes_list), chunk_size)]
        for chunk in chunks:
            emote_message = ', '.join(chunk)
            await self.highrise.chat(emote_message)
            await asyncio.sleep(1)


      elif message.lower() == "stop":
          # Handle stop command in a case-insensitive manner
          loop_data = self.user_loops.pop(user.id, None)
          if loop_data is not None:
              loop_data['loop'].cancel()

      elif message.lower().startswith("/dress") and user.username == "iced_yu":
       await self.highrise.set_outfit(outfit=[
          Item(type='clothing',
              amount=1,
              id='body-flesh',
              account_bound=False,
              active_palette=1),
          Item(type='clothing',
              amount=4,
              id='hair_front-n_basic2020overshoulderpony',
              account_bound=False,
              active_palette=4),
          Item(type='clothing',
              amount=4,
              id='eyebrow-n_basic2018newbrows16',
              account_bound=False,
              active_palette=4),
          Item(type='clothing',
              amount=1,
              id='mouth-basic2018unimpressed',
              account_bound=False,
              active_palette=1),
          Item(
              type='clothing',
              amount=1,
              id='nose-n_room22019nosestud',
          ),
          Item(type='clothing',
              amount=1,
              id='shirt-n_philippineday2019filipinotop',
              account_bound=False,
              active_palette=-1),
          Item(type='clothing',
              amount=1,
              id='skirt-f_gianttutu',
              account_bound=False,
              active_palette=-1),
          Item(type='clothing',
              amount=1,
              id='shoes-n_starteritems2019flatswhite',
              account_bound=False,
              active_palette=-1),
          Item(type='clothing',
              amount=1,
              id='eye-n_basic2018malediamondsleepy',
              account_bound=False,
              active_palette=1),
          Item(type='clothing',
              amount=3,
              id='freckle-n_basic2018freckle35',
              account_bound=False,
              active_palette=3),
          Item(type='clothing',
              amount=3,
              id='blush-f_blush01',
              account_bound=False,
              active_palette=3),
          Item(type='clothing',
              amount=4,
              id='hair_back-n_basic2020overshoulderpony',
              account_bound=False,
              active_palette=4),
      ])
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
                  loop_task = asyncio.create_task(self.send_emote_continuously(command, user.id))
                  self.user_loops[user.id] = {
                      'command': command,
                      'loop': loop_task
                  }
              else:
                  # Send the emote only once if the message contains only the emote name
                  await self.highrise.send_emote(command, user.id)

logging.basicConfig(filename='bot.log', level=logging.DEBUG)


app = Flask(__name__)

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    bot_file_name = "main"
    bot_class_name = "Bot"
    room_id = "65a8236a0aa6b497a9b328a8"
    bot_token = "480d69a2bc2440c9df71f24e59c6ad2e22490730511f3cc32cd0627e2bd56bbd"

    my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

    while True:
        try:
            definitions = [my_bot]
            arun(main(definitions))
        except Exception as e:
            logging.error(f"An exception occurred in the main loop: {e}")
            time.sleep(2)


  
