# Fenics---A-Decentralized-Federated-Learning-Simulator-for-Security-Evaluation

```markdown
# dfl_simulator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.8.0%2B-yellow.svg)
![tqdm](https://img.shields.io/badge/tqdm-4.64.0-brightgreen.svg)

**Distributed Federated Learning Simulator** (`dfl_simulator`) is a comprehensive tool designed to simulate and analyze distributed federated learning environments. It allows researchers and practitioners to experiment with various network topologies, participant selection strategies, and attack scenarios to evaluate the robustness and efficiency of federated learning algorithms.

---
    
## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Installing via `pip`](#installing-via-pip)
  - [Uninstallation](#uninstallation)
- [Configuration](#configuration)
  - [Parameters in `config.yaml`](#parameters-in-configyaml)
  - [Setting Up `topology.edgelist`](#setting-up-topologyedgelist)
- [Usage](#usage)
  - [Using the Phoenix Shell](#using-the-phoenix-shell)
  - [Running with Command-Line Arguments](#running-with-command-line-arguments)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---
    
## Features

- **Customizable Network Topologies:** Define and utilize custom network structures via edge list files.
- **Flexible Participant Selection:** Implement various client selection strategies based on data size or other metrics.
- **Support for Attacks:** Simulate adversarial attacks to assess the resilience of federated learning models.
- **Comprehensive Logging and Visualization:** Generate detailed logs and visual plots to analyze simulation results.
- **Scalable Simulations:** Handle simulations with varying numbers of nodes and complex network structures.
- **Real-Time Progress Monitoring:** Visualize simulation progress with an integrated loading bar using `tqdm`.

---
    
## Prerequisites

Before installing and using `dfl_simulator`, ensure that your system meets the following requirements:

- **Operating System:** Windows, macOS, or Linux.
- **Python Version:** Python 3.6 or higher.
- **Virtual Environment (Recommended):** It's advisable to use a virtual environment to manage dependencies.

---
    
## Installation
    
### Installing via `pip`

1. **Clone the Repository:**
    
    ```bash
    git clone https://github.com/yourusername/dfl_simulator.git
    cd dfl_simulator
    ```
    
2. **Create and Activate a Virtual Environment (Optional but Recommended):**
    
    - **Windows:**
    
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    
    - **Unix/Linux:**
    
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    
3. **Install Required Dependencies:**
    
    Ensure you have `pip` updated to the latest version:
    
    ```bash
    pip install --upgrade pip
    ```
    
4. **Install the Package in Editable Mode:**
    
    This allows you to modify the code without reinstalling the package each time.
    
    ```bash
    pip install -e .
    ```
    
    **Note:** The `setup.py` is configured to install all necessary dependencies, including `torch`, `numpy`, `psutil`, `colorama`, `pyfiglet`, and `tqdm`.
    
5. **Verify Installation:**
    
    After installation, the `phoenix` command-line tool should be available.
    
    ```bash
    phoenix --help
    ```
    
    **Expected Output:**
    
    ```
    Usage: phoenix [OPTIONS] COMMAND [ARGS]...
    
      Distributed Federated Learning Simulator
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      setup            Initialize the simulation environment with desired...
      run              Execute the simulation with the provided options.
      list_simulations List all available simulation configurations.
      parameters       Display all available simulation parameters and...
    ```
    
### Uninstallation
    
If you need to uninstall `dfl_simulator`, follow these steps:
    
1. **Deactivate the Virtual Environment (If Active):**
    
    ```bash
    deactivate
    ```
    
2. **Uninstall the Package:**
    
    ```bash
    pip uninstall dfl_simulator
    ```
    
3. **Remove the Virtual Environment (Optional):**
    
    If you created a virtual environment specifically for `dfl_simulator`, you can delete it:
    
    - **Windows:**
    
      ```bash
      rmdir /s /q venv
      ```
    
    - **Unix/Linux:**
    
      ```bash
      rm -rf venv
      ```
    
---
    
## Configuration
    
`dfl_simulator` uses a `config.yaml` file to manage simulation parameters. Proper configuration ensures that simulations run as intended with the desired settings.
    
### Parameters in `config.yaml`
    
Below is an explanation of the primary parameters you can configure:
    
```yaml
simulations:
  simulation1:
    rounds: 3                   # Number of training rounds
    epochs: 1                   # Number of epochs per round
    num_nodes: 5                # Total number of nodes in the simulation
    num_attackers: 0            # Number of attacker nodes
    attacker_nodes: []          # Specific nodes designated as attackers
    attacks: []                 # Types of attacks to simulate
    use_attackers: false        # Flag to enable or disable attacker simulation
    participation_rate: 0.6     # Fraction of nodes participating each round
    topology: fully_connected    # Network topology type (e.g., 'fully_connected', 'ring', etc.)
    topology_file: null         # Path to a custom topology edge list file
    max_attacks: null           # Maximum number of attacks an attacker can perform
    gossip_steps: 3             # Number of gossiping steps during aggregation
    protocol: gossip            # Aggregation protocol ('gossip' or 'neighboring')
    alpha: 0.5                  # Dirichlet distribution parameter for data partitioning
