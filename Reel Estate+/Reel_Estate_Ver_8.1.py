#gambling game!!
import json
import random 
import os

def clear_console():
    os.system('cls')
    


def save_game(game_state):  
    try:
        with open("save_file.json", "w") as f:
            json.dump(game_state, f)
        print(random.choice(["Saved", "Done", "Saved to Json File", "Json File Eaten"]))
    except Exception as e:
        print(f"Error saving game: {e}")
     


def load_game():
   
    try:
        with open("save_file.json", "r") as f:
             game_state = json.load(f)
        print("Game loaded suucessfully")
        return game_state
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
    except json.JSONDecodeError:
        print("Save file is corrupted. Starting a new game.")
 
    return None
#==========================================================================================================================================

#invnentory set up 
game_state = {
    "name" : "",
    "money" : "",
    "currency" : 200,
    "debug" : False,
    "tik" : 0,
    "fish" : 0,
    "fishnt": 0,
    "no" : 0,
    "G" : 0,
    "L" : 0 , 
    "fishy": False,
    "rigg": False,
    
    "Map" : False,    
    "Lore" : False,   
    "jackpot" : False,
    "jackpot2" : False, 
    
    "houses": {
        "box" : False,
        "big_box" : False,
        "backyard" : False,
        "small_house" : False,
        "house" : False,
        "kasino": False,
    },
    
    "rods": {
        "basic" : False, 
        "better" : False,
        "bh" : False,
        "bh_deluxe" : False,
        "bh_super" : False,
    },
    
    "bought": {
        "box" : False,
        "big_box" : False,
        "backyard" : False,
        "small_house" : False,
        "house" : False,
        "kasino": False,
        "map" : False,
        "basic" : False,
        "better" : False,
        "bh" : False,
        "bh_deluxe" : False,
        "bh_super" : False,
    },
    
    
    
    "achievements": {
        "U1" : False,
        "U2" : False,
        "U3" : False,
        "U4" : False,
        "U5" : False,
        "U6" : False,
        "U7" : False,
        "U8" : False,
        "U9" : False,
        "U10" : False,
        "U11" : False,
        "U12" : False,
        "U13" : False,
        "U14" : False,
        "U15" : False,
        "U16" : False,
        
    },
    
    "lore": {
        "intro": False,
        "ocean_path": False,
        "beach_house_orgin": False,
        "Kasino_owner": False,
    },
    "collectables" : {
        "slot_col": False,
        "roul_col": False,
        "lake_col": False,
        "ocean_col": False,
        "house_col_1": False,
        "house_col_2": False,
        "house_col_3": False,
    },
    "npcs": {
        "gambler": False,
        "fisher": False,
        "achiev": False,
    }
     
}
#==========================================================================================================================================
def create_new_game():
    game_state = {
        "name": "",
        "currency": 200,
        "money": "",
        "debug": False,
        "fish": 0,
        "fishnt": 0,
        "G": 0,
        "L": 0,
        "tik": 0,
        "no": 0,
        "Map": False,
        "Lore": False,
        "jackpot": False,
        "jackpot2": False,
        "rigg": False,
        "win" : 0,
        
        "houses": {
            "box": False,
            "big_box": False,
            "backyard": False,
            "small_house": False,
            "house": False,
            "kasino": False,
        },
        "rods": {
            "basic": False,
            "better": False,
            "bh": False,
            "bh_deluxe": False,
            "bh_super": False,
        },
        "bought": {
            "box": False,
            "big_box": False,
            "backyard": False,
            "small_house": False,
            "house": False,
            "kasino": False,
            "map": False,
            "basic": False,
            "better": False,
            "bh": False,
            "bh_deluxe": False,
            "bh_super": False,
        },
        "achievements": {
            "U1": False,
            "U2": False,
            "U3": False,
            "U4": False,
            "U5": False,
            "U6": False,
            "U7": False,
            "U8": False,
            "U9": False,
            "U10": False,
            "U11": False,
            "U12": False,
            "U13": False,
            "U14": False,
            "U15": False,
            "U16": False,
        },
        "misc": {
            "Map": False,
            "beach_unlocked": False
        },
        
        "lore": {
            "intro": False,
            "ocean_path": False,
            "beach_house_orgin": False,
            "Kasino_owner": False,  
        },
        "collectables" : {
        "slot_col": False,
        "roul_col": False,
        "lake_col": False,
        "ocean_col": False,
        "house_col_1": False,
        "house_col_2": False,
        "house_col_3": False,
        },
        "npcs": {
        "gambler": False,
        "fisher": False,
        "achiev": False,
        }
    }
    return game_state
