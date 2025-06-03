import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

# Define y-levels for different stages
input_y = 3
element_y = 2
phase_y = 1

# Colors for elements
element_colors = ['#1FB8CD', '#FFC185', '#ECEBD5', '#5D878F', '#D2BA4C']

# Input categories (top level)
input_categories = ["Chakra Guide", "Divine Elements", "Tree Knowledge", "Tree Experience"]
input_x = [1, 2, 3, 4]

# Add input category boxes
for i, cat in enumerate(input_categories):
    fig.add_trace(go.Scatter(
        x=[input_x[i]], 
        y=[input_y],
        mode='markers+text',
        marker=dict(size=40, color='#13343B'),
        text=[cat],
        textposition='middle center',
        textfont=dict(color='white', size=10),
        showlegend=False,
        name=cat
    ))

# Elements (middle level)
elements = ["Air", "Earth", "Fire", "Water", "Spirit"]
scores = [112.2, 75.8, 76.3, 106.6, 149.0]
element_x = [0.5, 1.5, 2.5, 3.5, 4.5]

# Add element boxes with scores
for i, (element, score, color) in enumerate(zip(elements, scores, element_colors)):
    fig.add_trace(go.Scatter(
        x=[element_x[i]], 
        y=[element_y],
        mode='markers+text',
        marker=dict(size=50, color=color),
        text=[f"{element}<br>{score}"],
        textposition='middle center',
        textfont=dict(size=9),
        showlegend=False,
        name=f"{element}: {score}"
    ))

# Phases (bottom level)
phases = ["Foundation", "Awakening", "Development", "Integration", "Mastery"]
phase_ranges = ["0-20", "20-40", "40-60", "60-80", "80-100"]
phase_x = [0.5, 1.5, 2.5, 3.5, 4.5]
phase_colors = ['#964325', '#944454', '#B4413C', '#DB4545', '#1FB8CD']

# Add phase boxes
for i, (phase, range_str, color) in enumerate(zip(phases, phase_ranges, phase_colors)):
    marker_size = 60 if i == 4 else 45  # Highlight current phase (Mastery)
    fig.add_trace(go.Scatter(
        x=[phase_x[i]], 
        y=[phase_y],
        mode='markers+text',
        marker=dict(size=marker_size, color=color),
        text=[f"{phase}<br>{range_str}"],
        textposition='middle center',
        textfont=dict(size=8, color='white'),
        showlegend=False,
        name=f"{phase} ({range_str})"
    ))

# Add flow lines from inputs to elements
for input_pos in input_x:
    for element_pos in element_x:
        fig.add_trace(go.Scatter(
            x=[input_pos, element_pos],
            y=[input_y-0.1, element_y+0.1],
            mode='lines',
            line=dict(color='lightgray', width=1),
            showlegend=False,
            hoverinfo='skip'
        ))

# Add flow lines from elements to phases
for element_pos in element_x:
    for phase_pos in phase_x:
        fig.add_trace(go.Scatter(
            x=[element_pos, phase_pos],
            y=[element_y-0.1, phase_y+0.1],
            mode='lines',
            line=dict(color='lightgray', width=1),
            showlegend=False,
            hoverinfo='skip'
        ))

# Current user indicator
fig.add_trace(go.Scatter(
    x=[4.5], 
    y=[0.7],
    mode='markers+text',
    marker=dict(size=20, color='gold', symbol='star'),
    text=["Current: 104.0"],
    textposition='bottom center',
    textfont=dict(size=10, color='gold'),
    showlegend=False,
    name="Current User Level"
))

# Update layout
fig.update_layout(
    title='Consciousness Flow System',
    xaxis=dict(range=[0, 5], showgrid=False, showticklabels=False),
    yaxis=dict(range=[0.5, 3.5], showgrid=False, showticklabels=False),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Save the chart
fig.write_image('consciousness_flow.png')