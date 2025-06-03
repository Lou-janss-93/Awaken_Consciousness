// Awaken Consciousness Application
class AwakeningConsciousness {
    constructor() {
        this.assessmentData = {
            "categories": {
                "Chakra_Guide": {
                    "subcategories": ["Root", "Sacral", "Solar_Plexus", "Heart", "Throat", "Third_Eye", "Crown"],
                    "scoring_range": [5, 25],
                    "weight": 0.3,
                    "elemental_mapping": {
                        "Root": "Earth", "Sacral": "Water", "Solar_Plexus": "Fire", 
                        "Heart": "Air", "Throat": "Air", "Third_Eye": "Spirit", "Crown": "Spirit"
                    }
                },
                "Divine_Elements": {
                    "subcategories": ["Pentagram", "Hexagon", "Seed_of_Life", "Tree_of_Life", "Egg_of_Life", "Flower_of_Life", "Fruit_of_Life", "Metatrons_Cube"],
                    "scoring_range": [1, 10],
                    "weight": 0.2,
                    "elemental_mapping": {
                        "Pentagram": "Spirit", "Hexagon": "Air", "Seed_of_Life": "Water", 
                        "Tree_of_Life": "Spirit", "Egg_of_Life": "Earth", "Flower_of_Life": "Spirit", 
                        "Fruit_of_Life": "Fire", "Metatrons_Cube": "Spirit"
                    }
                },
                "Tree_of_Life_Knowledge": {
                    "subcategories": ["Keter", "Chokhmah", "Binah", "Chesed", "Gevurah", "Tiferet", "Netzach", "Hod", "Yesod", "Malkuth"],
                    "scoring_range": [1, 10],
                    "weight": 0.25,
                    "elemental_mapping": {
                        "Keter": "Spirit", "Chokhmah": "Air", "Binah": "Water", "Chesed": "Water", 
                        "Gevurah": "Fire", "Tiferet": "Spirit", "Netzach": "Fire", "Hod": "Water", 
                        "Yesod": "Air", "Malkuth": "Earth"
                    }
                },
                "Tree_of_Life_Experience": {
                    "subcategories": ["Mystical_Unity", "Transcendence_Time_Space", "Ineffability", "Sacred_Quality", "Noetic_Quality", "Positive_Mood"],
                    "scoring_range": [0, 100],
                    "weight": 0.25,
                    "elemental_mapping": {
                        "Mystical_Unity": "Spirit", "Transcendence_Time_Space": "Air", "Ineffability": "Water", 
                        "Sacred_Quality": "Spirit", "Noetic_Quality": "Fire", "Positive_Mood": "Earth"
                    }
                }
            },
            "elements": {
                "Air": {"color": "#87CEEB", "qualities": ["Intellect", "Communication", "Movement", "Clarity"]},
                "Earth": {"color": "#228B22", "qualities": ["Grounding", "Manifestation", "Stability", "Growth"]},
                "Fire": {"color": "#FF4500", "qualities": ["Transformation", "Passion", "Energy", "Will"]},
                "Water": {"color": "#1E90FF", "qualities": ["Emotion", "Intuition", "Flow", "Healing"]},
                "Spirit": {"color": "#9370DB", "qualities": ["Unity", "Transcendence", "Wisdom", "Connection"]}
            },
            "consciousness_phases": [
                {"phase": 1, "name": "Foundation - Basic Awareness", "range": "0-20", "description": "Beginning to recognize spiritual dimensions"},
                {"phase": 2, "name": "Awakening - Initial Recognition", "range": "20-40", "description": "Growing awareness of inner spiritual nature"},
                {"phase": 3, "name": "Development - Growing Understanding", "range": "40-60", "description": "Actively developing spiritual practices and knowledge"},
                {"phase": 4, "name": "Integration - Balanced Awareness", "range": "60-80", "description": "Integrating spiritual understanding into daily life"},
                {"phase": 5, "name": "Mastery - Unified Consciousness", "range": "80-100+", "description": "Embodying unified spiritual consciousness"}
            ]
        };

        this.scores = {
            chakra: {},
            divine: {},
            knowledge: {},
            experience: {}
        };

        this.completed = {
            chakra: false,
            divine: false,
            knowledge: false,
            experience: false
        };

        this.init();
    }

    init() {
        this.setupEventListeners();
        this.generateAssessmentForms();
        this.updateProgress();
        this.showElementalPreview(); // Show preview immediately
    }

