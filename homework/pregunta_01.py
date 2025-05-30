"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # 0. Crear carpeta de salida si no existe
    os.makedirs('files/plots', exist_ok=True)

    # 1. Leer datos desde CSV
    df = pd.read_csv('files/input/news.csv', index_col=0)

    # 2. Definir estilos (colores, orden de pintado y grosor de línea)
    colors = {
        'Television': 'dimgray',
        'Newspaper':  'grey',
        'Internet':   'tab:blue',
        'Radio':      'lightgrey',
    }
    zorder = {
        'Television': 1,
        'Newspaper':  1,
        'Internet':   2,
        'Radio':      1,
    }
    linewidths = {
        'Television': 2,
        'Newspaper':  2,
        'Internet':   4,
        'Radio':      2,
    }

    first_year = df.index[0]
    last_year  = df.index[-1]

    # 3. Crear figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

    # 4. Dibujar cada serie con marcadores en los extremos y etiquetas
    for col in df.columns:
        y = df[col]
        ax.plot(
            df.index, y,
            color=colors[col],
            linewidth=linewidths[col],
            zorder=zorder[col]
        )
        # marcador primer punto
        ax.scatter(first_year, y[first_year], color=colors[col], s=50, zorder=zorder[col])
        # marcador último punto
        ax.scatter(last_year,  y[last_year ], color=colors[col], s=50, zorder=zorder[col])
        # etiqueta inicial con nombre y valor
        ax.text(
            first_year - 0.2, y[first_year],
            f'{col} {y[first_year]}%',
            ha='right', va='center',
            color=colors[col]
        )
        # etiqueta final solo con valor
        ax.text(
            last_year + 0.2, y[last_year],
            f'{y[last_year]}%',
            ha='left', va='center',
            color=colors[col]
        )

    # 5. Título y subtítulo
    fig.suptitle(
        'How people get their news',
        fontsize=16, y=0.98
    )
    ax.set_title(
        'An increasing proportion cite the internet as their primary news source',
        fontsize=10, pad=10
    )

    # 6. Ajustes de ejes y spines
    for side in ['top', 'right', 'left']:
        ax.spines[side].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.index.astype(str))
    ax.set_yticks([])

    # 7. Guardar la figura
    plt.tight_layout()
    plt.savefig('files/plots/news.png')
    plt.close()
    
pregunta_01()