#Dev commands==============================================================================================================================
commands_id = {
    "00": {"def": "sets currency to asked amount"},
    "01": {"def": "gives every lore entry"},
    "02": {"def": "changes currency name"},
    "03": {"def": "gives asked fish amount"},
    "04": {"def": "gives what ever item, with out charged."},
    "05": {"def": "a back door to all places on the map"},
    "06": {"def": "a toggle for rigged gambling"},
    "07": {"def": "a toggle for all achievements"},
}
#collectables=============================================================================================================================
Collectables = {
    "slot_col": {"rank": "Common", "desc": "a lever found on a slots machine.", "trigger": "slots"},
    "roul_col": {"rank": "Common", "desc": "A Ball found Roulette Wheel", "trigger": "roulette"},
    "lake_col": {"rank": "Uncommon", "desc": "a silver fishing hook", "trigger": "lake"},
    "ocean_col": {"rank": "Rare", "desc": "a large gold fish scale", "trigger": "ocean"},
    "house_col_1": {"rank": "Uncommon", "desc": "A nice rug for Your house", "trigger": "ran_house_1"},
    "house_col_2": {"rank": "Legendary", "desc": "A Fancy Toilet.", "trigger": "ran_house_2"},
    "house_col_3": {"rank": "Rare", "desc": "A Prestine Beach House(bh) Replica", "trigger": "ran_house_3"},
}
#lore======================================================================================================================================
Lore_entry = {
    "intro": {
        "title": "Reel Estate The Town",
        "text": (
            "Welcome To Jahabler, a small town in California."
            "its quite small, started out as a simple casino, the town was built around it, untill..."
        )
    },
    "ocean_path": {
        "title": "The Path To The Ocean",
        "text": (
            "1 fish, 2 fish, red fish, blue fish. 100 fish reveals the truth. quite fishy."
        )
    },
    "beach_house_orgin": {
        "title": "The owner of Beach House",
        "text": (
            "Beach House is a brand only found in Jahabler. no one knows who runs the store, or who keeps it stocked "
            "and cleaned, but it stays that way"
        )
    },
    "Kasino_owner": {
        "title": "The Owner of Kasino",
        "text": (
            "The Owner of Kondike's kasino, Kondike himself. no one has seen him, not after he disapeared into his creation."
            "The Kasino is run by The Ghosts supposedly, Who dont care about your age, just money. Rumors are Kondike is god "
            "himself, no good proof though"
        )
    }
}   
#shop pt.1=================================================================================================================================
shop_items = {
    "houses":{
        "Box": {"price": 50, "id": "box"},
        "Big Box": {"price": 150, "id": "big_box"},
        "Backyard": {"price": 350, "id": "backyard"},
         "Small House": {"price": 700, "id": "small_house"},  
         "House": {"price": 1500, "id": "house"},
         "Kasino": {"price": 5000, "id": "kasino"},
    },
    "rods": {
        "Basic Rod": {"price": 175, "id": "basic"},
        "Better Rod": {"price": 400, "id": "better"},
    },
    "misc": {
        "Map": {"price": 500, "id": "map"},
    },
    "bh_rods": {
        "bh rod": {"price": 700, "id": "bh"},
        "bh deluxe rod": {"price": 1500, "id": "bh_deluxe"},
        "bh super rod": {"price": 3000, "id": "bh_super"},
    }
}
#fishing set up============================================================================================================================
rod_data = {
    "basic": {"location": "lake", "chance": 0.5, "payout": (5, 15)},
    "better": {"location": "lake", "chance": 0.65, "payout": (25, 50)},
    "bh": {"location": "ocean", "chance": 0.6, "payout": (500, 570)},
    "bh_deluxe": {"location": "ocean", "chance": 0.7, "payout": (650, 750)},
    "bh_super": {"location": "ocean", "chance": 0.75, "payout": (850, 1000)},
}
#achievments===============================================================================================================================
Achievements = {
    "U1": {"desc": "Huh?[Buy The Box]", "trigger": "Shop"},
    "U2": {"desc": "Prime Reel Estate[Buy the Final House]", "trigger": "Shop"},
    "U3": {"desc": "Do You Click Them?[Name Currency Cookies]", "trigger": "money"},
    "U4": {"desc": "Found The Secret Path[To The Beach]", "trigger": "Beach_unlock"},
    "U5": {"desc": "Where My Fish At?[Fail To Catch 100 Fish]", "trigger": "fishnt"},
    "U6": {"desc": "Lucky[Win 5 Times In a Row!]", "trigger": "streak_5_win"},
    "U7": {"desc": "Rigged The System[Win 10 Times In a Row!]", "trigger": "streak_10_win"},
    "U8": {"desc": "RIGGED[Lose 5 Times]", "trigger": "streak_5_lose"},
    "U9": {"desc": "Rage Quit[Lose 10 Times]", "trigger": "streak_10_lose"},
    "U10": {"desc": "GAME THEORY[Get The Lore]", "trigger": "sans_is_ness"},
    "U11": {"desc": "Super Fisher[Get The Super Fishin Rod]", "trigger": "Shop"},
    "U12": {"desc": "Finders keepers[Find a Collectable]", "trigger": "finders"},
    "U13": {"desc": " They Are Everywhere[Find Every Collectable]", "trigger": "finders"},
    "U14" : {"desc": "Liar[Do the Gambler's Quest]", "trigger": "gambler"},
    "U15": {"desc": "Fisherman[Do the Fisher's Quest]", "trigger": "fisher"},
    "U16": {"desc": "Achievment Hunter[Do the Achievment's Quest]", "trigger": "achiev"},
}
#credits===================================================================================================================================
def credits():
    print("SnowMan Games Presents \fReel Estate")
    print("Lead, and Only programmer: Kondike_barr")
    print("Special Thanks to: FryinnPan, No2no, AvoidingCord, TurtleFoood, and My parents.")
    print("Thanks for playing Reel Estate.")
    input("press enter to leave")
    exit()
