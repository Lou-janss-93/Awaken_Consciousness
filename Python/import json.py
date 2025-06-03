import json

# Create a comprehensive data structure for Louis' Awaken Consciousness project
project_overview = {
    "project_name": "Awaken Consciousness",
    "concept": "Interactive webapp voor spirituele ontwikkeling met sacred geometry",
    "core_principles": [
        "As Above, So Below (Emerald Tablet)",
        "Consciousness Continuum ontwikkeling", 
        "Sacred Geometry visualisatie",
        "Interactieve symboliek exploratie"
    ],
    "structure": {
        "phases": 5,
        "elements": ["Air", "Earth", "Fire", "Water", "Universe"],
        "progression": "Van simpel naar complex bewustzijn"
    },
    "visual_design": {
        "color_progression": {
            "phase_1": "Wit (#ffffff) - Puur, onbeschreven",
            "phase_2": "Subtiele hints van elementkleuren",
            "phase_3": "Pastelachtige versies",
            "phase_4": "Diepe, rijke tinten",
            "phase_5": "Volle, felle kleuren - Awakening"
        },
        "theme": {
            "primary_colors": ["Diepblauw (#1A237E)", "Paars (#6C2EB6)", "Goud (#FFD700)"],
            "secondary_colors": ["Turquoise (#00B8D4)", "Wit (#F5F5F5)"],
            "style": "Mystiek, kosmisch, lichtgevend, modern"
        }
    },
    "technology_stack": {
        "frontend": ["HTML5", "CSS3", "JavaScript"],
        "features": ["Sacred geometry explorer", "Interactive symbols", "Phase transitions", "Audio integration"],
        "responsive": True,
        "accessibility": "WCAG 2.1 compliant"
    }
}

# Symbol categories from the conversation
symbol_categories = {
    "simple_universal": [
        "Dot & Circle", "Triangle", "Square", "Feather", "Sun", "Key", 
        "Bell/Gong", "Mirror", "Torch", "Hourglass", "Pine Cones"
    ],
    "natural_geometric": [
        "Spiral", "Labyrinth", "Butterfly", "Lotus", "Bodhi tree", 
        "Tree of Life", "Golden Fish", "Flower of Life", "River", "Beehive"
    ],
    "complex_spiritual": [
        "Yin Yang", "Infinity", "Hexagram", "Vajra", "Mandala", 
        "Yantras", "Platonic Solids", "Sankofa", "Kongo Cosmogram"
    ],
    "esoteric_advanced": [
        "Ouroboros", "Merkaba", "Third Eye Chakra", "Buddha's eyes", 
        "Sri Yantra", "Metatron's Cube", "Torus", "Unalome"
    ]
}

# Element mappings for Phase 5
element_meanings = {
    "Air": {
        "symbolism": "Intellect, communicatie, mentale bevrijding",
        "colors": ["Lichtblauw (#AEEFFF)", "Wit", "Zacht grijs"],
        "energy": "Inspiratie, denken, eerste ontwaking"
    },
    "Earth": {
        "symbolism": "Gronding, manifestatie, belichaming",
        "colors": ["Diep groen (#2E7D32)", "Warm bruin (#8D6748)", "Beige (#F5E5C0)"],
        "energy": "Integratie van kennis in dagelijks leven"
    },
    "Fire": {
        "symbolism": "Transformatie, wilskracht, innerlijk licht",
        "colors": ["Diep oranje (#FF6F00)", "Vurig rood (#FF3D00)", "Goudgeel (#FFF176)"],
        "energy": "Zuivering en bewustzijnsverruiming"
    },
    "Water": {
        "symbolism": "Emotie, intuïtie, collectief geheugen",
        "colors": ["Diep blauw (#1976D2)", "Turquoise (#00B8D4)", "Zacht wit"],
        "energy": "Stroom van bewustzijn en verbinding"
    },
    "Universe": {
        "symbolism": "Non-dualiteit, kosmisch bewustzijn, eenheid",
        "colors": ["Diep paars (#6C2EB6)", "Nachtblauw (#1A237E)", "Zilver/wit"],
        "energy": "Ultieme eenheid en universele kennis"
    }
}

print("=== AWAKEN CONSCIOUSNESS PROJECT OVERVIEW ===")
print(f"Project: {project_overview['project_name']}")
print(f"Concept: {project_overview['concept']}")
print()

print("CORE PRINCIPLES:")
for principle in project_overview['core_principles']:
    print(f"• {principle}")
print()

print("STRUCTURE:")
print(f"• {project_overview['structure']['phases']} fasen")
print(f"• Elementen: {', '.join(project_overview['structure']['elements'])}")
print(f"• Progressie: {project_overview['structure']['progression']}")
print()

print("SYMBOL CATEGORIES (Van Simpel naar Complex):")
for category, symbols in symbol_categories.items():
    print(f"\n{category.upper().replace('_', ' ')}:")
    for symbol in symbols[:5]:  # Show first 5 of each category
        print(f"  • {symbol}")
    if len(symbols) > 5:
        print(f"  ... en {len(symbols)-5} meer")
print()

print("ELEMENT BETEKENISSEN (Fase 5):")
for element, details in element_meanings.items():
    print(f"\n{element.upper()}:")
    print(f"  Symboliek: {details['symbolism']}")
    print(f"  Kleuren: {', '.join(details['colors'])}")
    print(f"  Energie: {details['energy']}")

# Save comprehensive project data as JSON for potential use
with open('awaken_consciousness_project_data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "project_overview": project_overview,
        "symbol_categories": symbol_categories,
        "element_meanings": element_meanings
    }, f, ensure_ascii=False, indent=2)

print(f"\n\nProject data saved to: awaken_consciousness_project_data.json")