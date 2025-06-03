import pandas as pd
import numpy as np
import json

# Definieer de vier hoofdcategorieën gebaseerd op Louis' documenten
categories = {
    "Chakra_Guide": {
        "subcategories": ["Root", "Sacral", "Solar_Plexus", "Heart", "Throat", "Third_Eye", "Crown"],
        "scoring_range": (5, 25),  # Gebaseerd op chakra assessment tools
        "elemental_correspondence": {
            "Root": "Earth", "Sacral": "Water", "Solar_Plexus": "Fire", 
            "Heart": "Air", "Throat": "Air", "Third_Eye": "Spirit", "Crown": "Spirit"
        }
    },
    "Divine_Elements": {
        "subcategories": ["Pentagram", "Hexagon", "Seed_of_Life", "Tree_of_Life", 
                         "Egg_of_Life", "Flower_of_Life", "Fruit_of_Life", "Metatrons_Cube"],
        "scoring_range": (1, 10),
        "elemental_correspondence": {
            "Pentagram": "Spirit", "Hexagon": "Air", "Seed_of_Life": "Water",
            "Tree_of_Life": "Spirit", "Egg_of_Life": "Earth", "Flower_of_Life": "Spirit",
            "Fruit_of_Life": "Fire", "Metatrons_Cube": "Spirit"
        }
    },
    "Tree_of_Life_Knowledge": {
        "subcategories": ["Keter", "Chokhmah", "Binah", "Chesed", "Gevurah", 
                         "Tiferet", "Netzach", "Hod", "Yesod", "Malkuth"],
        "scoring_range": (1, 10),
        "elemental_correspondence": {
            "Keter": "Spirit", "Chokhmah": "Air", "Binah": "Water",
            "Chesed": "Water", "Gevurah": "Fire", "Tiferet": "Spirit",
            "Netzach": "Fire", "Hod": "Water", "Yesod": "Air", "Malkuth": "Earth"
        }
    },
    "Tree_of_Life_Experience": {
        "subcategories": ["Mystical_Unity", "Transcendence_Time_Space", "Ineffability", 
                         "Sacred_Quality", "Noetic_Quality", "Positive_Mood"],
        "scoring_range": (0, 100),  # Percentage gebaseerd systeem zoals MEQ30
        "elemental_correspondence": {
            "Mystical_Unity": "Spirit", "Transcendence_Time_Space": "Air",
            "Ineffability": "Water", "Sacred_Quality": "Spirit",
            "Noetic_Quality": "Fire", "Positive_Mood": "Earth"
        }
    }
}

# Definieer elementaire doelen (de 5 eindelementen)
elemental_goals = {
    "Air": {"target_score": 100, "qualities": ["Intellect", "Communication", "Movement", "Clarity"]},
    "Earth": {"target_score": 100, "qualities": ["Grounding", "Manifestation", "Stability", "Growth"]},
    "Fire": {"target_score": 100, "qualities": ["Transformation", "Passion", "Energy", "Will"]},
    "Water": {"target_score": 100, "qualities": ["Emotion", "Intuition", "Flow", "Healing"]},
    "Spirit": {"target_score": 100, "qualities": ["Unity", "Transcendence", "Wisdom", "Connection"]}
}

print("✨ AWAKEN CONSCIOUSNESS SCORING SYSTEEM ✨")
print("=" * 50)
print(f"📊 Categorieën gedefinieerd: {len(categories)}")
print(f"🌟 Elementaire doelen: {len(elemental_goals)}")

# Toon de structuur
for cat_name, cat_data in categories.items():
    print(f"\n🔮 {cat_name}:")
    print(f"   Subcategorieën: {len(cat_data['subcategories'])}")
    print(f"   Score range: {cat_data['scoring_range']}")
    print(f"   Voorbeelden: {cat_data['subcategories'][:3]}...")