    setupEventListeners() {
        // Assessment card clicks
        document.querySelectorAll('.assessment-card').forEach(card => {
            card.addEventListener('click', (e) => {
                const category = e.currentTarget.dataset.category;
                this.showSection(`${category}-assessment`);
            });
        });

        // Back to landing buttons
        document.querySelectorAll('.back-to-landing').forEach(btn => {
            btn.addEventListener('click', () => this.showSection('landing'));
        });

        // Results button
        const viewResultsBtn = document.getElementById('view-results-btn');
        if (viewResultsBtn) {
            viewResultsBtn.addEventListener('click', () => this.showResults());
        }

        // Export and restart buttons
        const exportBtn = document.getElementById('export-results');
        const restartBtn = document.getElementById('restart-assessment');
        
        if (exportBtn) {
            exportBtn.addEventListener('click', () => this.exportResults());
        }
        
        if (restartBtn) {
            restartBtn.addEventListener('click', () => this.restartAssessment());
        }
    }

    showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });

        // Show target section
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.add('active');
            targetSection.classList.add('fade-in');
        }
    }

    generateAssessmentForms() {
        this.generateChakraForm();
        this.generateDivineForm();
        this.generateKnowledgeForm();
        this.generateExperienceForm();
    }

    generateChakraForm() {
        const form = document.getElementById('chakra-form');
        const category = this.assessmentData.categories.Chakra_Guide;
        
        const questions = {
            "Root": "Hoe gegrond en verbonden voel je je met de aarde en je fysieke lichaam?",
            "Sacral": "Hoe balanceert je creativiteit, seksualiteit en emotionele expressie?",
            "Solar_Plexus": "Hoe sterk is je persoonlijke kracht en zelfvertrouwen?",
            "Heart": "Hoe open en liefdevol is je hart naar jezelf en anderen?",
            "Throat": "Hoe authentiek en helder communiceer je je waarheid?",
            "Third_Eye": "Hoe ontwikkeld is je intuïtie en innerlijke wijsheid?",
            "Crown": "Hoe verbonden voel je je met het goddelijke en universele bewustzijn?"
        };

        category.subcategories.forEach(chakra => {
            const questionDiv = this.createSliderQuestion(
                chakra,
                questions[chakra],
                category.scoring_range[0],
                category.scoring_range[1],
                'chakra'
            );
            form.appendChild(questionDiv);
        });

        const buttonsDiv = this.createFormButtons('chakra');
        form.appendChild(buttonsDiv);
    }

    generateDivineForm() {
        const form = document.getElementById('divine-form');
        const category = this.assessmentData.categories.Divine_Elements;
        
        const questions = {
            "Pentagram": "Hoe goed begrijp je de symboliek van de vijfpuntige ster?",
            "Hexagon": "Welke betekenis heeft de zeshoek in sacred geometry voor jou?",
            "Seed_of_Life": "Hoe bekend ben je met het Zaad des Levens patroon?",
            "Tree_of_Life": "Hoe diep is je kennis van de Boom des Levens?",
            "Egg_of_Life": "Wat weet je over het Ei des Levens symbool?",
            "Flower_of_Life": "Hoe goed ken je de Bloem des Levens geometrie?",
            "Fruit_of_Life": "Welke inzichten heb je over de Vrucht des Levens?",
            "Metatrons_Cube": "Hoe vertrouwd ben je met Metatron's Kubus?"
        };

        category.subcategories.forEach(element => {
            const questionDiv = this.createSliderQuestion(
                element,
                questions[element],
                category.scoring_range[0],
                category.scoring_range[1],
                'divine'
            );
            form.appendChild(questionDiv);
        });

        const buttonsDiv = this.createFormButtons('divine');
        form.appendChild(buttonsDiv);
    }

    generateKnowledgeForm() {
        const form = document.getElementById('knowledge-form');
        const category = this.assessmentData.categories.Tree_of_Life_Knowledge;
        
        const questions = {
            "Keter": "Hoe goed begrijp je Keter (Kroon) - de hoogste emanatie?",
            "Chokhmah": "Wat weet je over Chokhmah (Wijsheid) in de Kabbalah?",
            "Binah": "Hoe diep is je begrip van Binah (Begrip/Inzicht)?",
            "Chesed": "Welke kennis heb je over Chesed (Genade/Liefde)?",
            "Gevurah": "Hoe vertrouwd ben je met Gevurah (Kracht/Oordeel)?",
            "Tiferet": "Wat weet je over Tiferet (Schoonheid/Harmonie)?",
            "Netzach": "Hoe goed ken je Netzach (Overwinning/Eeuwigheid)?",
            "Hod": "Welke inzichten heb je over Hod (Glorie/Majesteit)?",
            "Yesod": "Hoe diep begrijp je Yesod (Fundament/Basis)?",
            "Malkuth": "Wat weet je over Malkuth (Koninkrijk/Manifestatie)?"
        };

        category.subcategories.forEach(sephira => {
            const questionDiv = this.createSliderQuestion(
                sephira,
                questions[sephira],
                category.scoring_range[0],
                category.scoring_range[1],
                'knowledge'
            );
            form.appendChild(questionDiv);
        });

        const buttonsDiv = this.createFormButtons('knowledge');
        form.appendChild(buttonsDiv);
    }

    generateExperienceForm() {
        const form = document.getElementById('experience-form');
        const category = this.assessmentData.categories.Tree_of_Life_Experience;
        
        const questions = {
            "Mystical_Unity": "In welke mate heb je eenheid met het universum ervaren?",
            "Transcendence_Time_Space": "Hoe vaak transcendeer je tijd en ruimte in meditatie?",
            "Ineffability": "Hoeveel mystieke ervaringen heb je die onbeschrijfbaar zijn?",
            "Sacred_Quality": "Hoe sterk ervaar je het heilige in je dagelijks leven?",
            "Noetic_Quality": "In welke mate krijg je directe spirituele kennis/inzichten?",
            "Positive_Mood": "Hoe positief en verheven voel je je meestal?"
        };

        category.subcategories.forEach(dimension => {
            const questionDiv = this.createSliderQuestion(
                dimension,
                questions[dimension],
                category.scoring_range[0],
                category.scoring_range[1],
                'experience'
            );
            form.appendChild(questionDiv);
        });

        const buttonsDiv = this.createFormButtons('experience');
        form.appendChild(buttonsDiv);
    }

    createSliderQuestion(name, question, min, max, category) {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question-group';
        questionDiv.innerHTML = `
            <h3 class="question-title">${name.replace(/_/g, ' ')}</h3>
            <p class="question-description">${question}</p>
            <div class="slider-labels">
                <span>${min}</span>
                <span>${max}</span>
            </div>
            <input type="range" class="form-control slider-input question-input" 
                   min="${min}" max="${max}" value="${min}" 
                   data-category="${category}" data-subcategory="${name}">
            <div class="slider-value">${min}</div>
        `;

        const slider = questionDiv.querySelector('.slider-input');
        const valueDisplay = questionDiv.querySelector('.slider-value');

        slider.addEventListener('input', (e) => {
            const value = parseInt(e.target.value);
            valueDisplay.textContent = value;
            this.updateScore(category, name, value);
        });

        return questionDiv;
    }

    createFormButtons(category) {
        const buttonsDiv = document.createElement('div');
        buttonsDiv.className = 'form-buttons';
        buttonsDiv.innerHTML = `
            <button class="btn btn--secondary save-btn" data-category="${category}">
                Opslaan en Doorgaan
            </button>
        `;

        const saveBtn = buttonsDiv.querySelector('.save-btn');
        saveBtn.addEventListener('click', () => {
            this.completeAssessment(category);
        });

        return buttonsDiv;
    }

    updateScore(category, subcategory, value) {
        this.scores[category][subcategory] = value;
        this.updateElementalScores();
        this.updateProgress();
    }

    completeAssessment(category) {
        this.completed[category] = true;
        this.updateAssessmentStatus(category);
        this.showSection('landing');
        this.updateProgress();
        this.checkResultsAvailability();
    }

    checkResultsAvailability() {
        // Show results button if at least one assessment is complete or if any scores exist
        const hasAnyScores = Object.values(this.scores).some(categoryScores => 
            Object.keys(categoryScores).length > 0
        );
        
        const viewResultsBtn = document.getElementById('view-results-btn');
        if (viewResultsBtn && hasAnyScores) {
            viewResultsBtn.style.display = 'block';
        }
    }

    updateAssessmentStatus(category) {
        const statusElement = document.getElementById(`status-${category}`);
        const cardElement = document.querySelector(`[data-category="${category}"]`);
        
        if (statusElement && cardElement) {
            statusElement.textContent = 'Voltooid';
            statusElement.style.color = 'var(--color-success)';
            cardElement.classList.add('completed');
        }
    }

    showElementalPreview() {
        const resultsPreview = document.getElementById('results-preview');
        if (resultsPreview) {
            resultsPreview.style.display = 'block';
            this.updateElementalScores();
        }
    }

    updateElementalScores() {
        const elementalScores = this.calculateElementalScores();
        const scoresContainer = document.getElementById('element-scores');
        
        if (scoresContainer) {
            scoresContainer.innerHTML = '';
            
            // Always show all elements, even with 0 scores
            const elements = ['Air', 'Earth', 'Fire', 'Water', 'Spirit'];
            elements.forEach(element => {
                const score = elementalScores[element] || 0;
                const scoreDiv = document.createElement('div');
                scoreDiv.className = `element-score element-score--${element.toLowerCase()}`;
                scoreDiv.innerHTML = `
                    <div class="element-score__name">${element}</div>
                    <div class="element-score__value">${score.toFixed(1)}</div>
                `;
                scoresContainer.appendChild(scoreDiv);
            });
        }
        
        this.checkResultsAvailability();
    }

    calculateElementalScores() {
        const elementTotals = { Air: 0, Earth: 0, Fire: 0, Water: 0, Spirit: 0 };
        const elementCounts = { Air: 0, Earth: 0, Fire: 0, Water: 0, Spirit: 0 };

        // Map category keys to assessment data keys
        const categoryMapping = {
            chakra: 'Chakra_Guide',
            divine: 'Divine_Elements', 
            knowledge: 'Tree_of_Life_Knowledge',
            experience: 'Tree_of_Life_Experience'
        };

        Object.entries(this.scores).forEach(([categoryKey, scores]) => {
            const categoryName = categoryMapping[categoryKey];
            if (!categoryName || !this.assessmentData.categories[categoryName]) return;
            
            const categoryData = this.assessmentData.categories[categoryName];
            
            Object.entries(scores).forEach(([subcategory, score]) => {
                const element = categoryData.elemental_mapping[subcategory];
                if (element && elementTotals.hasOwnProperty(element)) {
                    // Normalize score to 0-100 scale
                    const [min, max] = categoryData.scoring_range;
                    const normalizedScore = ((score - min) / (max - min)) * 100;
                    
                    elementTotals[element] += normalizedScore * categoryData.weight;
                    elementCounts[element] += categoryData.weight;
                }
            });
        });

        // Calculate averages
        const elementalScores = {};
        Object.keys(elementTotals).forEach(element => {
            if (elementCounts[element] > 0) {
                elementalScores[element] = elementTotals[element] / elementCounts[element];
            } else {
                elementalScores[element] = 0;
            }
        });

        return elementalScores;
    }

    updateProgress() {
        const completedCount = Object.values(this.completed).filter(status => status).length;
        const totalAssessments = Object.keys(this.completed).length;
        const progressPercentage = (completedCount / totalAssessments) * 100;
        
        const progressBar = document.getElementById('overall-progress');
        if (progressBar) {
            progressBar.style.width = `${progressPercentage}%`;
        }
    }

    showResults() {
        const elementalScores = this.calculateElementalScores();
        const scoreValues = Object.values(elementalScores).filter(score => score > 0);
        const averageScore = scoreValues.length > 0 ? 
            scoreValues.reduce((sum, score) => sum + score, 0) / scoreValues.length : 0;
        
        // Determine consciousness phase
        const phase = this.determineConsciousnessPhase(averageScore);
        
        // Update consciousness phase display
        const phaseElement = document.getElementById('consciousness-phase');
        if (phaseElement) {
            phaseElement.innerHTML = `
                <div class="phase-number">Fase ${phase.phase}</div>
                <div class="phase-name">${phase.name}</div>
                <div class="phase-description">${phase.description}</div>
                <div class="phase-score">Gemiddelde Score: ${averageScore.toFixed(1)}</div>
            `;
        }

        // Update detailed scores
        this.updateDetailedScores();
        
        // Update recommendations
        this.updateRecommendations(elementalScores);
        
        this.showSection('results');
    }

    determineConsciousnessPhase(averageScore) {
        const phases = this.assessmentData.consciousness_phases;
        
        if (averageScore <= 20) return phases[0];
        if (averageScore <= 40) return phases[1];
        if (averageScore <= 60) return phases[2];
        if (averageScore <= 80) return phases[3];
        return phases[4];
    }

    updateDetailedScores() {
        const detailedContainer = document.getElementById('detailed-scores');
        if (!detailedContainer) return;

        let html = '<h3>Gedetailleerde Scores</h3>';
        
        Object.entries(this.scores).forEach(([category, scores]) => {
            if (Object.keys(scores).length === 0) return;
            
            const categoryName = this.getCategoryDisplayName(category);
            const categoryAverage = Object.values(scores).reduce((sum, score) => sum + score, 0) / Object.keys(scores).length;
            
            html += `
                <div class="score-item">
                    <span>${categoryName}</span>
                    <span>${categoryAverage.toFixed(1)}</span>
                </div>
            `;
        });

        if (html === '<h3>Gedetailleerde Scores</h3>') {
            html += '<p>Nog geen scores beschikbaar.</p>';
        }

        detailedContainer.innerHTML = html;
    }

    updateRecommendations(elementalScores) {
        const recommendationsContainer = document.getElementById('recommendations');
        if (!recommendationsContainer) return;

        let html = '<h3>Persoonlijke Aanbevelingen</h3>';

        // Filter out zero scores and find weakest elements
        const nonZeroScores = Object.entries(elementalScores).filter(([,score]) => score > 0);
        
        if (nonZeroScores.length === 0) {
            html += '<p>Begin met de assessments om persoonlijke aanbevelingen te ontvangen.</p>';
        } else {
            const sortedElements = nonZeroScores.sort(([,a], [,b]) => a - b).slice(0, 2);
            
            sortedElements.forEach(([element, score]) => {
                const qualities = this.assessmentData.elements[element].qualities;
                html += `
                    <div class="recommendation-item">
                        <strong>${element} (${score.toFixed(1)})</strong><br>
                        Focus op: ${qualities.join(', ')}<br>
                        Overweeg meditatie en oefeningen gericht op ${element.toLowerCase()} element.
                    </div>
                `;
            });
        }

        recommendationsContainer.innerHTML = html;
    }

    getCategoryDisplayName(category) {
        const names = {
            chakra: 'Chakra Gids',
            divine: 'Goddelijke Elementen',
            knowledge: 'Boom des Levens Kennis',
            experience: 'Boom des Levens Ervaring'
        };
        return names[category] || category;
    }

    exportResults() {
        const elementalScores = this.calculateElementalScores();
        const scoreValues = Object.values(elementalScores).filter(score => score > 0);
        const averageScore = scoreValues.length > 0 ? 
            scoreValues.reduce((sum, score) => sum + score, 0) / scoreValues.length : 0;
        const phase = this.determineConsciousnessPhase(averageScore);

        const results = {
            timestamp: new Date().toISOString(),
            elementalScores,
            averageScore,
            consciousnessPhase: phase,
            detailedScores: this.scores,
            completed: this.completed
        };

        const dataStr = JSON.stringify(results, null, 2);
        const dataBlob = new Blob([dataStr], {type: 'application/json'});
        
        const link = document.createElement('a');
        link.href = URL.createObjectURL(dataBlob);
        link.download = `awaken-consciousness-results-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
    }

    restartAssessment() {
        if (confirm('Weet je zeker dat je de assessment opnieuw wilt starten? Alle voortgang gaat verloren.')) {
            this.scores = { chakra: {}, divine: {}, knowledge: {}, experience: {} };
            this.completed = { chakra: false, divine: false, knowledge: false, experience: false };
            
            // Reset UI
            document.querySelectorAll('.assessment-card').forEach(card => {
                card.classList.remove('completed');
            });
            
            document.querySelectorAll('.assessment-card__status').forEach(status => {
                status.textContent = 'Niet voltooid';
                status.style.color = '';
            });
            
            document.getElementById('view-results-btn').style.display = 'none';
            
            // Reset all sliders
            document.querySelectorAll('.slider-input').forEach(slider => {
                slider.value = slider.min;
                const valueDisplay = slider.parentElement.querySelector('.slider-value');
                if (valueDisplay) {
                    valueDisplay.textContent = slider.min;
                }
            });
            
            this.updateProgress();
            this.updateElementalScores();
            this.showSection('landing');
        }
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AwakeningConsciousness();
});