```
    
**Parameter Descriptions:**
    
- **`rounds`**: Total number of training rounds to execute.
- **`epochs`**: Number of training epochs each node performs per round.
- **`num_nodes`**: Total number of participating nodes in the simulation.
- **`num_attackers`**: Number of nodes designated as attackers.
- **`attacker_nodes`**: List of specific node IDs to act as attackers. Overrides `num_attackers` if provided.
- **`attacks`**: Types of attacks to simulate (e.g., 'delay', 'model_poisoning'). Define the attack strategies you want to test.
- **`use_attackers`**: Boolean flag to enable (`true`) or disable (`false`) attacker simulations.
- **`participation_rate`**: Fraction of nodes selected to participate in each round. For example, `0.6` means 60% of nodes are selected each round.
- **`topology`**: Defines the network topology. Common options include:
  - `fully_connected`: Every node is connected to every other node.
  - `ring`: Nodes are connected in a ring structure.
  - `star`: One central node connected to all other nodes.
  - `custom`: Use a custom topology defined in an edge list file.
- **`topology_file`**: Path to a custom topology edge list file. Required if `topology` is set to `custom`.
- **`max_attacks`**: Maximum number of attacks an attacker node can perform throughout the simulation.
- **`gossip_steps`**: Number of gossiping steps to perform during the aggregation phase.
- **`protocol`**: Aggregation protocol to use. Options:
  - `gossip`: Nodes exchange updates in a gossip manner.
  - `neighboring`: Nodes exchange updates with their immediate neighbors.
- **`alpha`**: Parameter for the Dirichlet distribution used in data partitioning among nodes.
    
### Setting Up `topology.edgelist`
    
When using a **custom network topology**, you need to define the connections between nodes in an edge list file. Here's how to set it up:
    
1. **Create the Edge List File:**
    
    - **Filename:** `topology.edgelist` (or any name of your choice)
    - **Format:** Each line represents an undirected edge between two nodes, specified by their node IDs separated by a space.
    
    **Example `topology.edgelist`:**
    
    ```
    0 1
    1 2
    1 4
    2 3
    3 5
    3 6
    4 5
    5 6
    5 7
    7 8
    8 9
    ```
    
    **Explanation:**
    - Node `0` is connected to Node `1`.
    - Node `1` is connected to Nodes `0`, `2`, and `4`.
    - And so on...
    
2. **Place the Edge List File:**
    
    Save the `topology.edgelist` file in a directory accessible to your project. For example, you can place it in the root directory of your project.
    
3. **Configure `config.yaml` to Use the Custom Topology:**
    
    Update the `config.yaml` to reference your custom edge list file.
    
    ```yaml
    simulations:
      simulation1:
        rounds: 3
        epochs: 1
        num_nodes: 10
        num_attackers: 0
        attacker_nodes: []
        attacks: []
        use_attackers: false
        participation_rate: 0.6
        topology: custom
        topology_file: path/to/your/topology.edgelist
        max_attacks: null
        gossip_steps: 3
        protocol: gossip
        alpha: 0.5
    ```
    
    **Replace `path/to/your/topology.edgelist` with the actual path to your edge list file.**
    
4. **Understanding the `topology.edgelist`:**
    
    - **Node IDs:** Ensure that node IDs in the edge list start from `0` and are consecutive integers up to `num_nodes - 1`.
    - **Undirected Edges:** Each connection is bidirectional. If you want Node `0` connected to Node `1`, you only need to specify `0 1`. There's no need to add `1 0`.
    
---
    
## Usage
    
`dfl_simulator` provides a command-line interface called **Phoenix Shell** to interact with the simulator. Below are instructions on how to set up and run simulations using both the Phoenix Shell and direct command-line arguments.
    
### Using the Phoenix Shell
    
1. **Launch the Phoenix Shell:**
    
    ```bash
    phoenix
    ```
    
    **Sample Output:**
    
    ```
       ____  _           _             
      |  _ \(_) __ _ ___| | _____ _ __ 
      | |_) | |/ _` / __| |/ / _ \ '__|
      |  __/| | (_| \__ \   <  __/ |   
      |_|   |_|\__,_|___/_|\_\___|_|   
                                        
    Welcome to Phoenix Shell! Type 'help' to see available commands.
    Phoenix> 
    ```
    