#==========================================================================================================================================
def count_cols(game_state):
    return sum(1 for v in game_state["collectables"].values() if v)
#npc functions=============================================================================================================================
def npc_gambler(game_state):
    print("hello there, i am a friend of kondikes, and was hoping you could check up on the kasino?")
    print("win 5 times in the Kasino.")
    print(f"win count: {game_state['win']}")
    if game_state["win"] >= 5:
        print("good, the ghosts havent rigged it, that means i have a chance to get a jack- i mean report to kondike...")
        game_state["currency"] += 500
        game_state["npcs"]["gambler"] = True    
    else:
        print("come on, i need this, so i can know if its possi- i mean so i can report to kondike")
        
def npc_fisher(game_state):
    print("Sup Mate. I heard you have a rod, and was hoping you could help me out?")
    print("find the golden fish scale!")
    if game_state["collectables"]["ocean_col"]:
        print("You found it! thanks mate, here is a little something for your troubles")
        game_state["currency"] += 1000
        game_state["npcs"]["fisher"] = True
    else:
        print("im starting to think its not real.")

def npc_menu(game_state):
    print("hello there traveler, welcome to the town of jahabler. get some achievements, i will reward you.")
    print("get 3 achievements")
    if sum(1 for v in game_state["achievements"].values() if v) >= 3:
        print("You have done it! here is a little something for you")
        game_state["currency"] += 1500
        game_state["npcs"]["achiev"] = True
    else:
        print("you havent been here long enough for a reward.")
       
#collectable check :)======================================================================================================================
def collectable_check(game_state, context=None):
    c = game_state["collectables"]
    for key, data in Collectables.items():
        if c[key]:
            continue
        trigger = data["trigger"]
        
        if trigger == context:
            if trigger == "slots":
                if not game_state["collectables"].get("slot_col"):
                    continue
            if trigger == "roulette":
                if not game_state["collectables"].get("roul_col"):
                    continue
            if trigger == "lake":
                if not game_state["collectables"].get("lake_col"):
                    continue
            if trigger == "ocean":
                if not game_state["collectables"].get("ocean_col"):
                    continue
            if trigger == "ran_house_1":
                if not game_state["collectables"].get("house_col_1"):
                    continue
            if trigger == "ran_house_2":
                if not game_state["collectables"].get("house_col_2"):
                    continue
            if trigger == "ran_house_3":
                if not game_state["collectables"].get("house_col_3"):
                    continue
                
            c[key] = True
            print(f"\nCollectable Found: {data['desc']} ({data['rank']}) ")
#==========================================================================================================================================
def achievment_check(game_state, context=None):
    a = game_state["achievements"]
    for key, data in Achievements.items():
        if a[key]:
            continue
        trigger = data["trigger"]

        # Only unlock if the trigger matches AND the condition is met
        if trigger == context:
            # Special checks for achievements that need extra conditions
            if trigger == "Beach_unlock":
                if not game_state["misc"].get("beach_unlocked"):
                    continue  # Don't unlock unless the beach is actually unlocked
            if trigger == "money":
                if game_state.get("money", "").lower() != "cookie":
                    continue
            if trigger == "fishnt":
                if game_state.get("fishnt", 0) < 100:
                    continue
            if trigger == "streak_5_win":
                if game_state.get("G", 0) < 5:
                    continue
            if trigger == "streak_10_win":
                if game_state.get("G", 0) < 10:
                    continue
            if trigger == "streak_5_lose":
                if game_state.get("L", 0) < 5:
                    continue
            if trigger == "streak_10_lose":
                if game_state.get("L", 0) < 10:
                    continue
            if trigger == "sans_is_ness":
                if not game_state.get("Lore"):
                    continue
            if trigger == "Shop":
                # U1: Buy the box
                if key == "U1" and not game_state["bought"].get("box"):
                    continue
                # U2: Buy the final house
                if key == "U2" and not game_state["bought"].get("house"):
                    continue
                # U11: Buy the super rod
                if key == "U11" and not game_state["bought"].get("bh_super"):
                    continue
            if trigger == "finders":
                if key == "U12" and count_cols(game_state) < 1:
                    continue
                if key == "U13" and count_cols(game_state) < len(game_state["collectables"]):
                    continue
            if trigger == "gambler":
                if not game_state["npcs"].get("gambler"):
                    continue
            if trigger == "fisher":
                if not game_state["npcs"].get("fisher"):
                    continue
            if trigger == "achiev":
                if not game_state["npcs"].get("achiev"):
                    continue
                
            # If all conditions are met, unlock achievement
            a[key] = True
            
            print(f"\n Achievment Unlocked: {data['desc']}")
        if key == "U6" or key == "U8":
            game_state["lore"]["Kasino_owner"] = True
