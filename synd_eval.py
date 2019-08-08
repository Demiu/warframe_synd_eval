# Created by Demiu
import requests
import sys

MARKET_API_URL = "https://api.warframe.market/v1/items"

# Default value for how many listings of lowest value should be included in the average
PRICE_AVERAGE_FIRST = 3

# Plat per (standing / divisor) is easier for humans than plat per standing
STANDING_DIVISOR = 1000

# How many rewards to list per syndicate, sorted by plat per standing (decreasing)
LIST_BEST_N_REWARDS = 5

syndicate_rewards = {
    "Steel Meridian" : {
        20000 : (
            "Kaszas Handle",
            "Velocitus Receiver",
            "Corvas Stock",
            "Agkuza Guard",
            "Fluctus Stock"
        ),
        25000 : (
            # Weapon Augments
            "Scattered Justice",
            "Justice Blades",
            "Neutralizing Justice",
            "Shattering Justice",
            # Atlas
            "Path of Statues",
            "Tectonic Fracture",
            "Ore Gaze",
            "Titanic Rumbler",
            # Ember
            "Fireball Frenzy",
            "Flash Accelerant",
            "Fire Fright",
            "Firequake",
            # Excalibur
            "Surging Dash",
            "Radiant Finish",
            "Furious Javelin",
            "Chromatic Blade",
            # Frost
            "Freeze Force",
            "Ice Wave Impedance",
            "Chilling Globe",
            "Icy Avalanche",
            # Garuda
            "Dread Ward",
            # Khora
            "Accumulating Whipclaw",
            "Venari Bodyguard",
            "Pilfering Strangledome",
            # Mesa
            "Ballistic Bullseye",
            "Staggering Shield",
            "Muzzle Flash",
            "Mesa’s Waltz",
            # Nezha
            "Pyroclastic Flow",
            "Reaping Chakram",
            "Safeguard",
            # Nidus
            "Teeming Virulence",
            "Larva Burst",
            "Insatiable",
            # Nova
            "Neutron Star",
            "Antimatter Absorb",
            "Escape Velocity",
            # Oberon
            "Smite Infusion",
            "Hallowed Eruption",
            "Phoenix Renewal",
            "Hallowed Reckoning",
            # Rhino
            "Ironclad Charge",
            "Iron Shrapnel",
            "Piercing Roar",
            "Reinforcing Stomp",
            # Saryn
            "Venom Dose",
            "Regenerative Molt",
            "Contagion Cloud"
        ),
        100000 : (
            "Vaykor Marelok",
            "Cressa's Garrison Scene",
            "Grineer Settlement Reactor Scene",
            "Kuva Throne Scene",
        ),
        125000 : (
            "Vaykor Hek",
            "Vaykor Sydon"
        )
    },
    "Arbiters of Hexis" : {
        20000 : (
            "Decurion Barrel",
            "Phaedra Barrel",
            "Corvas Barrel",
            "Cyngas Barrel",
            "Centaur Aegis"
        ),
        25000 : (
            # Weapon Augments
            "Gilded Truth",
            "Blade of Truth",
            "Avenging Truth",
            "Stinging Truth",
            # Ash
            "Seeking Shuriken",
            "Smoke Shadow",
            "Fatal Teleport",
            "Rising Storm",
            # Equinox
            "Duality",
            "Calm & Frenzy",
            "Peaceful Provocation",
            "Energy Transfer",
            # Excalibur
            "Surging Dash",
            "Radiant Finish",
            "Furious Javelin",
            "Chromatic Blade",
            # Gara
            "Mending Splinters",
            # Harrow
            "Warding Thurible",
            "Lasting Covenant",
            # Inaros
            "Elemental Sandstorm",
            "Negation Swarm",
            # Limbo
            "Rift Haven",
            "Rift Torrent",
            "Cataclysmic Continuum",
            # Loki
            "Savior Decoy",
            "Hushed Invisibility",
            "Safeguard Switch",
            "Irradiating Disarm",
            # Mirage
            "Hall of Malevolence",
            "Explosive Legerdemain",
            "Total Eclipse",
            # Nyx
            "Mind Freak",
            "Pacifying Bolts",
            "Chaos Sphere",
            "Assimilate",
            # Volt
            "Shock Trooper",
            "Shocking Speed",
            "Transistor Shield",
            "Capacitance",
            # Wukong
            "Celestial Stomp",
            "Enveloping Cloud",
            "Primal Rage"
        ),
        100000 : (
            "Telos Akbolto",
            "Arbiter's Tribunal Scene",
            "Lua Nursery Scene",
            "Lua Containment Scene"
        ),
        125000 : (
            "Telos Boltor",
            "Telos Boltace"
        )
    },
    "Cephalon Suda" : {
        20000 : (
            "Decurion Receiver",
            "Velocitus Barrel",
            "Corvas Receiver",
            "Cyngas Receiver",
            "Fluctus Barrel"
        ),
        25000 : (
            # Weapon Augments
            "Entropy Spike",
            "Entropy Flight",
            "Entropy Detonation",
            "Entropy Burst",
            # Banshee
            "Sonic Fracture",
            "Resonance",
            "Savage Silence",
            "Resonating Quake",
            # Chroma
            "Afterburn",
            "Everlasting Ward",
            "Vexing Retaliation",
            "Guided Effigy",
            # Frost
            "Freeze Force",
            "Ice Wave Impedance",
            "Chilling Globe",
            "Icy Avalanche",
            # Hydroid
            "Corroding Barrage",
            "Tidal Impunity",
            "Curative Undertow",
            "Pilfering Swarm",
            # Ivara
            "Empowered Quiver",
            "Piercing Navigator",
            "Infiltrate",
            "Concentrated Arrow",
            # Limbo
            "Rift Haven",
            "Rift Torrent",
            "Cataclysmic Continuum",
            # Mirage
            "Hall of Malevolence",
            "Explosive Legerdemain",
            "Total Eclipse",
            # Nezha
            "Pyroclastic Flow",
            "Reaping Chakram",
            "Safeguard",
            # Nova
            "Neutron Star",
            "Antimatter Absorb",
            "Escape Velocity",
            # Octavia
            "Partitioned Mallet",
            "Conductor",
            # Revenant
            "Blinding Reave",
            # Vauban
            "Tesla Link",
            "Repelling Bastille",
            "Perpetual Vortex"
        ),
        100000 : (
            "Synoid Gammacor",
            "Suda's Datascape Scene",
            "Hunhow's Datascape Scene",
            "Corpus Ice Planet Wreckage Scene",
            "Chamber Of The Lotus Scene"
        ),
        125000 : (
            "Synoid Simulor",
            "Synoid Heliocor"
        )
    },
    "The Perrin Sequence" : {
        10000 : (
            "Onorix Handle",
            "Phaedra Receiver",
            "Centaur Blade",
            "Cyngas Stock"
        ),
        25000 : (
            # Weapon Augments
            "Toxic Sequence",
            "Deadly Sequence",
            "Voltage Sequence",
            "Sequence Burn",
            # Banshee
            "Sonic Fracture",
            "Resonance",
            "Savage Silence",
            "Resonating Quake",
            # Chroma
            "Afterburn",
            "Everlasting Ward",
            "Vexing Retaliation",
            "Guided Effigy",
            # Inaros
            "Elemental Sandstorm",
            "Negation Swarm",
            # Ivara
            "Empowered Quiver",
            "Piercing Navigator",
            "Infiltrate",
            "Concentrated Arrow",
            # Mag
            "Greedy Pull",
            "Magnetized Discharge",
            "Counter Pulse",
            "Fracturing Crush",
            # Nekros
            "Soul Survivor",
            "Creeping Terrify",
            "Despoil",
            "Shield of Shadows",
            # Nidus
            "Teeming Virulence",
            "Larva Burst",
            "Insatiable",
            # Revenant
            "Blinding Reave",
            # Rhino
            "Ironclad Charge",
            "Iron Shrapnel",
            "Piercing Roar",
            "Reinforcing Stomp",
            # Trinity
            "Pool of Life",
            "Vampire Leech",
            "Abating Link",
            # Valkyr
            "Swing Line",
            "Eternal War",
            "Prolonged Paralysis",
            "Hysterical Assault",
            # Vauban
            "Tesla Link",
            "Repelling Bastille",
            "Perpetual Vortex"
        ),
        100000 : (
            "Secura Dual Cestra",
            "Ergo's Boardroom Scene",
            "Corpus Gas City Conduit Scene",
            "Mycona Colony Scene",
        ),
        125000 : (
            "Secura Penta",
            "Secura Lecta"
        )
    },
    "Red Veil" : {
        10000 : (
            "Kaszas Blade",
            "Velocitus Stock",
            "Rathbone Handle",
            "Agkuza Handle",
            "Fluctus Limbs"
        ),
        25000 : (
            # Weapon Augments
            "Gleaming Blight",
            "Eroding Blight",
            "Stockpiled Blight",
            "Toxic Blight",
            # Ash
            "Seeking Shuriken",
            "Smoke Shadow",
            "Fatal Teleport",
            "Rising Storm",
            # Atlas
            "Path of Statues",
            "Tectonic Fracture",
            "Ore Gaze",
            "Titanic Rumbler",
            # Ember
            "Fireball Frenzy",
            "Flash Accelerant",
            "Fire Fright",
            "Firequake",
            # Garuda
            "Dread Ward",
            # Harrow
            "Warding Thurible",
            "Lasting Covenant",
            # Khora
            "Accumulating Whipclaw",
            "Venari Bodyguard",
            "Pilfering Strangledome",
            # Loki
            "Savior Decoy",
            "Hushed Invisibility",
            "Safeguard Switch",
            "Irradiating Disarm",
            # Mesa
            "Ballistic Bullseye",
            "Staggering Shield",
            "Muzzle Flash",
            "Mesa’s Waltz",
            # Nekros
            "Soul Survivor",
            "Creeping Terrify",
            "Despoil",
            "Shield of Shadows",
            # Saryn
            "Venom Dose",
            "Regenerative Molt",
            "Contagion Cloud",
            # Titania
            "Beguiling Lantern",
            "Razorwing Blitz",
            # Volt
            "Shock Trooper",
            "Shocking Speed",
            "Transistor Shield",
            "Capacitance",
            # Zephyr
            "Target Fixation",
            "Jet Stream",
            "Funnel Clouds"
        ),
        100000 : (
            "Rakta Ballistica",
            "Veil's Binding Scene",
            "Harrow's Temple Scene",
            "Infested Ship Bridge Scene",
            "Hunhow's Chamber Scene"
        ),
        125000 : (
            "Rakta Cernos",
            "Rakta Dark Dagger"
        )
    },
    "New Loka" : {
        10000 : (
            "Onorix Blade",
            "Phaedra Stock",
            "Rathbone Head",
            "Agkuza Blade",
            "Centaur Handle"
        ),
        25000 : (
            # Weapon Augments
            "Winds of Purity",
            "Disarming Purity",
            "Bright Purity",
            "Lasting Purity",
            # Equinox
            "Duality",
            "Calm & Frenzy",
            "Peaceful Provocation",
            "Energy Transfer",
            # Gara
            "Mending Splinters",
            # Hydroid
            "Corroding Barrage",
            "Tidal Impunity",
            "Curative Undertow",
            "Pilfering Swarm",
            # Mag
            "Greedy Pull",
            "Magnetized Discharge",
            "Counter Pulse",
            "Fracturing Crush",
            # Nyx
            "Mind Freak",
            "Pacifying Bolts",
            "Chaos Sphere",
            "Assimilate",
            # Oberon
            "Smite Infusion",
            "Hallowed Eruption",
            "Phoenix Renewal",
            "Hallowed Reckoning",
            # Octavia
            "Partitioned Mallet",
            "Conductor",
            # Titania
            "Beguiling Lantern",
            "Razorwing Blitz",
            # Trinity
            "Pool of Life",
            "Vampire Leech",
            "Abating Link",
            # Valkyr
            "Swing Line",
            "Eternal War",
            "Prolonged Paralysis",
            "Hysterical Assault",
            # Zephyr
            "Target Fixation",
            "Jet Stream",
            "Funnel Clouds",
            # Wukong
            "Celestial Stomp",
            "Enveloping Cloud",
            "Primal Rage"
        ),
        100000 : (
            "Sancti Castanas",
            "Amaryn's Retreat Scene",
            "Grineer Shipyards Manufactory Scene",
            "Silver Grove Shrine Scene"
        ),
        125000 : (
            "Sancti Tigris",
            "Sancti Magistar"
        )
    }
}

