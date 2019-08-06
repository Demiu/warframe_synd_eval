# Created by Demiu
import requests

MARKET_API_URL = "https://api.warframe.market/v1/items"

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
            "Regenerative Volt",
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
            "Entropy Burst"
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
            "Pilfering Sward",
            # Ivara
            "Empowered Quiver",
            "Piercing Navigator",
            "Infiltrate",
            "Concetrated Arrow",
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
            "Sequence Burn"
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
            "Concetrated Arrow",
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
            "Gleaming Blith",
            "Eroding Blith",
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
            "Regenerative Volt",
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
            "Pilfering Sward",
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
                    rewards_data_by_name[synd_rew_name] = [synd_rew_cost, 0]

    market_items = get_page(MARKET_API_URL).json()['payload']['items']
    i = 1