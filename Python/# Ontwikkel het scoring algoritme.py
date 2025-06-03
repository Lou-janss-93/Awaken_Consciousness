# Ontwikkel het scoring algoritme
def calculate_elemental_scores(user_responses):
    """
    Berekent elementaire scores gebaseerd op gebruikersresponsen in alle vier categorieën
    """
    elemental_scores = {element: 0 for element in elemental_goals.keys()}
    detailed_breakdown = {element: [] for element in elemental_goals.keys()}
    
    for category_name, responses in user_responses.items():
        category_data = categories[category_name]
        
        for subcategory, score in responses.items():
            # Normaliseer score naar 0-100 schaal
            min_score, max_score = category_data['scoring_range']
            normalized_score = ((score - min_score) / (max_score - min_score)) * 100
            
            # Zoek elementaire correspondentie
            element = category_data['elemental_correspondence'].get(subcategory, "Spirit")
            
            # Voeg gewogen score toe (verschillende categorieën hebben verschillende gewichten)
            weight = get_category_weight(category_name)
            weighted_score = normalized_score * weight
            
            elemental_scores[element] += weighted_score
            detailed_breakdown[element].append({
                'category': category_name,
                'subcategory': subcategory,
                'raw_score': score,
                'normalized': round(normalized_score, 2),
                'weighted': round(weighted_score, 2)
            })
    
    return elemental_scores, detailed_breakdown

def get_category_weight(category_name):
    """Definieer gewichten voor verschillende categorieën"""
    weights = {
        "Chakra_Guide": 0.3,  # 30% - Basis energiecentra
        "Divine_Elements": 0.2,  # 20% - Sacred geometry kennis
        "Tree_of_Life_Knowledge": 0.25,  # 25% - Kabbalistische wijsheid
        "Tree_of_Life_Experience": 0.25   # 25% - Mystieke ervaring
    }
    return weights.get(category_name, 0.25)

def determine_flow_progression(elemental_scores):
    """
    Bepaalt de progressie naar de 5 eindelementen gebaseerd op scores
    """
    # Bereken totale spirituele score
    total_score = sum(elemental_scores.values())
    average_score = total_score / len(elemental_scores)
    
    # Bepaal dominante en onderontwikkelde elementen
    sorted_elements = sorted(elemental_scores.items(), key=lambda x: x[1], reverse=True)
    dominant_element = sorted_elements[0]
    weakest_element = sorted_elements[-1]
    
    # Bepaal bewustzijnsniveau gebaseerd op gemiddelde score
    if average_score >= 80:
        consciousness_level = "Mastery - Unified Consciousness"
        phase = 5
    elif average_score >= 60:
        consciousness_level = "Integration - Balanced Awareness"
        phase = 4
    elif average_score >= 40:
        consciousness_level = "Development - Growing Understanding"
        phase = 3
    elif average_score >= 20:
        consciousness_level = "Awakening - Initial Recognition"
        phase = 2
    else:
        consciousness_level = "Foundation - Basic Awareness"
        phase = 1
    
    return {
        'total_score': round(total_score, 2),
        'average_score': round(average_score, 2),
        'consciousness_level': consciousness_level,
        'phase': phase,
        'dominant_element': dominant_element,
        'weakest_element': weakest_element,
        'balance_ratio': round(dominant_element[1] / max(weakest_element[1], 1), 2)
    }

# Simuleer gebruikersdata voor demonstratie
sample_user_responses = {
    "Chakra_Guide": {
        "Root": 20, "Sacral": 18, "Solar_Plexus": 22, "Heart": 25,
        "Throat": 15, "Third_Eye": 12, "Crown": 10
    },
    "Divine_Elements": {
        "Pentagram": 8, "Hexagon": 7, "Seed_of_Life": 9,
        "Tree_of_Life": 10, "Egg_of_Life": 6, "Flower_of_Life": 9,
        "Fruit_of_Life": 7, "Metatrons_Cube": 8
    },
    "Tree_of_Life_Knowledge": {
        "Keter": 6, "Chokhmah": 8, "Binah": 7, "Chesed": 9,
        "Gevurah": 5, "Tiferet": 8, "Netzach": 6, "Hod": 7,
        "Yesod": 8, "Malkuth": 9
    },
    "Tree_of_Life_Experience": {
        "Mystical_Unity": 45, "Transcendence_Time_Space": 60,
        "Ineffability": 55, "Sacred_Quality": 70,
        "Noetic_Quality": 50, "Positive_Mood": 80
    }
}

# Bereken scores
elemental_scores, detailed_breakdown = calculate_elemental_scores(sample_user_responses)
flow_progression = determine_flow_progression(elemental_scores)

print("🌟 ELEMENTAIRE SCORE RESULTATEN 🌟")
print("=" * 40)
for element, score in elemental_scores.items():
    emoji = {"Air": "🌪️", "Earth": "🌍", "Fire": "🔥", "Water": "🌊", "Spirit": "✨"}[element]
    print(f"{emoji} {element}: {score:.1f}/100")

print(f"\n📊 BEWUSTZIJNSNIVEAU")
print(f"Gemiddelde Score: {flow_progression['average_score']:.1f}/100")
print(f"Huidige Fase: {flow_progression['phase']}/5")
print(f"Niveau: {flow_progression['consciousness_level']}")
print(f"Dominant Element: {flow_progression['dominant_element'][0]} ({flow_progression['dominant_element'][1]:.1f})")
print(f"Te Ontwikkelen: {flow_progression['weakest_element'][0]} ({flow_progression['weakest_element'][1]:.1f})")
print(f"Balans Ratio: {flow_progression['balance_ratio']:.1f}")