2. **Setup the Simulation Environment:**
    
    Use the `setup` command to initialize simulation parameters.
    
    - **Using Direct Parameters:**
    
      ```bash
      setup --rounds 3 --epochs 1 --topology fully_connected --participation_rate 0.6 --gossip_steps 3 --protocol gossip --num_nodes 5 --alpha 0.5
      ```
    
    - **Using a Configuration File:**
    
      ```bash
      setup --config config.yaml --simulation_name simulation1
      ```
    
      **Explanation:**
      - **`--config`**: Specifies the path to the `config.yaml` file.
      - **`--simulation_name`**: Identifies which simulation parameters to load from the configuration file.
    
    **Sample Output:**
    
    ```
    Parsed Arguments:
    Rounds: 3
    Epochs: 1
    Topology: fully_connected
    Participation rate: 0.6
    Gossip steps: 3
    Protocol: gossip
    Number of nodes: 5
    Alpha: 0.5
    Created directory: results
    Logging is configured.
    Setup completed successfully.
    ```
    
3. **Run the Simulation:**
    
    After setup, execute the simulation using the `run` command.
    
    ```bash
    run
    ```
    
    **Sample Output:**
    
    ```
    Final Simulation Arguments:
    Rounds: 3
    Epochs: 1
    Topology: fully_connected
    Participation rate: 0.6
    Gossip steps: 3
    Protocol: gossip
    Num nodes: 5
    Alpha: 0.5
    
    Starting simulation...
    Simulation Progress: 100%|██████████████████████████████████████████████████████████| 3/3 [00:01<00:00, 2.50round/s, CPU Usage: 55%]
    
    Simulation completed successfully. Check the 'results' directory for outputs.
    ```
    
    **Explanation:**
    - **Progress Bar:** A real-time progress bar displays the simulation's progress, showing the percentage completed and the latest CPU usage.
    - **Logs and Plots:** Detailed logs and visual plots are saved in the `results` directory.
    
4. **Exit the Phoenix Shell:**
    
    Use the `exit` or `quit` command to exit.
    
    ```bash
    exit
    ```
    
    **Sample Output:**
    
    ```
    Exiting Phoenix. Goodbye!
    ```
    
### Running with Command-Line Arguments
    
