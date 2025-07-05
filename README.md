**Maximal & Co-Normal Product using Dominating Set, Burning Numbers, and Absorbance Tree in Optimizing Fuzzy Networks**

## Project Overview

This project  implements and analyzes advanced methods for optimizing fuzzy networks via three key concepts:

1. **Maximal & Co-Normal Product of Fuzzy Graphs**: Computation of both maximal and co-normal products of two fuzzy graphs under various connectivity constraints
2. **Dominating Set & Burning Numbers**: Identification of minimal dominating sets and computation of burning numbers to capture spread dynamics.
3. **Absorbance Tree Construction**: Generation of absorbance trees to measure and enhance network containment properties.

By integrating these approaches, the project delivers a toolkit for researchers and practitioners to model, analyze, and optimize fuzzy networks in applications such as decision-making, communication systems, and cryptography.

## Features

* **Co-Normal Product**: Algorithms to compute co-normal (conormal) products under the co-normal operation.
* **Maximal Product**: Algorithms to compute maximal products under $\odot$, $\otimes$, and other operations.
* **Dominating Set**: Exact and heuristic methods to find minimal dominating sets in fuzzy digraphs.
* **Burning Number**: Compute the burning number for a given fuzzy graph to model diffusion processes.
* **Absorbance Tree**: Build absorbance trees, measure absorbance efficiency, and derive network containment metrics.
* **Visualization**: Plot graph structures, dominating sets, and absorbance trees using Matplotlib and NetworkX.

## Prerequisites

* **Python**: Version 3.8 or higher
* **Core Libraries** (specified in `requirements.txt`):

  * `networkx>=2.5`  # Graph creation and manipulation
  * `matplotlib>=3.3.0`  # Plotting and animations (includes `FuncAnimation`)
  * `numpy>=1.18.0`  # Numerical computations
  * `pandas>=1.0.0`  # Data handling
  * `scipy>=1.4.0`  # Scientific utilities
  * `pillow>=8.0.0`  # Image handling backend for animations
  * `imageio-ffmpeg>=0.4.0`  # FFmpeg plugin for saving animations

**Note:** To generate and save animations via `FuncAnimation`, ensure that FFmpeg is installed on your system and available in your PATH. On Linux/macOS you can typically install it via your package manager (e.g., `apt`, `brew`), and on Windows by downloading from the [FFmpeg website](https://ffmpeg.org/).

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Shivangi1427/fuzzy-network-optimizer.git
   cd fuzzy-network-optimizer
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # on Linux/Mac
   venv\\Scripts\\activate   # on Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```text
fuzzy-network-optimizer/
├── src/
│   SCFD.py
├── requirements.txt
└── README.md
```

## Usage

### 1. Compute Maximal Product

```python
from src.maximal_product import maximal_product
H = maximal_product(G, G, method="odot")
```

## 2. Compute Co-Normal Product
from src.co_normal_product import co_normal_product
H_conormal = co_normal_product(G, G)

### 3. Find a Dominating Set

```python
from src.dominating_set import find_min_dominating_set
S = find_min_dominating_set(G)
```

### 4. Calculate Burning Number

```python
from src.burning_number import compute_burning_number
b = compute_burning_number(G)
```

### 5. Build Absorbance Tree

```python
from src.absorbance_tree import build_absorbance_tree
T = build_absorbance_tree(G, root=0)
```

### 6. Visualization

```python
from src.visualize import plot_graph, plot_tree
plot_graph(G, highlighted_nodes=S)
plot_tree(T)
```


## Contributing

Contributions are welcome! Please open an issue or pull request. Follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## References

1. Bonato, A., & Janssen, J. (2015). The burning number of a graph. *Discrete Mathematics*, 338(7), 1695–1700.
2. Meenakshi, J., Senbagamalar, A., & Kannan, A. (2023). Application of Intuitionistic Fuzzy Networks using Efficient Domination. *Fuzzy Logic Applications in Computer Science and Mathematics*, 213–232.
3. Kumaran, N., Meenakshi, A., Mahdal, M., Prakash, J.U., & Guras, R. (2023). Application of Fuzzy Network Using Efficient Domination.
4. Gourab, R.; Sen, A. Minimal arborescence. {\em arXiv preprint}, {\bf 2024}, arXiv:2401.13238.