#inventory=================================================================================================================================
def show_inventory(game_state):
    print(f"{game_state['name']}'s Status:")
    
    #player info
    print(f"Name: {game_state['name']}")
    print(f"Currency: {game_state['currency']} {game_state['money']}")
    print(f"Fish Caught: {game_state['fish']}")
    print(f"fishnt caught[Failed catches]: {game_state['fishnt']}")
    print(f"{game_state['name']}'s inventory")
    print("\nall rods owned:")
    any_rods = False
    for rod_id, owned in game_state["rods"].items():
        if owned:
            print(f" - {rod_id.replace('_', ' ').title()}")
            any_rods = True
    if not any_rods:
        print(" - None. you should buy some, its the best way to make money.")
    
    print("\n Houses Owned(Real Estate owner are you?):")
    any_houses = False
    for house_id, owned in game_state["houses"].items():
        if owned:
            print(f" - {house_id.replace('_', ' ').title()}")
            any_houses = True
    if not any_houses:
        print("You are activly homeless, go buy a house buddy")
        
    print("\nAchievments[:D]:")
    unlocked = [Achievements[k]["desc"] for k, v in game_state["achievements"].items() if v]
    if unlocked:
        for a in unlocked:
            print(f" - {a}")
    else:
        print("You should do something interesting to get achievements")
    print("Collectables Found: ")
    any_cols = [(Collectables[k]['rank'], Collectables[k]['desc']) for k, v in game_state["collectables"].items() if v]
    if any_cols:
        for rank, desc in any_cols:
            print(f"- {rank}: {desc}")
    if not any_cols:
        print("No Collectables found. Try searching for them")
    print("DEBUG: ",game_state["collectables"])
    input(" ")
#roulette==================================================================================================================================
def play_roulette(game_state):
    
    while True:
        clear_console()
        print(f"Welcome to the roulette corner. you have {game_state['currency']} {game_state['money']}")
        print("Bet on Red(1), Black(2) Blue(3) or just leave(4)")
        color = input("your pick: ").strip()
        
        if color == "4":
            print("Leaving the Roulette corner")
            break
        if color not in ["1", "2", "3", "4"]:
            print("Plz pick a Choice :(")
        
        try:
            bet = int(input(f"place your bet in {game_state['money']}: "))
        except ValueError:
            print("invalid bet.")
            continue
        if bet <= 0 or bet > game_state["currency"]:
            print("lmao, nice try. denied >:(")     
            continue
        if random.randint(1, 20) == 1 or game_state["rigg"]:
            print("JACKPOT!!! ALL PAYOUTS ARE DOUBLED!!")
            game_state["jackpot"] = True
        else:
            game_state["jackpot"] = False
            
        outcome = random.randint(1,5) if not game_state["rigg"] else 3
        
        win = False
        if color == "1" and outcome in [1, 2, 3]:
            win = True
            color = "red"
        elif color == "2" and outcome in [1, 2, 3]:
            win = True
            color = "black"
        elif color =="3" and outcome == 3:
            win = True
            color = "blue"
            
        if win:
            print(f"YOU WIN, IT LANDED ON {color}!!")
            payout = bet * 2 if color != "3" else bet * 3
            if game_state["jackpot"]:
                payout *= 2
            game_state["currency"] += payout
            game_state["G"] += 1
            game_state["win"] += 1
            game_state["L"] = 0
            achievment_check(game_state, "streak_5_win")
            achievment_check(game_state, "streak_10_win")
            achievment_check(game_state, "streak_5_lose")
            achievment_check(game_state, "streak_10_lose")
            save_game(game_state)
            input("")
            continue
        else:
            print("welp, better try again right? you didnt win.")
            game_state["currency"] -= bet
            game_state["G"] = 0
            game_state["L"] += 1
            achievment_check(game_state, "streak_5_win")
            achievment_check(game_state, "streak_10_win")
            achievment_check(game_state, "streak_5_lose")
            achievment_check(game_state, "streak_10_lose")
            input("")
            if not game_state["collectables"]["roul_col"]:
                if random.random() < 0.1:
                    print("a ball underneath the table rolls out, yours for the taking...")
                    game_state["collectables"]["roul_col"] = True
            continue
            
