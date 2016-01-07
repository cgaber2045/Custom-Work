class splashes:
    splash = {
        
        'title' : """ 
  _   _           _                     _____                          
 | | | | ___  ___| |_ __ _  __ _  ___  | ____|___  ___ __ _ _ __   ___  
 | |_| |/ _ \/ __| __/ _` |/ _` |/ _ \ |  _| / __|/ __/ _` | '_ \ / _ \ 
 |  _  | (_) \__ \ || (_| | (_| |  __/ | |___\__ \ (_| (_| | |_) |  __/ 
 |_| |_|\___/|___/\__\__,_|\__, |\___| |_____|___/\___\__,_| .__/ \___| 
                           |___/                           |_|           """,

        'instructions' : """
At this time, there are no instructions.
We bid you the best of luck trying to play
the game on your own. Have fun!""",
        'game_start' : """--GAME START--""",
        'game_over' : """
    _________    __  _________   ____ _    ____________  __ 
   / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \/ / 
  / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ / / 
 / /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/_/  
 \____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_(_)   """,
        'goodbye' : """
     __   __   __   __   __       ___   / 
    / _` /  \ /  \ |  \ |__) \ / |__   / 
    \__| \__/ \__/ |__/ |__)  |  |___ .  

    """
    }
  

class rooms:
	room = {
    	'start' : {
        	"greeting" : """Welcome to...
  _    _   _____  
 | |  | | |  __ \                  -----|-----
 | |__| | | |__) |              *>=====[_]D  
 |  __  | |  _   /                    -'-`-           
 | |  | | | | \ \                       |
 |_|  |_| |_|  \_\                      | 
	
				Hostage Rescue!
							
You wake up in a small locked room. Everything feels hazy... you remember that you were pulled off the street one day and remember something about being taken hostage! You begin to panic but you remember that if you want to escape you must stay calm and alert. You find that you are tied up, but you can move your hands a little and look around.
""",
        	"option_text" : """Would you like to try to get the ropes off (A) or examine the room (B)?""",
        	"next" : ['A', 'B'],
        	"found_weapons" : ['Fist'],
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},
   	 
    	'graveyard' : {
        	"greeting" : """You were shot in the back by terrorists. Try again!""",
        	"option_text" : """ """,
        	"next" : [],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
        	# Note - usage of graveyard as room is depreceated
        	#   and will be removed soon in favor of a function
        	#   within the game engine itself.
    	},

    	'A' : {
        	"greeting" : """
While the terrorists hear you struggling, you are tortured and 
lose 15 HP. They leave, but accidently leave behind one of their AK-47's.
			""",
        	"option_text" : """Proceed to room B by typing B.""",
        	"next" : ['B'],
        	"found_weapons" : ['AK-47'],
        	"health" : -15,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'B' : {
        	"greeting" : """
You choose to examine the room and see a knife on the floor by your foot, which you use to cut the rope.
			""",
        	"option_text" : """Search for supplies (C) or search for an exit (D).""",
        	"next" : ['C', 'D'],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'C' : {
        	"greeting" : """
You are looking for supplies, but take too long and get caught. You have been shot in the back and died.
			""",
        	"option_text" : """ """,
        	"next" : ['D', 'E', 'F'],
        	"found_weapons" : None,
        	"health" : -100,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'D' : {
        	"greeting" : """
You have found a way through the air vent. You see a room, you wonder to yourself if you should you drop down or not.
			""",
        	"option_text" : """Choose to drop down here (E) or Continue Past and drop into the next room (F).""",
        	"next" : ['E', 'F'],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'E' : {
        	"greeting" : """
You drop down into the room and find an M4 with ammo in it. Suddenly you hear a noise.
			""",
        	"option_text" : """Press F to continue...""",
        	"next" : ['F'],
        	"found_weapons" : ['M4'],
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'F' : {
        	"greeting" : """
A Terrorist enters the room and you have no choice but to fight him.
			""",
        	"option_text" : """ """,
        	"next" : [],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : True,
        	"battle_props" : {
            	"on_defeat" : 'G',
            	"monster_name" : 'A Terrorist',
            	"monster_health" : 100,
                "monster_max_health" : 100,
            	"monster_weapon" : {
                	"name" : "AK-47",
                	"damage" : -25,
            	}
        	}
    	},
   	 
    	'G' : {
        	"greeting" : """
Good job defeating the terrorist, you have found a health pack which restores 50 health points!
			""",
        	"option_text" : """Go past the terrorist (H) or stay and try to look for other hostages (F)?""",
        	"next" : ['H', 'F'],
        	"found_weapons" : None,
        	"health" : +50,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'H' : {
        	"greeting" : """
You have walked past the terrorist. On the ground you pick up your USP.
			""",
        	"option_text" : """You can either go around trying to find more loot (F) or try to find an exit (I).""",
        	"next" : ['F', 'I'],
        	"found_weapons" : ['USP'],
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'I' : {
        	"greeting" : """
You find a grenade that you can use in your fight to get out. Too bad when you touch it it explodes and you are left wounded.
			""",
        	"option_text" : """If you don't die from the explosion, keep moving forward into the next room. (J)""",
        	"next" : ['J'],
        	"found_weapons" : None,
        	"health" : -20,
        	"battle" : False,
        	"battle_props" : None
    	},
   	 
    	'J' : {
        	"greeting" : """
You can see the exit! Just a little more... BOOM! A huge terrorist boss suited in juggernaut gear busts through the ceiling. There is no way around him, you must defeat him!
			""",
        	"option_text" : """ """,
        	"next" : [],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : True,
        	"battle_props" : {
            	"on_defeat" : 'K',
            	"monster_name" : 'Snake - The Head Terrorist',
            	"monster_health" : 150,
                "monster_max_health" : 150,
            	"monster_weapon" : {
                	"name" : "MachineGun",
                	"damage" : -10,
            	}
        	}
		},
		
		'K' : {
        	"greeting" : """
Congratulations! You have escaped from the facility where the terrorists were keeping you. You proceed to run into the forest. You have won! The only question left is... how will you survive? Time goes past and you are finally rescued by the U.S. Army's Hostage Recovery program. Things are finally working out in your favor.
			""",
        	"option_text" : """ """,
        	"next" : [],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None,
            "end_game" : True
    	},
		
	}

class arsenal:
	weapon = {
    	'AK-47' : {
        	"label" : "AK-47",
        	"damage" : -50,
        	"ammo" : 20,
        	"found" : False
    	},
   	 
    	'M4' : {
        	"label" : "M4",
        	"damage" : -40,
        	"ammo" : 15,
        	"found" : False
    	},
   	 
    	'USP' : {
        	"label" : "USP",
        	"damage" : -30,
        	"ammo" : 20,
        	"found" : False
    	},
		
    	'MachineGun' : {
        	"label" : "Machine Gun",
        	"damage" : -30,
        	"ammo" : 200,
        	"found" : False
    	},	
		
		'Fist' : {
        	"label" : "Your Fists of Fury",
        	"damage" : -20,
        	"ammo" : None,
        	"found" : False
    	},	
	}