def price(orders, average_of_first=PRICE_AVERAGE_FIRST):
    n = len(orders)
    if n < 1:
            return 0
    if n < average_of_first:
            orders_sorted = sorted(orders, key = lambda x: x[0])

            sum = 0
            quant = 0
            for order in orders_sorted[0:n]:
                sum += order[0]
                quant += order[1]
            return sum/quant
    else:
            orders_sorted = sorted(orders, key = lambda x: x[0])
            
            sum = 0
            quant = 0
            for order in orders_sorted[0:average_of_first]:
                sum += order[0]
                quant += order[1]
            return sum/quant


def get_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response

if __name__ == '__main__':
    rewards_data_by_name = {}
    for synd_name, synd_rew_tiers in syndicate_rewards.items():
        for synd_rew_cost, synd_rew_at_cost in synd_rew_tiers.items():
            for synd_rew_name in synd_rew_at_cost:
                if synd_rew_name not in rewards_data_by_name:
                    # Standing cost, in-game average price, in-game and online and offline average price
                    rewards_data_by_name[synd_rew_name] = [0, 0]

    market_items = get_page(MARKET_API_URL).json()['payload']['items']
    
    rewards_i = 0
    rewards_num = len(rewards_data_by_name)
    for reward_name, reward_data in rewards_data_by_name.items():
        id = -1
        for i, market_item in enumerate(market_items):
            if market_item['item_name'] == reward_name:
                id = i
                break
        
        if id == -1:
            print("\nCould not find market data for {0}! Check spelling or if item is listed on warframe.market".format(reward_name))
        else:
            item_orders_url = "https://api.warframe.market/v1/items/{0}/orders".format(market_item['url_name'])
            item_orders = get_page(item_orders_url).json()['payload']['orders']
            item_orders = [
                            (order['platinum'], order['quantity'], order['user']['status']) 
                            for order in item_orders 
                            if order['order_type'] == 'sell' and order['region'] == 'en'
            ]
            
            # In-game
            rewards_data_by_name[reward_name][0] = price([
                order[0:2]
                for order in item_orders
                if order[2] == 'ingame'
            ])
            # In-game, online and offline
            rewards_data_by_name[reward_name][1] = price([
                order[0:2]
                for order in item_orders
            ])

        rewards_i += 1
        sys.stdout.write("\rGetting items market data... {:.2f}%".format(100*rewards_i/rewards_num))
        sys.stdout.flush()
    
    print("\nAssigning data to syndicates...")
    syndicate_rewards_sorted = {}
    for synd_name, synd_rew_tiers in syndicate_rewards.items():
        syndicate_rewards_sorted[synd_name] = []
        for synd_rew_cost, synd_rew_at_cost in synd_rew_tiers.items():
            for synd_rew_name in synd_rew_at_cost:
                syndicate_rewards_sorted[synd_name].append((
                    synd_rew_name,
                    rewards_data_by_name[synd_rew_name][0] / (synd_rew_cost / STANDING_DIVISOR),
                    rewards_data_by_name[synd_rew_name][1] / (synd_rew_cost / STANDING_DIVISOR),
                ))
    
    for synd_name, synd_rew_list in syndicate_rewards_sorted.items():
        syndicate_rewards_sorted[synd_name] = sorted(syndicate_rewards_sorted[synd_name], key = lambda x: x[1], reverse=True)
    
    print("\nFormat of rewards is: name (plat per 1k standing for online offers, plat per 1k standing for all offers)")
    for synd_name, synd_rew_list in syndicate_rewards_sorted.items():
        print("\nBest offerings for {0}:".format(synd_name))

        for i, reward in enumerate(synd_rew_list):
            if i == LIST_BEST_N_REWARDS:
                break

            print("* {0} ({1:.2f}, {2:.2f})".format(reward[0], reward[1], reward[2]))