import random
from bisect import bisect_left
import sys

#turn a string into a class with the same name (s/o to https://www.tutorialspoint.com/How-to-convert-a-string-to-a-Python-class-object)
def str_to_class(str):
    return getattr(sys.modules[__name__], str)
#given a number find the closest minimum value in a dictionary (s/o to https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value)
def take_closest(collection, num):
    return min(collection,key=lambda x:abs(x-num))
#General Classes
class Unit:
    def __init__(self, name, synerg):
        self.name = name
        self.synerg = synerg
class Synergies:
    syn = {}
    description = " "
    chr_list = []
    def __init__(self, name):
        self.name = name
        self.syn = {}
    #display a specific synergy
    def specfic_synergy(self, number):
        if number >= min(self.syn):     #if the number is valid
            spec = self.syn[take_closest(self.syn, number)]
            return (self.name + ": " + str(number) + " --> " + spec)
        else:                           #if a the synergy wouldn't happen (in game --> greyed out box)
            return(self.name + ": " + str(number) + " --> Not Enough Units ")

    def show_syn(self):                 #display synergy list (description and breakpoints)
        print(self.description)
        for k in sorted(self.syn.keys()):
            print(str(k) + ': ' + self.syn.get(k))

#Origins
class Celestial(Synergies):
    description = "All allies heal based on '%' of damage dealt"
    name = "Celestial"
    champ_w_trait = ["Xayah", "Rakan", "Xin_Zhao", "Ashe", "Lulu"]
    chr_list = []
    syn = {2: "15'%' of damage dealt", 4: "40'%' of damage dealt", 6:"99'%' of damage dealt"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Chrono(Synergies):
    description = "All allies gain 15% AS"
    name = "Chrono"
    chr_list = []
    champ_w_trait = ["Caitlyn", "Twisted_Fate", "Blitzcrank", "Shen", "Ezreal", "Wukong", "Riven", "Thresh"]
    syn = {2: "Every 8s", 4: "Every 3.5s", 6: "Every 1.5s", 8: "Every 0.75s"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Battlecast(Synergies):
    description = "BC units, upon dealing/ taking 10 instances of damage, heal if below 1/2 health, deal magic damage if above 1/2 health"
    name = "Battlecast"
    chr_list = []
    champ_w_trait = ["Nocturne", "Illaoi", "Kog'Maw", "Cassiopeia", "Viktor", "Urgot"]
    syn = {2: "80 health or damage", 4: "180 health or damage", 6:"480 health or damage", 8: "880 health or damage"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Star_Guardian(Synergies):
    description = "SG spellcasts grant mana to other SG (spread)"
    name = "Star Guardian"
    chr_list = []
    champ_w_trait = ["Poppy", "Zoe", "Ahri","Neeko", "Syndra", "Soraka", "Janna"]
    syn = {3: "25 Mana", 6: "40 Mana", 9:"55 Mana"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Dark_Star(Synergies):
    description = "When an ally dies, all DS gain AD and AP"
    name = "Dark Star"
    chr_list = []
    champ_w_trait = ["Jarvan_IV", "Mordekaiser", "Karma", "Shaco", "Jhin", "Xerath"]
    syn = {2: "8 AD and AP", 4: "18 AD and AP", 6:"28 AD and AP", 8:"38 AD and AP"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Cybernetic(Synergies):
    description = "Cybernetics with an item gain bonus AD and HP"
    name = "Cybernetic"
    chr_list = []
    champ_w_trait = ["Fiora", "Leona", "Lucian", "Vi", "Vayne", "Irelia", "Ekko"]
    syn = {3: "40 AD/ 350 HP", 6: "75 AD/ 600 HP"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Astro(Synergies):
    description = "Astro champs have mana cost reduced by 30"
    name = "Astro"
    chr_list = []
    champ_w_trait = ["Nautilus", "Bard", "Gnar", "Teemo"]
    syn = {3: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Space_Pirate(Synergies):
    description = "50'%' chance to drop gold on SP gold"
    name = "Space Pirate"
    chr_list = []
    champ_w_trait = ["Graves", "Darius", "Jayce", "Gangplank"]
    syn = {2: "1 gold", 4: "1 gold and 25% to drop an item"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Rebel(Synergies):
    description = "At start, rebels gain health shield for 8 seconds and increased damage for each adjacent rebel"
    name = "Rebels"
    chr_list = []
    champ_w_trait = ["Malphite", "Ziggs", "Yasuo", "Master_Yi", "Jinx", "Aurelion_Sol"]
    syn = {3: "150 Shield/ 10'%' damage", 6: "210 Shield/ 12'%' damage", 9:"330 Shield/ 15'%' damage"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Mech_Pilot(Synergies):
    description = ("At start, 3 random pilots are merged into a Super-mech, with the combined HP, AD, and traits."
    " When it dies, the pilots are ejected, with 25 mana and 35% HP")
    name = "Mech Pilot"
    chr_list = []
    champ_w_trait = ["Annie", "Rumble", "Fizz"]
    syn = {3: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)

#Traits
class Protector(Synergies):
    description = "Protectors gain a shield scaling off max health for 3 seconds when they cast"
    name = "Protector"
    chr_list = []
    champ_w_trait = ["Jarvan_IV", "Rakan", "Xin_Zhao", "Neeko", "Urgot"]
    syn = {2: "30% max HP shield", 4: "40% max HP shield", 6:"50% max HP shield"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Sniper(Synergies):
    description = "Snipers deal increased damagee for each hex of distance betweeen themselves and the target"
    name = "Sniper"
    chr_list = []
    champ_w_trait = ["Caitlyn", "Ashe", "Vayne", "Jhin", "Teemo"]
    syn = {2: "10% per hex", 4: "18% per hex"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Blademaster(Synergies):
    description = "Blademasters have a chance on hit to attack two extra times"
    name = "Blademaster"
    chr_list = []
    champ_w_trait = ["Fiora", "Xayah", "Shen", "Yasuo", "Master_Yi", "Irelia", "Riven"]
    syn = {3: "30'%' chance on hit", 6: "65'%' chance on hit", 9:"100'%' chance on hit"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Sorcerer(Synergies):
    description = "All allies gain increased spell power"
    name = "Sorcerer"
    chr_list = []
    champ_w_trait = ["Twisted_Fate", "Zoe", "Ahri", "Annie", "Syndra", "Viktor", "Xerath"]
    syn = {2: "20% Spell Power", 4: "45% Spell Power", 6:"75% Spell Power"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Mystic(Synergies):
    description = "Grant the team bonus MR"
    name = "Mystic"
    chr_list = []
    champ_w_trait = ["Bard", "Karma", "Cassiopeia", "Soraka", "Lulu"]
    syn = {2: "50 MR", 4: "120 MR"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Vanguard(Synergies):
    description = "Vanguards gain bonus Armour"
    name = "Vanguard"
    chr_list = []
    champ_w_trait = ["Leona", "Poppy", "Mordekaiser", "Nautilus", "Jayce", "Wukong"]
    syn = {2: "125 Armour", 4: "300 Armour", 6:"1000 Armour"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Brawler(Synergies):
    description = "Brawlers gain bonus HP"
    name = "Brawler"
    chr_list = []
    champ_w_trait = ["Malphite", "Illaoi", "Blitzcrank", "Vi", "Gnar"]
    syn = {2: "350 HP", 4: "600 HP"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Infiltrator(Synergies):
    description = ("Passively, infiltrators jump to the back of the enemy territory at the start of combat." 
    "Infiltrators gain AS for the first 6s of combat, refreshing on takedown")
    name = "Infiltrator"
    chr_list = []
    champ_w_trait = ["Nocturne", "Zed", "Shaco", "Fizz", "Ekko"]
    syn = {2: "40% AS", 4: "80% AS", 6:"120% AS"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Paragon(Synergies):
    description = "Ally SG basic attacks are converted to true damage, all other ally basic attacks are converted to magic damage"
    name = "Paragon"
    chr_list = []
    champ_w_trait = ["Janna"]
    syn = {1: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Starship(Synergies):
    description = "Starships continuously circle the arena and cannot basic attack. Gains 40 mana/s"
    name = "Starship"
    chr_list = []
    champ_w_trait = ["Aurelion_Sol"]
    syn = {1: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Blaster(Synergies):
    description = "Every 4th Blaster attack fires additonal attacks, applying on-hit effects"
    name = "Blaster"
    chr_list = []
    champ_w_trait = ["Graves", "Lucian", "Kog'Maw", "Ezreal", "Jinx"]
    syn = {2: "3 additional attacks", 4: "65 additional attacks"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Mana_Reaver(Synergies):
    description = "Mana Reaver attacks increase the cost of their targets next spell by 40%"
    name = "Mana Reaver"
    chr_list = []
    champ_w_trait = ["Darius", "Irelia", "Thresh"]
    syn = {2: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Demolitionist(Synergies):
    description = "Demolitionist spells stun target for 1.5s"
    name = "Demolitionist"
    chr_list = []
    champ_w_trait = ["Ziggs", "Rumble", "Gankplank"]
    syn = {2: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)
class Mercenary(Synergies):
    description = "Mercs can have spells upgraded"
    name = "Mercenary"
    chr_list = []
    champ_w_trait = ["Gankplank"]
    syn = {1: "Bonus Active"}
    def __init__(self, name, description, syn, chr_list):
        super().__init__(name,description, syn, chr_list)



if __name__ == "__main__":
    #Create champion list
    units = []
    with open("champ_list.txt") as f:
        f.readline()
        fil = f.readlines()
        for lines in fil:
            line = lines.strip().split(",")
            classes = []
            for i in range(len(line)):
                classes.append(line[i])
            units.append(classes)

    #create the random comp
    comp = []
    for i in range(9):
        comp.append(units[random.randint(0,len(units)-1)])      #add a random unit and it's origins and traits to the list

    #dictionary connecting word and class with same name
    trait_lst = ({"Celestial": Celestial, "Chrono": Chrono, "Star_Guardian": Star_Guardian, "Dark_Star": Dark_Star, "Cybernetic": Cybernetic,
        "Astro": Astro, "Space_Pirate": Space_Pirate, "Rebel": Rebel, "Mech_Pilot": Mech_Pilot, "Battlecast": Battlecast, "Protector": Protector, "Sniper": Sniper, "Blademaster": Blademaster, 
        "Sorcerer": Sorcerer, "Mystic": Mystic, "Vanguard": Vanguard, "Brawler": Brawler, "Infiltrator": Infiltrator, "Paragon": Paragon, "Starship": Starship, "Blaster": Blaster, 
        "Mana_Reaver": Mana_Reaver, "Demolitionist": Demolitionist, "Mercenary": Mercenary})
    #make all units from random comp into a unit type
    u1 = Unit(comp[0][0:1], comp[0][1:])
    u2 = Unit(comp[1][0:1], comp[1][1:])
    u3 = Unit(comp[2][0:1], comp[2][1:])
    u4 = Unit(comp[3][0:1], comp[3][1:])
    u5 = Unit(comp[4][0:1], comp[4][1:])
    u6 = Unit(comp[5][0:1], comp[5][1:])
    u7 = Unit(comp[6][0:1], comp[6][1:])
    u8 = Unit(comp[7][0:1], comp[7][1:])
    u9 = Unit(comp[8][0:1], comp[8][1:])

    #list of random units in unit class
    comp_units = [u1,u2,u3,u4,u5,u6,u7,u8,u9]

    #list of all traits that the random units have
    traits_included = []

    print("Your comp is: ")
    for i in comp_units:                                                                    #for all units in comp
        print(i.name[0])                                                                    #print names
        for t in i.synerg:                                                                  #loop for synergies the unit has
            if (i.name[0] in str_to_class(t).champ_w_trait):                                #verification check(if the unit is in the list of units that have that trait)    
                if i.name[0] not in str_to_class(t).chr_list:                               #if the unit is not already in the "chr_list" --> for unit that has the trait and was selected
                    str_to_class(t).chr_list.append(i.name[0])                              #add to the chr_list for that class
                    traits_included.append(t)                                               #add to trait list
    print()
    for t in traits_included:                                                               #for all traits
        print(trait_lst[t].specfic_synergy(trait_lst[t], len(set(trait_lst[t].chr_list))))  #show the specific synergy that would be used 
        print(trait_lst[t].chr_list)                                                        #print list of units under the specific synergy
        