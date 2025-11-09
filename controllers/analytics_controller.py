import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from typing import Dict, List

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def load_dataset() -> pd.DataFrame:
    """Carga el dataset de razas de perros"""
    return pd.read_csv('data/dog_breeds_dataset.csv')

def plot_to_base64(fig) -> str:
    """Convierte una figura de matplotlib a base64 para embeber en HTML"""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close(fig)
    return f"data:image/png;base64,{img_base64}"

def generate_feature_distributions() -> str:
    """Histogramas de distribución de características"""
    df = load_dataset()
    
    features = ['energy_level', 'trainability', 'good_with_kids', 'exercise_needs', 
                'barking_tendency', 'grooming_needs', 'apartment_friendly', 
                'good_alone', 'watchdog_ability']
    
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    fig.suptitle('Distribución de Características de las Razas', fontsize=16, fontweight='bold')
    
    # Crear paleta de colores con suficientes colores
    colors = sns.color_palette("husl", len(features))
    
    for idx, feature in enumerate(features):
        ax = axes[idx // 3, idx % 3]
        counts = df[feature].value_counts().sort_index()
        
        ax.bar(counts.index, counts.values, color=colors[idx], alpha=0.7)
        ax.set_xlabel(feature.replace('_', ' ').title(), fontsize=10)
        ax.set_ylabel('Número de Razas', fontsize=10)
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.grid(axis='y', alpha=0.3)
        
        # Añadir valores sobre las barras
        for i, v in enumerate(counts.values):
            ax.text(counts.index[i], v + 1, str(v), ha='center', fontsize=8)
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_correlation_heatmap() -> str:
    """Matriz de correlación entre características"""
    df = load_dataset()
    
    features = ['energy_level', 'trainability', 'good_with_kids', 'exercise_needs', 
                'barking_tendency', 'grooming_needs', 'apartment_friendly', 
                'good_alone', 'watchdog_ability']
    
    correlation = df[features].corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
    
    ax.set_title('Matriz de Correlación entre Características', fontsize=14, fontweight='bold', pad=20)
    
    # Rotar etiquetas
    labels = [label.get_text().replace('_', ' ').title() for label in ax.get_xticklabels()]
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels(labels, rotation=0)
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_size_distribution() -> str:
    """Gráfico de pastel de distribución de tamaños"""
    df = load_dataset()
    
    size_counts = df['size'].value_counts().sort_index()
    
    # Labels dinámicos basados en los valores que existen
    size_labels_map = {
        1: 'Muy Pequeño',
        2: 'Pequeño',
        3: 'Mediano',
        4: 'Grande',
        5: 'Muy Grande'
    }
    
    size_labels = [size_labels_map[size] for size in size_counts.index]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#FFA07A', '#4ECDC4', '#45B7D1', '#95E1D3']
    # Usar solo los colores necesarios
    used_colors = [colors[i-1] for i in size_counts.index]
    
    explode = tuple([0.05] * len(size_counts))
    
    _, _, autotexts = ax.pie(size_counts.values, labels=size_labels,
                                        autopct='%1.1f%%', startangle=90,
                                        colors=used_colors, explode=explode,
                                        textprops={'fontsize': 12})    # Mejorar estilo
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(14)
    
    ax.set_title('Distribución de Tamaños de Razas\n(195 Razas AKC)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Añadir leyenda con conteos
    legend_labels = [f'{label}: {count} razas' for label, count in zip(size_labels, size_counts.values)]
    ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_top_breeds_chart(feature: str, top_n: int = 10) -> str:
    """Gráfico de barras horizontales de top razas por característica"""
    df = load_dataset()
    
    top_breeds = df.nlargest(top_n, feature)[['breed', feature]].sort_values(feature)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.viridis(top_breeds[feature] / 5.0)
    bars = ax.barh(top_breeds['breed'], top_breeds[feature], color=colors)
    
    ax.set_xlabel('Nivel (1-5)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Raza', fontsize=12, fontweight='bold')
    ax.set_title(f'Top {top_n} Razas - {feature.replace("_", " ").title()}', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 5.5)
    ax.grid(axis='x', alpha=0.3)
    
    # Añadir valores al final de las barras
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{width:.1f}', ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_radar_chart() -> str:
    """Radar chart comparando razas populares"""
    df = load_dataset()
    
    # Seleccionar 4 razas populares (nombres exactos del dataset)
    breeds_to_compare = [
        'Retrievers (Labrador)',
        'German Shepherd Dogs', 
        'Bulldogs',
        'Yorkshire Terriers'
    ]
    features = ['energy_level', 'trainability', 'good_with_kids', 
                'exercise_needs', 'barking_tendency', 'watchdog_ability']
    
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
    
    angles = [n / float(len(features)) * 2 * 3.14159 for n in range(len(features))]
    angles += angles[:1]
    
    ax.set_theta_offset(3.14159 / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([f.replace('_', ' ').title() for f in features], fontsize=10)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
    ax.grid(True)
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    
    for idx, breed in enumerate(breeds_to_compare):
        breed_data = df[df['breed'] == breed][features].values.flatten().tolist()
        breed_data += breed_data[:1]
        ax.plot(angles, breed_data, 'o-', linewidth=2, label=breed, color=colors[idx])
        ax.fill(angles, breed_data, alpha=0.15, color=colors[idx])
    
    ax.set_title('Comparación de Perfiles de Razas Populares', 
                 fontsize=14, fontweight='bold', y=1.08)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_scatter_plot() -> str:
    """Scatter plot: Energy vs Trainability con tamaño por size"""
    df = load_dataset()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    size_map = {1: 100, 2: 200, 3: 300}
    sizes = df['size'].map(size_map)
    
    scatter = ax.scatter(df['energy_level'], df['trainability'], 
                        s=sizes, alpha=0.6, c=df['good_with_kids'], 
                        cmap='viridis', edgecolors='black', linewidth=0.5)
    
    ax.set_xlabel('Nivel de Energía', fontsize=12, fontweight='bold')
    ax.set_ylabel('Entrenabilidad', fontsize=12, fontweight='bold')
    ax.set_title('Energía vs Entrenabilidad (color=bueno con niños, tamaño=size)', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.grid(alpha=0.3)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Bueno con Niños', fontsize=10)
    
    # Leyenda de tamaños
    for size_val, marker_size in size_map.items():
        size_label = ['Pequeño', 'Mediano', 'Grande'][size_val - 1]
        ax.scatter([], [], s=marker_size, c='gray', alpha=0.6, 
                  edgecolors='black', label=size_label)
    
    ax.legend(title='Tamaño', loc='upper left', fontsize=10)
    
    plt.tight_layout()
    return plot_to_base64(fig)

def generate_pair_plot() -> str:
    """Genera un Pair Plot (matriz de dispersión) similar al de Iris"""
    df = load_dataset()
    
    # Seleccionar las características más importantes para visualizar
    features = ['energy_level', 'trainability', 'exercise_needs', 'good_with_kids']
    
    # Crear categorías de tamaño para colorear
    size_labels = ['Pequeño', 'Mediano', 'Grande']
    df['size_category'] = pd.cut(df['size'], bins=[0, 2, 3, 5], labels=size_labels)
    
    # Crear el pair plot
    pairplot_data = df[features + ['size_category']].copy()
    
    # Crear el pairplot
    g = sns.pairplot(pairplot_data, 
                     hue='size_category',
                     palette={size_labels[0]: '#FF6B35', size_labels[1]: '#8B4513', size_labels[2]: '#654321'},
                     diag_kind='hist',
                     plot_kws={'alpha': 0.6, 's': 50},
                     diag_kws={'alpha': 0.7, 'bins': 5})
    
    g.fig.suptitle('Matriz de Relaciones entre Características Principales', 
                   fontsize=18, fontweight='bold', y=1.0)
    
    # Ajustar etiquetas
    for ax in g.axes.flatten():
        ax.set_xlabel(ax.get_xlabel().replace('_', ' ').title(), fontsize=10)
        ax.set_ylabel(ax.get_ylabel().replace('_', ' ').title(), fontsize=10)
    
    # Convertir a base64
    buf = io.BytesIO()
    g.fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close(g.fig)
    
    return f"data:image/png;base64,{img_base64}"

def generate_all_charts() -> Dict[str, str]:
    """Genera todos los gráficos y retorna diccionario con imágenes base64"""
    return {
        'distributions': generate_feature_distributions(),
        'correlation': generate_correlation_heatmap(),
        'size_pie': generate_size_distribution(),
        'top_energy': generate_top_breeds_chart('energy_level', 10),
        'top_trainability': generate_top_breeds_chart('trainability', 10),
        'scatter': generate_scatter_plot(),
        'pair_plot': generate_pair_plot()  # Nuevo: Pair Plot como en Iris
    }

def get_dataset_statistics() -> Dict:
    """Obtiene estadísticas descriptivas del dataset"""
    df = load_dataset()
    
    features = ['energy_level', 'trainability', 'good_with_kids', 'exercise_needs', 
                'barking_tendency', 'grooming_needs', 'apartment_friendly', 
                'good_alone', 'watchdog_ability']
    
    stats = df[features].describe().round(2).to_dict()
    
    return {
        'total_breeds': len(df),
        'statistics': stats,
        'size_distribution': df['size'].value_counts().to_dict()
    }