#slots!!===================================================================================================================================
def play_slots(game_state):
    while True:
        
        print(f"\nYou have {game_state['currency']} {game_state['money']}")
        leave = input("Type 1 to leave, or anything else to spin: ").strip()
        if leave == "1":
            print("leaving the Slots Corner...")
            break
        
        try:
            bet = int(input("How much you betting? "))
        except ValueError:
            print("ERR: Invalid Bet")
            continue
        
        if bet <= 0 or bet > game_state["currency"] or bet >= 500:
            clear_console()
            print("Invalid Amount")
            continue
        
        if random.randint(1, 20) == 1 or game_state["rigg"]:
            print("JACKPOT!!! ALL PAYOUTS DOUBLED(...not really though?)!!")
            game_state["jackpot2"] = True
        else:
            game_state["jackpot2"] = False
            
        print(random.choice(["loading...", "please wait...", "ERR", "spining gears...", "huh?"]))
        input("press enter to see the results")
        
        slot1 = random.randint(1, 5)
        slot2 = random.randint(1, 5)
        slot3 = random.randint(1, 5)
        
        if game_state["rigg"]:
            slot1 = slot2 = slot3 = 5
            
        print(f"The Slots rolled: {slot1}|{slot2}|{slot3}")    
        save_game(game_state)
        if slot1 == slot2 == slot3:
            payout = bet * 4 if game_state["jackpot2"] else bet * 3
            print("EZ WIN, ABSOULTE 3/3 MATCHUP!!")
            game_state["currency"] += payout
            game_state["G"] += 1
            game_state["win"] += 1
            game_state["L"] = 0
            achievment_check(game_state, "streak_5_win")
            achievment_check(game_state, "streak_10_win")
            achievment_check(game_state, "streak_5_lose")
            achievment_check(game_state, "streak_10_lose")
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            payout = bet * 3 if game_state["jackpot2"] else bet * 2
            print("ez win, a 2/3 on that roll!")
            game_state["currency"] += payout
            game_state["G"] += 1
            game_state["win"] += 1
            game_state["L"] = 0
            achievment_check(game_state, "streak_5_win")
            achievment_check(game_state, "streak_10_win")
            achievment_check(game_state, "streak_5_lose")
            achievment_check(game_state, "streak_10_lose")
        else:
            print("shame this was a bad roll, always again right?")
            game_state["currency"] -= bet
            game_state["G"] = 0
            game_state["L"] += 1
            achievment_check(game_state, "streak_5_win")
            achievment_check(game_state, "streak_10_win")
            achievment_check(game_state, "streak_5_lose")
            achievment_check(game_state, "streak_10_lose")
        input(" ")
        if not game_state["collectables"]["slot_col"]:
            if random.random() < 0.1:
                print("as the reels stop, the lever for the slot machine falls of...")
                game_state["collectables"]["slot_col"] = True
#kasino back room==========================================================================================================================
def back_room(game_state):
    clear_console()
    print("you enter the back room. it is a mess. the lights filcker as ghosts run amuck, causing chaos. then you see him, a snowman, kondike"
          "himself, dissapear in the ever streching back room.")
    input("press enter to continue")
    credits()
    
#kasino====================================================================================================================================            
def open_kasino(game_state):
       while True:
           print("you are in Kondike's Kasino, smells of new cards, and horrible life choices. go to...?")
           print("1. Roulette corner")
           print("2. Slots")
           print("3. Leave")
           if game_state["houses"].get("kasino"):
               print("4. A back door in the back is open")
               
               
                               
           choice = input("What to do?...").strip()      
           if choice == "1":
               play_roulette(game_state)
           elif choice == "2":
               play_slots(game_state) 
           elif choice == "3":
               print("you walk out of the kasino into the fresh air, maybe richer, but probably not.")
               break
           elif choice == "4" and game_state["houses"].get("kasino"):
               back_room(game_state)
           
                   
           else:
               print("Invalid option")
               continue
#shop menu=================================================================================================================================
def shop_menu(game_state, items, category, sale_multi=1.0):
    clear_console()
    display_items = dict(items)
    if category == "houses" and not all(game_state["npcs"].values()):
        display_items = {k: v for k, v in items.items() if k != "kasino"}
    while True:
        print(f" {category.title()} isle")
        for idx, (item_name, data) in enumerate(display_items.items(), start=1):
            item_id = data["id"]
            price = data["price"]
            bought = game_state["bought"].get(item_id, False)
            status = "BOUGHT" if bought else f"${price} {game_state['money']}"
            print(f"{idx}. {item_name} - {status}")
        print(f"{len(display_items)+1}. Leave")
        
        choice = input("Select an item: ").strip()
        if not choice.isdigit():
            print("Sorry, no can do bud")
            continue
        
        choice = int(choice)
        if choice == len(display_items) + 1:
            print("leaving this isle")
            break
        elif 1 <= choice <= len(display_items):
            item_name = list(display_items.keys())[choice - 1]
            item_data = display_items[item_name]
            item_id = item_data["id"]
            item_price = int(item_data["price"] * sale_multi)
            
            if game_state["bought"].get(item_id, False):
                print("there is nothing to buy, it's out of stock.")
                continue
            
            if game_state["currency"] < item_price:
                print(f"You are {item_price - game_state['currency']} short, maybe come back when your a little, m m m m m m m, richer.")
                continue
            
            game_state["currency"] -= item_price
            game_state["bought"][item_id] = True
            save_game(game_state)
            
            
            if category == "houses":
                game_state["houses"][item_id] = True
            elif category == "rods":
                game_state["rods"][item_id]= True
                if item_id == "bh":
                    game_state["lore"]["beach_house_orgin"] = True
            elif category == "misc" and item_id == "map":
                game_state["Map"] = True
                
            print(f"you bought {item_name} for {item_price}!")
            achievment_check(game_state, "Shop")
            if not (game_state["collectables"]["house_col_1"] and
                    game_state["collectables"]["house_col_2"] and
                    game_state["collectables"]["house_col_3"]):
                House = random.randint(1,3)
                if random.random() < 0.1:
                    print("you notice a forgotten item in the shop")
                    if House == 1 and not game_state["collectables"]["house_col_1"]:
                        game_state["collectables"]["house_col_1"] = True
                    if House == 2 and not game_state["collectables"]["house_col_2"]:
                        game_state["collectables"]["house_col_2"] = True
                    if House == 3 and not game_state["collectables"]["house_col_3"]:
                        game_state["collectables"]["house_col_3"] = True
        else:
            print("Not a thing you can buy")
            
    
    achievment_check(game_state, "Shop")