Alternatively, you can run simulations directly without entering the Phoenix Shell by passing commands as arguments. However, the Phoenix Shell is the recommended way to interact with `dfl_simulator` for its interactive capabilities.
    
```bash
phoenix setup --config config.yaml --simulation_name simulation1 && phoenix run
```
    
**Note:** This approach sequentially executes the `setup` and `run` commands.

---
    
## Example
    
Here's a step-by-step example to demonstrate how to set up and run a simulation using a custom network topology.
    
### 1. Define a Custom Topology
    
Create a file named `topology.edgelist` with the following content:
    
```
0 1
1 2
1 4
2 3
3 5
3 6
4 5
5 6
5 7
7 8
8 9
```
    
**Explanation:**
    
- **Nodes:** 0 through 9 (total of 10 nodes).
- **Edges:** Defines the connections between nodes. For example, Node `0` is connected to Node `1`, Node `1` is connected to Nodes `0`, `2`, and `4`, etc.
    
### 2. Configure `config.yaml`
    
Update your `config.yaml` to include the custom topology.
    
```yaml
simulations:
  simulation1:
    rounds: 5
    epochs: 2
    num_nodes: 10
    num_attackers: 2
    attacker_nodes: [3, 7]
    attacks: ['model_poisoning', 'delay']
    use_attackers: true
    participation_rate: 0.6
    topology: custom
    topology_file: path/to/topology.edgelist
    max_attacks: 3
    gossip_steps: 4
    protocol: gossip
    alpha: 0.5
```
    
**Replace `path/to/topology.edgelist` with the actual path to your `topology.edgelist` file.**
    
### 3. Run the Simulation
    
1. **Launch the Phoenix Shell:**
    
    ```bash
    phoenix
    ```
    
2. **Setup the Simulation Using `config.yaml`:**
    
    ```bash
    setup --config config.yaml --simulation_name simulation1
    ```
    
3. **Execute the Simulation:**
    
    ```bash
    run
    ```
    
4. **Monitor Outputs:**
    
    - **Logs:** Check the `results/simulation.log` file for detailed logs.
    - **Plots:** Generated plots will be saved as PNG files in the `results` directory.
    - **Simulation Results:** Ensure that attacker nodes (3 and 7) perform their designated attacks, and observe how the network handles these adversarial behaviors.
    
---
    
## Contributing
    
Contributions are welcome! If you'd like to enhance `dfl_simulator`, please follow these steps:
    
1. **Fork the Repository:**
    
    Click the "Fork" button on the repository's GitHub page to create your own copy.
    
2. **Clone Your Fork:**
    
    ```bash
    git clone https://github.com/yourusername/dfl_simulator.git
    cd dfl_simulator
    ```
    
3. **Create a New Branch:**
    
    ```bash
    git checkout -b feature/your-feature-name
    ```
    
4. **Make Your Changes:**
    
    Implement your desired features or fixes.
    
5. **Commit Your Changes:**
    
    ```bash
    git add .
    git commit -m "Add feature XYZ"
    ```
    
6. **Push to Your Fork:**
    
    ```bash
    git push origin feature/your-feature-name
    ```
    
7. **Create a Pull Request:**
    
    Navigate to the original repository and create a pull request from your forked repository.
    
---
    
## License
    
This project is licensed under the [MIT License](LICENSE).
    
---
    
## Acknowledgments
    
- **PyTorch:** For providing a robust framework for deep learning.
- **Colorama & Pyfiglet:** For enhancing the command-line interface aesthetics.
- **tqdm:** For providing the progress bar functionality that enhances user experience.
- **OpenAI's ChatGPT:** For assisting in the development and troubleshooting of this simulator.
    
---
    
## Contact
    
For any questions or feedback, please contact [Shubham Saha](mailto:shuvsaha7@gmail.com) or [Sifat Nawrin Nova](mailto:nawrinnova04@gmail.com).

---
```
