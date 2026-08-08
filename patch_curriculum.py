import json

# Define 5 quiz questions for each lesson in Phase 1, Phase 2, Phase 3, Phase 4
# and 20 interphasory questions per phase.

def make_q(qid, text, options, correct, exp):
    return {
        "id": qid,
        "question": text,
        "options": options,
        "correctIndex": correct,
        "explanation": exp
    }

# Function to generate 20 interphasory exam questions for Phase P
def make_interphasory_quiz(phase_num):
    qs = []
    if phase_num == 1:
        topics = [
            ("Qubits", "Physical realization of a qubit", "Electron spin state (Up / Down)", ["Transistor voltage", "Electron spin state (Up / Down)", "Hard drive magnet", "CPU clock"]),
            ("Qubits", "Dimension of single-qubit Hilbert space", "2 (ℂ²)", ["1", "2 (ℂ²)", "3", "4"]),
            ("Linear Algebra", "Representation of computational state |0⟩", "[1, 0]ᵀ", ["[0, 1]ᵀ", "[1, 0]ᵀ", "[1, 1]ᵀ", "[1/√2, 1/√2]ᵀ"]),
            ("Linear Algebra", "State produced by applying H on |0⟩", "|+⟩ = (|0⟩ + |1⟩)/√2", ["|1⟩", "|+⟩ = (|0⟩ + |1⟩)/√2", "|-⟩", "i|0⟩"]),
            ("Entanglement", "Maximally entangled Bell state |Φ⁺⟩", "(|00⟩ + |11⟩)/√2", ["(|00⟩ + |11⟩)/√2", "(|01⟩ + |10⟩)/√2", "|00⟩", "|11⟩"]),
            ("Entanglement", "Gate sequence to create Bell pair |Φ⁺⟩ from |00⟩", "H on q0, then CNOT(q0 -> q1)", ["H on q0, then CNOT(q0 -> q1)", "CNOT then H", "X then Z", "H on both"]),
            ("Quantum Gates", "Matrix property requiring U†U = I for logic gates", "Unitary (preserves norm)", ["Unitary (preserves norm)", "Hermitian", "Symmetric", "Diagonal"]),
            ("Quantum Gates", "Pauli-X gate operation on computational basis", "Flips |0⟩ to |1⟩ and |1⟩ to |0⟩", ["Flips |0⟩ to |1⟩ and |1⟩ to |0⟩", "Applies -1 phase", "Creates superposition", "Measures qubit"]),
            ("Rotations", "Continuous rotation gate around Y-axis", "Ry(θ)", ["Rx(θ)", "Ry(θ)", "Rz(θ)", "Hadamard"]),
            ("Rotations", "Role of rotation angles θ in QML circuits", "Trainable continuous weights updated via gradient descent", ["Trainable continuous weights updated via gradient descent", "Fixed constants", "Shot counters", "Clock frequency"]),
            ("Bloch Sphere", "Bloch sphere location for state |0⟩", "North Pole (θ = 0)", ["South Pole", "North Pole (θ = 0)", "Equator", "Center"]),
            ("Bloch Sphere", "Bloch vector length r for pure quantum states", "r = 1.0", ["r = 0", "r = 0.5", "r = 1.0", "r = 2.0"]),
            ("Measurement", "Post-measurement state after measuring state |0⟩", "Collapses to |0⟩", ["Collapses to |0⟩", "Stays in superposition", "Flips to |1⟩", "Becomes random"]),
            ("Measurement", "Rule mapping state amplitudes to outcome probabilities", "Born's Rule P(i) = |α_i|²", ["Born's Rule P(i) = |α_i|²", "Ohm's Law", "Chain Rule", "Bayes Theorem"]),
            ("Classical ML", "Function of non-linear activation σ(z) in neural layers", "Introduces non-linearity to represent complex patterns", ["Increases memory", "Introduces non-linearity to represent complex patterns", "Decreases speed", "Converts to binary"]),
            ("Classical ML", "Standard loss function for binary classification", "Binary Cross-Entropy (BCE)", ["Mean Squared Error", "Binary Cross-Entropy (BCE)", "Huber Loss", "L1 Loss"]),
            ("Optimization", "Quantum gradient rule replacing backpropagation on QPUs", "Parameter-Shift Rule", ["Parameter-Shift Rule", "Finite Differences", "Genetic Search", "Simulated Annealing"]),
            ("Optimization", "Direction of gradient vector ∇L(θ)", "Direction of steepest loss increase", ["Direction of steepest loss increase", "Direction of minimum loss", "Orthogonal to loss", "Zero vector"]),
            ("Hello World", "Expected measurement outcomes of H|0⟩ over 1000 shots", "~500 shots of 0 and ~500 shots of 1", ["1000 shots of 0", "~500 shots of 0 and ~500 shots of 1", "1000 shots of 1", "Random integers"]),
            ("Hello World", "Qiskit class representing quantum registers and gates", "QuantumCircuit", ["QuantumRegister", "QuantumCircuit", "AerSimulator", "QiskitRuntime"])
        ]
        for idx, (ch, qt, ans, opts) in enumerate(topics):
            qs.append(make_q(f"q-p1-exam-{idx+1}", f"[{ch}] {qt}?", opts, opts.index(ans), f"Correct answer is {ans} based on Phase 1 curriculum principles."))
    elif phase_num == 2:
        topics = [
            ("Circuits", "Unitary matrix dimension for n-qubit register", "2ⁿ x 2ⁿ", ["n x n", "2ⁿ x 2ⁿ", "2n x 2n", "n² x n²"]),
            ("Circuits", "Multi-qubit gate coupling two qubits for entanglement", "CNOT (CX)", ["Hadamard", "CNOT (CX)", "Pauli-X", "Phase S"]),
            ("Interference", "Mechanism eliminating incorrect solution state amplitudes", "Destructive Interference", ["Constructive Interference", "Destructive Interference", "Decoherence", "Measurement"]),
            ("Interference", "Result of HH|0⟩ gate sequence", "|0⟩ (Identity)", ["|1⟩", "|0⟩ (Identity)", "|+⟩", "|-⟩"]),
            ("Deutsch-Jozsa", "Oracle queries required by Deutsch-Jozsa algorithm", "Exactly 1 query", ["2ⁿ⁻¹ + 1", "n queries", "Exactly 1 query", "2ⁿ queries"]),
            ("Deutsch-Jozsa", "Problem solved by Deutsch-Jozsa algorithm", "Determining if black-box function is constant or balanced", ["Factoring integers", "Searching database", "Determining if black-box function is constant or balanced", "Sorting arrays"]),
            ("Grover Search", "Quantum search complexity for N unstructured database items", "O(√N)", ["O(N)", "O(N²)", "O(√N)", "O(log N)"]),
            ("Grover Search", "Grover diffusion operator operation", "Inversion about the mean amplitude", ["Inversion about the mean amplitude", "Phase flip", "Bit flip", "Measurement"]),
            ("QFT", "Gate complexity of Quantum Fourier Transform on n qubits", "O(n²)", ["O(2ⁿ)", "O(n²)", "O(n log n)", "O(n³)"]),
            ("QFT", "Classical FFT vs QFT complexity scaling advantage", "Exponential speedup O(n²) vs O(n 2ⁿ)", ["Linear speedup", "Exponential speedup O(n²) vs O(n 2ⁿ)", "No speedup", "Quadratic slowdown"]),
            ("Shor's Algorithm", "Problem reduced to factor prime integers in Shor's algorithm", "Modular Period Finding", ["Modular Period Finding", "Linear Regression", "Graph Coloring", "Matrix Inversion"]),
            ("Shor's Algorithm", "Impact of Shor's algorithm on classical cryptography", "Breaks RSA encryption in polynomial time", ["Breaks AES-256", "Breaks RSA encryption in polynomial time", "No impact", "Secures RSA"]),
            ("NISQ Era", "NISQ definition", "Noisy Intermediate-Scale Quantum (50-1000 qubits without fault tolerance)", ["New Integrated Silicon Quantum", "Noisy Intermediate-Scale Quantum (50-1000 qubits without fault tolerance)", "Non-Interfering Qubits", "Next-gen Scalable Quantum"]),
            ("NISQ Era", "Primary hardware limitation in NISQ devices", "Decoherence and gate error noise", ["Decoherence and gate error noise", "Slow clock speed", "Lack of memory", "High cost"]),
            ("Decoherence", "Physical timescale measured by T1 relaxation time", "Energy relaxation from state |1⟩ down to ground state |0⟩", ["Dephasing time", "Energy relaxation from state |1⟩ down to ground state |0⟩", "Gate execution time", "Measurement time"]),
            ("Decoherence", "Physical phenomenon measured by T2 dephasing time", "Decay of relative phase in superposition", ["Decay of relative phase in superposition", "Energy loss", "Heat generation", "Laser frequency"]),
            ("Error Mitigation", "Zero-Noise Extrapolation (ZNE) principle", "Scale noise levels (λ=1,3,5) and extrapolate expectation back to λ=0", ["Cool to absolute zero", "Scale noise levels (λ=1,3,5) and extrapolate expectation back to λ=0", "Increase shots", "Use classical GPU"]),
            ("Error Mitigation", "Difference between NISQ error mitigation and fault-tolerant QEC", "Error mitigation uses software post-processing without extra physical logical qubits", ["Error mitigation uses software post-processing without extra physical logical qubits", "They are identical", "QEC requires no extra qubits", "Mitigation only works on GPUs"]),
            ("Hardware Execution", "Role of Qiskit Transpiler before QPU job execution", "Compiles high-level circuits into native hardware gates for QPU topology", ["Translates to C++", "Compiles high-level circuits into native hardware gates for QPU topology", "Deletes gates", "Runs on GPU"]),
            ("Hardware Execution", "Function of QiskitRuntimeService", "Authentication and QPU cloud job queue submission", ["Authentication and QPU cloud job queue submission", "Circuit drawing", "Memory clearing", "Local simulation"])
        ]
        for idx, (ch, qt, ans, opts) in enumerate(topics):
            qs.append(make_q(f"q-p2-exam-{idx+1}", f"[{ch}] {qt}?", opts, opts.index(ans), f"Correct answer is {ans} based on Phase 2 curriculum principles."))
    elif phase_num == 3:
        topics = [
            ("PQCs", "Continuous parameters acting as QNN trainable weights", "Rotation angles θ in single-qubit gates", ["Qubit count", "Rotation angles θ in single-qubit gates", "Shot count", "QPU frequency"]),
            ("PQCs", "Ansatz in QML terminology", "Parameterized circuit structural template", ["Database model", "Parameterized circuit structural template", "Error correction code", "Cryogenic cooler"]),
            ("Data Embedding", "Encoding technique packing 2ⁿ feature values into n qubits", "Amplitude Encoding", ["Basis Encoding", "Angle Encoding", "Amplitude Encoding", "One-Hot Encoding"]),
            ("Data Embedding", "Angle encoding mapping strategy", "Maps classical features into single-qubit rotation angles", ["Maps classical features into single-qubit rotation angles", "Maps bitstrings to basis vectors", "Packs amplitudes", "Uses binary gates"]),
            ("VQE", "Mathematical principle guaranteeing ⟨H⟩ ≥ E₀ in VQE", "Rayleigh-Ritz Variational Principle", ["Heisenberg Uncertainty", "Rayleigh-Ritz Variational Principle", "No-Cloning Theorem", "Born Rule"]),
            ("VQE", "Role of classical optimizer in VQE hybrid loop", "Updates parameters θ to minimize energy expectation ⟨H⟩", ["Updates parameters θ to minimize energy expectation ⟨H⟩", "Measures qubits", "Cools dilution fridge", "Compiles Qiskit"]),
            ("QAOA", "Class of problems targeted by QAOA algorithm", "Combinatorial Optimization (e.g. Max-Cut, QUBO)", ["Linear Regression", "Combinatorial Optimization (e.g. Max-Cut, QUBO)", "Image generation", "Sorting"]),
            ("QAOA", "Function of Mixer Hamiltonian H_M = ∑ X_i in QAOA", "Drives quantum transitions and interference between candidate states", ["Drives quantum transitions and interference between candidate states", "Measures bits", "Encrypts data", "Decreases shots"]),
            ("QSVM", "Quantum Kernel Gram matrix formula", "K_ij = |⟨Φ(x_i)|Φ(x_j)⟩|²", ["K_ij = x_i * x_j", "K_ij = |⟨Φ(x_i)|Φ(x_j)⟩|²", "K_ij = x_i + x_j", "K_ij = 0"]),
            ("QSVM", "Node executing dual SVM quadratic optimization in QSVM", "Classical CPU / GPU", ["Physical QPU", "Classical CPU / GPU", "Quantum buffer", "Dilution fridge"]),
            ("QNNs", "Method for propagating gradients backward through quantum layers", "Parameter-Shift Rule", ["Classical Backprop", "Parameter-Shift Rule", "Random search", "Genetic algorithm"]),
            ("QNNs", "Benefit of embedding a PQC layer inside a classical neural network", "Combines classical feature extraction with quantum entangling power", ["Combines classical feature extraction with quantum entangling power", "Reduces GPU memory", "Eliminates training", "Deletes weights"]),
            ("Quantum Kernels", "Overlapping state fidelity value when x_i is identical to x_j", "1.0", ["0.0", "0.5", "1.0", "Infinity"]),
            ("Quantum Kernels", "ZZFeatureMap entangling mechanism", "2-qubit R_ZZ gates encoding non-classical feature correlations", ["2-qubit R_ZZ gates encoding non-classical feature correlations", "Single-qubit X gates", "Measurement gates", "Classical lookup"]),
            ("Parameter-Shift", "Parameter shift angle value s for Ry rotation gates", "s = π/2 (90 degrees)", ["s = 0.001", "s = π/2 (90 degrees)", "s = π", "s = 2π"]),
            ("Parameter-Shift", "Parameter-Shift analytic gradient formula for expectation f(θ)", "(f(θ + π/2) - f(θ - π/2)) / 2", ["(f(θ + ε) - f(θ)) / ε", "(f(θ + π/2) - f(θ - π/2)) / 2", "f'(θ) * θ", "0.0"]),
            ("Barren Plateaus", "Behavior of gradient variance in deep random PQCs as qubits increase", "Vanishes exponentially O(2⁻ⁿ)", ["Grows linearly", "Stays constant", "Vanishes exponentially O(2⁻ⁿ)", "Explodes"]),
            ("Barren Plateaus", "Effective strategy to mitigate barren plateaus in QML", "Using local cost functions and identity initialization", ["Using global cost functions", "Using local cost functions and identity initialization", "Increasing circuit depth", "Random weights"]),
            ("Hybrid Architectures", "Role of GPU tensor-network simulator in hybrid QML clusters", "Accelerating classical simulation of quantum circuits", ["Cryogenic cooling", "Accelerating classical simulation of quantum circuits", "QPU hardware control", "Storing qubits"]),
            ("Hybrid Architectures", "Triad of heterogeneous compute components in enterprise QML", "CPU (Orchestration) - GPU (Tensors) - QPU (Quantum Sampling)", ["CPU - RAM - Disk", "CPU (Orchestration) - GPU (Tensors) - QPU (Quantum Sampling)", "GPU - Monitor - Keyboard", "QPU - Laser - Mirror"])
        ]
        for idx, (ch, qt, ans, opts) in enumerate(topics):
            qs.append(make_q(f"q-p3-exam-{idx+1}", f"[{ch}] {qt}?", opts, opts.index(ans), f"Correct answer is {ans} based on Phase 3 curriculum principles."))
    elif phase_num == 4:
        topics = [
            ("QGANs", "Role of Quantum Generator G(θ_g) in QGAN architecture", "Maps latent states to candidate quantum probability distributions", ["Measures temperature", "Maps latent states to candidate quantum probability distributions", "Stores SQL logs", "Error correction"]),
            ("QGANs", "Adversarial minimax objective in QGAN training", "Generator attempts to fool Discriminator while Discriminator detects fakes", ["Generator attempts to fool Discriminator while Discriminator detects fakes", "Both minimize loss together", "No discriminator", "Classical random search"]),
            ("QCNNs", "Primary reason QCNNs are immune to Barren Plateaus", "O(log N) depth and localized quantum pooling blocks", ["No single-qubit gates", "O(log N) depth and localized quantum pooling blocks", "No measurement gates", "Runs on CPU"]),
            ("QCNNs", "Quantum pooling layer operation in QCNNs", "Measures subset of qubits to conditionally contract active register dimension", ["Measures subset of qubits to conditionally contract active register dimension", "Applies Hadamard", "Flips bits", "Doubles qubits"]),
            ("Quantum RL", "Method used by Quantum Q-Learning agent to compute action values", "Measuring expectation values of target observables on variational state", ["Reading lookup tables", "Measuring expectation values of target observables on variational state", "Counting wires", "Sorting arrays"]),
            ("Quantum RL", "Advantage of quantum state superposition in RL exploration policies", "Native sampling of multi-action superposition space for faster policy convergence", ["Native sampling of multi-action superposition space for faster policy convergence", "Zero memory usage", "Eliminates environment", "No rewards"]),
            ("Hardware-Efficient", "Primary benefit of Hardware-Efficient Ansatz (HEA)", "Restricts entangling gates to physical QPU topology, avoiding SWAP gates", ["Eliminates QPUs", "Restricts entangling gates to physical QPU topology, avoiding SWAP gates", "Infinite depth", "No rotation gates"]),
            ("Hardware-Efficient", "Typical 2-qubit gate native to IBM heavy-hex QPU architectures", "ECR or CNOT gate", ["Toffoli", "ECR or CNOT gate", "SWAP", "Fredkin"]),
            ("Quantum Chemistry", "Mapping transformation converting fermionic operators to Pauli operators", "Jordan-Wigner Transformation", ["Fourier Transform", "Jordan-Wigner Transformation", "Laplace Transform", "PCA"]),
            ("Quantum Chemistry", "Primary chemical property calculated via VQE molecular simulations", "Ground state potential energy surface E₀", ["Ground state potential energy surface E₀", "Molecular weight", "Boiling point", "pH level"]),
            ("Financial QML", "Speedup offered by Quantum Amplitude Estimation (QAE) for risk analysis", "Quadratic speedup O(1/ε) vs classical Monte Carlo O(1/ε²)", ["No speedup", "Quadratic speedup O(1/ε) vs classical Monte Carlo O(1/ε²)", "Exponential speedup", "Linear slowdown"]),
            ("Financial QML", "Mathematical model mapping portfolio optimization to QAOA", "QUBO (Quadratic Unconstrained Binary Optimization)", ["Linear Regression", "QUBO (Quadratic Unconstrained Binary Optimization)", "Neural network", "Decision tree"]),
            ("Benchmarking", "Metric measuring how closely an ansatz distribution matches Haar random ensemble", "Expressibility (KL divergence D_KL)", ["Code lines", "Expressibility (KL divergence D_KL)", "Clock speed", "Ping latency"]),
            ("Benchmarking", "Purpose of classical dequantization tests", "Verifying whether a QML model can be efficiently approximated by classical kernel methods", ["Verifying whether a QML model can be efficiently approximated by classical kernel methods", "Deleting quantum code", "Measuring temperature", "Testing GPU memory"]),
            ("Topological QC", "Quasi-particles used to store information non-locally in topological qubits", "Non-Abelian Anyons (Majorana Zero Modes)", ["Electrons", "Non-Abelian Anyons (Majorana Zero Modes)", "Photons", "Protons"]),
            ("Topological QC", "Why topological braid operations are immune to local noise perturbations", "Information is encoded in global spacetime braid topology", ["Operates at room temp", "Information is encoded in global spacetime braid topology", "No electricity needed", "Uses transistors"]),
            ("Cloud Deployment", "Function of asynchronous task queues (e.g. Redis / Celery) in cloud QML services", "Buffers client API requests to handle QPU execution queue latency and rate limits", ["Cools qubits", "Buffers client API requests to handle QPU execution queue latency and rate limits", "Compiles C++", "Generates randoms"]),
            ("Cloud Deployment", "Fallback mechanism when cloud QPU queue times exceed SLA thresholds", "Routing inference payloads to GPU simulator clusters (e.g. cuQuantum)", ["Routing inference payloads to GPU simulator clusters (e.g. cuQuantum)", "Throwing unhandled error", "Shutting down server", "Deleting user account"]),
            ("Capstone Project", "Key components of an end-to-end QML engineering capstone project", "Formulation, PQC design, Parameter-Shift training, QPU hardware execution, and web deployment", ["Writing pseudocode", "Formulation, PQC design, Parameter-Shift training, QPU hardware execution, and web deployment", "Deleting code", "Buying a QPU"]),
            ("Capstone Project", "Final step in completing the 4-Phase QML Academy Curriculum", "Deploying interactive QML web application and publishing execution results", ["Deploying interactive QML web application and publishing execution results", "Clearing browser cache", "Formatting hard drive", "Logging out"])
        ]
        for idx, (ch, qt, ans, opts) in enumerate(topics):
            qs.append(make_q(f"q-p4-exam-{idx+1}", f"[{ch}] {qt}?", opts, opts.index(ans), f"Correct answer is {ans} based on Phase 4 curriculum principles."))

    return qs

print("Quiz generator helper ready.")