#Shop======================================================================================================================================
def main_shop(game_state):
    sale_status = random.randint(1, 100) == 1
    sale_multi = 0.5 if sale_status else 1.0
    while True:
        print(f"\n ah,{game_state['name']}, Welcome to Spamminton's store.")#spammington is based off of spamo
        print("there are many isles here, what are you looking for?")
        print("1. Houses")
        print("2. Fishing Rods")
        print("3. Junk")
        print("4. Leave Spammington's")
        if not game_state["npcs"]["gambler"]:
            print("5. Talk to the Gambler")
        if not game_state["npcs"]["fisher"]:
            print("6. Talk to the Fisher")
        choice = input("> ").strip()
        if choice == "1":
            shop_menu(game_state, shop_items["houses"], "houses", sale_multi)
        elif choice == "2":
            shop_menu(game_state, shop_items["rods"], "rods", sale_multi)
        elif choice == "3":
            shop_menu(game_state, shop_items["misc"], "misc", sale_multi)
        elif choice == "4":
            print("you have exited spammington's. the air outside is nice.", sale_multi)
            break
        elif choice == "5" and not game_state["npcs"]["gambler"]:
            npc_gambler(game_state) 
        elif choice == "6" and not game_state["npcs"]["fisher"]:
            npc_fisher(game_state)
        else:
            print("Invalid Option.")
#fish======================================================================================================================================
def fish(game_state, rod_id):
    rod = rod_data[rod_id]
    location = rod["location"]
    chance = rod["chance"]
    payout_range = rod["payout"]
    
    print(f"\n You are fishing at the local {location}. rod: {rod_id.replace('_', ' ')}")
    while True:
        choice = input("Fish(1), or Leave(2): ").strip()
        if choice == "2":
            print(f"you stopped, and left {location}. ")
            break
        elif choice != "1":
            print("what are you trying to do, drown?")
            continue
        
        if random.random() < chance or game_state["debug"]:
            print("You caught a fish!")
            game_state["fish"] += 1
            sell = input("sell the fish? (y/n): ").strip().lower()
            if sell == "y":
                clear_console()
                payout = random.randint(*payout_range)
                game_state["currency"] += payout
                print(f"You earned {payout} {game_state['money']}")
                
        else:
            clear_console()
            print("No catch...")
            game_state["fishnt"] += 1
            achievment_check(game_state, "fishnt")
            if location == "lake" and not game_state["collectables"]["lake_col"]:
                if random.random() < 0.1:
                    print("You found a silver fishing hook in the mud!")
                    game_state["collectables"]["lake_col"] = True
            if location == "ocean" and not game_state["collectables"]["ocean_col"]:
                if random.random() < 0.1:
                    print("You found a large gold fish scale in the sand!")
                    game_state["collectables"]["ocean_col"] = True
    
            
#lake======================================================================================================================================
def go_fishing(game_state):
    clear_console()
    print("\n You arrive at the lake, the air smells of fish and mud.")
    has_rod = False
  
    
    for rod_id in ["better","basic"]:
        if game_state["rods"].get(rod_id):
            fish(game_state, rod_id)
            has_rod = True 
            break
    if not has_rod:
        print("you dont have a rod for the lake")
            
#beach_shop================================================================================================================================
def beach_shop(game_state):
    shop_menu(game_state, shop_items["bh_rods"], "rods")
#ocean=====================================================================================================================================
def ocean_area(game_state):
    while True:
        print("\n You arrive at the beach. its nice, lots of water, and clouds")
        print("1. fish")
        print("2, shop")
        print("3. leave")
    
        choice = input("> ").strip()
        if choice == "1":
            for rod_id in ["bh_super", "bh_deluxe", "bh"]:
                if game_state["rods"].get(rod_id):
                    fish(game_state, rod_id)
                    break
            else:
                print("You dont have a good enough rod. peasant")
        elif choice == "2":
            beach_shop(game_state)
        elif choice == "3":
            break
#Lore check================================================================================================================================
def view_lore(game_state):
    while True:
        unlocked_lore = [key for key, unlocked in game_state["lore"].items() if unlocked]
    
        if not unlocked_lore:
            print("you have not found any lore, or secrets. try looking around")
            return
        print("\nLore Entries:")
        for idx, key in enumerate(unlocked_lore, start=1):
            title = Lore_entry[key]["title"]
            print(f"{idx}. {title}")
        print(f"{len(unlocked_lore)+1}. leave")
    
        choice = input("select an entry: ").strip()
        if not choice.isdigit():
            print("Invalid entry")
            return
        choice = int(choice)
        if choice == len(unlocked_lore) + 1:
            return
        elif 1 <= choice <= len(unlocked_lore):
            selected_key = unlocked_lore[choice - 1]
            entry = Lore_entry[selected_key]
            print(f"\n{entry['title']}\n{'-' * len(entry['title'])}\n{entry['text']}\n")
        else:
            print("No")
#save, quit, and debug stuff===============================================================================================================
def save_or_quit(game_state):
    while True:
        print("Save(1), or Quit(2): ")
        answer = input("> ").strip()
        
        if answer == "1":
            save_game(game_state)
            break
        elif answer == "2":
            print('a bye bye!')
            exit()
        elif answer == ":)":
            clear_console()
            if game_state["debug"]:
                print("Dev/debug command console: ")
                for cmd, info in commands_id.items():
                    print(f"{cmd}: {info['def']}" )
                com_id = input("> ").strip()
                if com_id == "00":
                    cheat_amount = input("what amount: ").strip()
                    if not cheat_amount.isdigit():
                        print("nah")
                        return
                    else:
                        game_state["currency"] = int(cheat_amount)
                        print(f"currency set to {game_state['currency']}")
                if com_id == "01":
                    for lore_key in game_state["lore"]:
                        game_state["lore"][lore_key] = True
                    print("All lore entries summoned")
                if com_id == "02":
                    new_name = input("new name here: > ").strip()
                    game_state["money"] = new_name
                    achievment_check(game_state, "money")
                    print(f"currency name updated: {game_state['money']}")
                if com_id == "03":
                    try:
                        amount = int(input("summon fish; how much: > "))
                        game_state["fish"] += amount
                        print(f"fish caught: {amount} just now. fish owned: {game_state['fish']}")
                    except ValueError:
                        print("ERR: not an amount. please input amount")
                if com_id == "04":
                    print("which item do you want? please input the name. this is case sensitive")
                    print("houses: ")
                    for house in game_state["houses"]:
                        print(f" {house}")
                    print("=" * 10)
                    print("rods: ")
                    for rod in game_state["rods"]:
                        print(f" {rod}")
                    print("=" * 10)
                    print("misc: ")
                    for misc in game_state["misc"]:
                        print(f" {misc}")
                    hak_item = input("> ").strip().lower()
                    
                    rod_even = {
                        "basic_rod": "basic",
                        "better_rod": "better",
                        "bh": "bh",
                        "bh_deluxe": "bh_deluxe",
                        "bh_super": "bh_super",
                    }
                    if hak_item in rod_even:
                        rod_key = rod_even[hak_item]
                    elif hak_item in game_state["rods"]:
                        rod_key = hak_item
                    else:
                        rod_key = None
                    
                    if rod_key and rod_key in game_state["rods"]:
                        game_state["rods"][rod_key] = True
                        game_state["bought"][rod_key] = True
                        if rod_key + "_rod" in game_state["bought"]:
                            game_state["bought"][rod_key + "_rod"] = True
                        print("Rod added to Inventory")
                    elif hak_item in game_state["houses"]:
                        game_state["houses"][hak_item] = True
                        game_state["bought"][hak_item] = True
                        print("House added to inventory!")
                    # Misc
                    elif hak_item in game_state["misc"]:
                        game_state["misc"][hak_item] = True
                        game_state["bought"][hak_item] = True
                        print("Misc item added to inventory!")        
                        
                    else:
                        print("ERR: Invalid Item_ID")
                if com_id == "05":
                    print("backdoor access: active. backdoors[kasino|shop|lake|ocean]")
                    back_door = input("> ").strip().lower()
                    if back_door == "kasino":
                        open_kasino(game_state)
                    elif back_door == "shop":
                        main_shop(game_state)
                    elif back_door == "lake":
                        go_fishing(game_state)
                    elif back_door == "ocean":
                        ocean_area(game_state)
                    else:
                        print("ERR: Invalid BackDoor_ID")
                if com_id == "06":
                    game_state["rigg"] = not game_state.get('rigg', False)
                    print("Gambling is Roulette, and slots are Rigged.")
                if com_id == "07":
                    for key in game_state["achievements"]:
                        game_state["achievements"][key] = True
                    print("All Achievements set to True.")
            else:
                print(f"Name = {game_state['name']}; Debug False. Access Denied.")
                break
        else:
            print("sure bud.")
            break
#==========================================================================================================================================
def handle_choice(choice, game_state):
        game_state["tik"] += 1
        save_game(game_state)
        if game_state["tik"] == 10:
            game_state["currency"] += 10
            game_state["tik"] = 0
            
        if choice == "1":
            clear_console()
            save_game(game_state)
            game_state["tik"] += 1
            open_kasino(game_state)
            
            
        elif choice == "2":
            clear_console()
            save_game(game_state)
            game_state["tik"] += 1
            main_shop(game_state)
            
        elif choice == "3":
            clear_console()
            save_game(game_state)
            go_fishing(game_state)
            
        elif choice == "4":
            clear_console()
            save_game(game_state)
            view_lore(game_state)
            achievment_check(game_state, "sans_is_ness")
            
        elif choice == "5":
            clear_console()
            show_inventory(game_state)
            
        elif choice == "6" and game_state["Map"] and game_state["fish"] >= 50:
            clear_console()
            save_game(game_state)
            ocean_area(game_state)
            
        elif choice == "0":
            save_or_quit(game_state)
            clear_console()
        elif choice == "7" and not game_state["npcs"]["achiev"]:
            clear_console()
            save_game(game_state)
            game_state["tik"] += 1
            npc_menu(game_state)

def main_menu(game_state):
    clear_console()
    while True:
        if game_state["Map"]:
            print("\nThe map is shiny, brand new. Where do you wanna go?")
            print("1. Kasino")
            print("2. Shop")
            print("3. Fishing")
            print("4. Lore")
            print("5. Inventory")
            print("0. Save/Quit")
            if not game_state["misc"]["beach_unlocked"] and game_state["Map"] and game_state["fish"] >= 50:
                game_state["misc"]["beach_unlocked"] = True
                game_state["lore"]["ocean_path"] = True
                achievment_check(game_state, "Beach_unlock")
            if game_state["misc"]["beach_unlocked"]:
                print("6. Secret Ocean Path (Unlocked!)")
        else:
            print("many paths infront of you. 1, 2, 3, 4, 5, 6")
            print("0 to save/quit")
        if not game_state["npcs"]["achiev"]:
            print("7. Achievment NPC")
        if game_state["houses"].get("kasino"):
            print("The Kasino Is calling you. Something inside Wants YOU.")
        choice = input("Choose a location: ").strip()
        handle_choice(choice, game_state)
       
#==========================================================================================================================================
game_state = None
is_new_game = False

print("SnowMan Games Presnets:")
print("Reel Estate")
input("")
clear_console()
while True:
        print("Do You want to load a previous save? (y/n)")
        load = input(">").lower()
        if load == "y":
            game_state = load_game()
            if game_state is None:
                game_state = create_new_game()
                is_new_game = True
            else:
                is_new_game = False
            break
        elif load == "n":
            game_state = create_new_game()
            is_new_game = True
            break
        else:
            print("please choose y or n, or no game for u :)")

if is_new_game:
    clear_console()
    while True: 
        print("what type of money is it?")#cash, cash, cash, step on the cash. get it. like gas? im funny, trust.
        game_state["money"]=input("").lower()
    
        if 0 < len(game_state["money"]) <= 10:
            print("good job, you can create a good name for money, now move on")
            achievment_check(game_state, "money")
            input("press enter to continue")
            clear_console()
            break
        else:
            print("ew, bad name, try again.")
        
        
    while True:
        game_state["name"] = input("what is your name? ").strip().lower()
        if game_state["name"] == "cannoli":
            print("welcome god of cannolis, please enjoy ;)")
            input("press enter to continue")
            clear_console()
            break
        elif game_state["name"] == "no2no":
            print("y o u. i will allow you to pass, for the sake of kindness")
            input("press enter to continue")
            clear_console()
            break
        elif game_state["name"] == "fryinnpan":
            print("hello streamer.")
            input("press enter to continue")
            clear_console()
            break
        elif game_state["name"] == "spamo":
            print("ah, you, continue.")
            input("press enter to continue")
            clear_console()
            break
        elif game_state["name"] == "":
            print("no, bad name, try again")
            clear_console()
            continue
        elif game_state["name"] == "silas":
            print("too young, please do not come back.")#L silas
        elif game_state["name"] == "tester" or game_state["name"] == "kondike":#as said, i am god.
            game_state["debug"] = True
            print("Dev Mode Active, Console Access: True, key: ':)'")
            print(f"you start with {game_state['currency']}, {game_state['money']}")
            input("press enter to continue")
            clear_console()
            break
        else:
            input("press enter to continue")
            clear_console()
            break
         
    while True:
        print(f"Hello {game_state['name']} Welcome to the Town of Jahabler, know for our exculsive Casino, Kondike's Kasino. Let me give you a map.")
        #choices
        
        choice=input("y/n: ")
#actions of coices

        if choice == "y":
            input("you have map now, press Enter to continue")
            clear_console()
            game_state["Map"] = True
            game_state["lore"]["intro"] = True
            break
                
    
        elif choice == "n":
            print("what is wrong with you?? without the map you cant get around. let me try again")# funny response for map
            game_state["no"] = game_state["no"] + 1
            if game_state["no"] == 3:
                print("okay, fine, go buy the map yourself")
                game_state["lore"]["intro"] = True
                break

save_game(game_state)
main_menu(game_state)
   

                
          
        
  



        
                  
            