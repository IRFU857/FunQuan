import json

# Python script to build src/data/curriculumData.ts with:
# 1. 5 questions for every lesson
# 2. 20 interphasory questions for every phase
# 3. Updated MOCK_LEADERBOARD with phaseScores

def q(qid, question, options, correct_idx, explanation):
    return {
        "id": qid,
        "question": question,
        "options": options,
        "correctIndex": correct_idx,
        "explanation": explanation
    }

# Phase 1 Quiz Questions (5 per lesson)
p1_quizzes = {
    "lesson-1-1": [
        q("q-1-1-1", "What physical property can be used as a natural realization of a qubit?",
          ["Transistor voltage levels", "Electron spin state (Up / Down)", "Hard drive magnetic domains", "CPU clock cycles"], 1,
          "Physical two-level quantum systems like electron spin (up/down) or photon polarization serve as physical implementations of qubits."),
        q("q-1-1-2", "In Dirac bra-ket notation, what vector space does a qubit state |ψ⟩ reside in?",
          ["Real 3D space ℝ³", "Two-dimensional complex Hilbert Space ℂ²", "1D scalar space", "Quaternionic space"], 1,
          "A single qubit state |ψ⟩ = α|0⟩ + β|1⟩ is a normalized vector residing in ℂ² Hilbert space."),
        q("q-1-1-3", "What condition must the complex probability amplitudes α and β satisfy for a normalized qubit?",
          ["α + β = 1", "|α|² + |β|² = 1", "α * β = 0", "|α| + |β| = 2"], 1,
          "The normalization condition requires total probability sum |α|² + |β|² = 1."),
        q("q-1-1-4", "Which physical qubit technology operates inside dilution refrigerators near 15 millikelvin?",
          ["Photonic circuits", "Superconducting Transmon circuits", "Acoustic resonators", "Optocouplers"], 1,
          "Superconducting transmon circuits require dilution refrigerators (~15 mK) to eliminate thermal excitations."),
        q("q-1-1-5", "Unlike a classical bit that is strictly 0 or 1, what allows a qubit to exist in a continuous combination of 0 and 1?",
          ["Superposition", "Semiconductor doping", "Thermal noise", "Clock frequency"], 0,
          "Quantum superposition allows a qubit to hold linear combinations α|0⟩ + β|1⟩ prior to measurement.")
    ],
    "lesson-1-2": [
        q("q-1-2-1", "What is the linear algebra representation of the quantum computational basis state |0⟩?",
          ["[0, 1]ᵀ", "[1, 0]ᵀ", "[1, 1]ᵀ", "[1/√2, 1/√2]ᵀ"], 1,
          "The state |0⟩ is represented by column vector [1, 0]ᵀ in computational basis."),
        q("q-1-2-2", "What is the Hermitian conjugate (ket to bra) operation applied to |ψ⟩ = [a, b]ᵀ?",
          ["⟨ψ| = [a*, b*]", "⟨ψ| = [a, b]", "⟨ψ| = [a*, -b*]", "⟨ψ| = [b*, a*]"], 0,
          "The bra vector ⟨ψ| is the conjugate transpose (row vector [a*, b*]) of ket |ψ⟩."),
        q("q-1-2-3", "What does the inner product ⟨φ|ψ⟩ evaluate to if states |φ⟩ and |ψ⟩ are orthogonal?",
          ["1.0", "0.0", "-1.0", "i"], 1,
          "Orthogonal quantum state vectors have an inner product ⟨φ|ψ⟩ = 0."),
        q("q-1-2-4", "What state is produced when a Hadamard gate H acts on state |0⟩?",
          ["|1⟩", "|+⟩ = (|0⟩ + |1⟩)/√2", "|-⟩ = (|0⟩ - |1⟩)/√2", "i|0⟩"], 1,
          "H|0⟩ creates the equal superposition state |+⟩ = (|0⟩ + |1⟩)/√2."),
        q("q-1-2-5", "What is the result of the inner product ⟨+|–⟩ between superposition states |+⟩ and |–⟩?",
          ["0.0", "1.0", "0.5", "0.25"], 0,
          "States |+⟩ and |–⟩ form an orthonormal basis, so ⟨+|–⟩ = 0.")
    ],
    "lesson-1-3": [
        q("q-1-3-1", "Which state represents the maximally entangled Bell pair |Φ⁺⟩?",
          ["(|00⟩ + |11⟩)/√2", "(|01⟩ + |10⟩)/√2", "(|00⟩ - |11⟩)/√2", "|00⟩"], 0,
          "The Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2 is maximally entangled."),
        q("q-1-3-2", "Can a product state |ψ⟩ = |a⟩ ⊗ |b⟩ be an entangled state?",
          ["Yes, always", "No, product states are strictly unentangled (separable)", "Only on Tuesdays", "Only if measured"], 1,
          "Product states are separable and contain zero quantum entanglement between subsystems."),
        q("q-1-3-3", "What happens to qubit 1 when qubit 0 of Bell pair (|00⟩ + |11⟩)/√2 is measured and collapses to |1⟩?",
          ["Qubit 1 remains in superposition", "Qubit 1 collapses to |1⟩ instantly", "Qubit 1 collapses to |0⟩", "Qubit 1 is destroyed"], 1,
          "Entanglement correlates the states, so measuring qubit 0 as |1⟩ forces qubit 1 to collapse to |1⟩."),
        q("q-1-3-4", "Which sequence of gates creates the Bell state |Φ⁺⟩ from initial state |00⟩?",
          ["H on q0, then CNOT(q0 -> q1)", "CNOT(q0 -> q1), then H on q0", "X on q0, then Z on q1", "H on both q0 and q1"], 0,
          "Hadamard on q0 creates (|0⟩+|1⟩)|0⟩, and CNOT entangles it into (|00⟩+|11⟩)/√2."),
        q("q-1-3-5", "What theorem proves that quantum entanglement cannot be used for faster-than-light communication?",
          ["No-Cloning Theorem", "No-Communication Theorem", "Born Rule", "Heisenberg Uncertainty Principle"], 1,
          "The No-Communication theorem proves entanglement cannot transmit classical messages faster than light.")
    ],
    "lesson-1-4": [
        q("q-1-4-1", "Which gate performs a bit-flip operation analogous to a classical NOT gate?",
          ["Hadamard gate (H)", "Pauli-X gate (X)", "Pauli-Z gate (Z)", "Phase gate (S)"], 1,
          "The Pauli-X gate flips |0⟩ to |1⟩ and |1⟩ to |0⟩."),
        q("q-1-4-2", "What is the matrix representation of the Pauli-Z gate?",
          ["[[0, 1], [1, 0]]", "[[1, 0], [0, -1]]", "[[0, -i], [i, 0]]", "[[1, 0], [0, 1]]"], 1,
          "Pauli-Z matrix is [[1, 0], [0, -1]], leaving |0⟩ unchanged and applying -1 phase to |1⟩."),
        q("q-1-4-3", "Why must all valid quantum logic gate transformations be unitary (U†U = I)?",
          ["To preserve probability norm and ensure reversibility", "To increase clock speed", "To generate heat", "To make matrices symmetric"], 0,
          "Unitary transformations preserve quantum state norm (total probability = 1) and are reversible."),
        q("q-1-4-4", "What is the result of applying Pauli-X twice consecutively (X X |0⟩)?",
          ["|1⟩", "|0⟩", "|+⟩", "|-⟩"], 1,
          "Since X² = I (Identity), applying X twice returns the original state |0⟩."),
        q("q-1-4-5", "Which gate is known as the controlled-NOT gate with 2 qubits?",
          ["Toffoli", "CNOT (CX)", "SWAP", "CZ"], 1,
          "The CNOT (CX) gate flips target qubit if and only if control qubit is in state |1⟩.")
    ],
    "lesson-1-5": [
        q("q-1-5-1", "What matrix formula defines the continuous single-qubit rotation Ry(θ)?",
          ["[[cos(θ/2), -sin(θ/2)], [sin(θ/2), cos(θ/2)]]", "[[1, 0], [0, e^(iθ)]]", "[[e^(iθ), 0], [0, e^(-iθ)]]", "[[0, θ], [θ, 0]]"], 0,
          "Ry(θ) = [[cos(θ/2), -sin(θ/2)], [sin(θ/2), cos(θ/2)]]."),
        q("q-1-5-2", "Why are parameterized rotation gates like Ry(θ) fundamental to Quantum Machine Learning?",
          ["They are cheaper to fabricate", "Continuous angles θ act as trainable weights updated during gradient descent", "They delete qubit states", "They destroy superposition"], 1,
          "Continuous rotation angles θ serve as trainable weight parameters in Parameterized Quantum Circuits (PQCs)."),
        q("q-1-5-3", "What rotation angle θ in Ry(θ) transforms state |0⟩ into state |1⟩?",
          ["θ = π/2", "θ = π", "θ = 2π", "θ = π/4"], 1,
          "Ry(π)|0⟩ = [cos(π/2), sin(π/2)]ᵀ = [0, 1]ᵀ = |1⟩."),
        q("q-1-5-4", "What rotation angle θ in Ry(θ) transforms state |0⟩ into superposition state |+⟩?",
          ["θ = π/2", "θ = π", "θ = 2π", "θ = π/4"], 0,
          "Ry(π/2)|0⟩ = [cos(π/4), sin(π/4)]ᵀ = [1/√2, 1/√2]ᵀ = |+⟩."),
        q("q-1-5-5", "Which single-qubit gate applies a parameterized phase rotation around the Z-axis?",
          ["Rx(θ)", "Ry(θ)", "Rz(θ)", "Hadamard"], 2,
          "Rz(θ) applies phase rotation diag(e^(-iθ/2), e^(iθ/2)) around the Bloch sphere Z-axis.")
    ],
    "lesson-1-6": [
        q("q-1-6-1", "Which coordinates on the Bloch sphere correspond to the state |0⟩?",
          ["South Pole (θ = π)", "North Pole (θ = 0)", "Equator (θ = π/2, ϕ = 0)", "Center of the sphere"], 1,
          "When θ = 0, cos(0) = 1 and sin(0) = 0, placing the state vector at the North Pole (|0⟩)."),
        q("q-1-6-2", "Which state lies on the positive X-axis on the equator of the Bloch sphere?",
          ["|0⟩", "|1⟩", "|+⟩ = (|0⟩ + |1⟩)/√2", "|+i⟩ = (|0⟩ + i|1⟩)/√2"], 2,
          "State |+⟩ sits at polar angle θ = π/2, azimuthal angle ϕ = 0 on the X-axis."),
        q("q-1-6-3", "What is the length r of the Bloch vector (x, y, z) for any pure quantum state?",
          ["r = 0.5", "r = 1.0", "r = 2.0", "r = 0.0"], 1,
          "Pure quantum states lie on the surface of the unit Bloch sphere with vector length r = 1."),
        q("q-1-6-4", "Where do mixed (decohered) quantum states lie in the Bloch sphere representation?",
          ["Outside the sphere (r > 1)", "Inside the interior of the sphere (r < 1)", "Only at the poles", "On the equator only"], 1,
          "Mixed statistical state mixtures reside inside the interior of the Bloch ball with radius r < 1."),
        q("q-1-6-5", "Geometrically, what does a single-qubit quantum gate operation correspond to on the Bloch sphere?",
          ["A 3D rotation of the state vector", "Scaling the sphere to infinity", "Translating the sphere origin", "A projection to a 2D line"], 0,
          "Unitary single-qubit gates map to rigid 3D spatial rotations of the Bloch vector on the unit sphere.")
    ],
    "lesson-1-7": [
        q("q-1-7-1", "What happens if you measure the exact same qubit immediately a second time after it collapses to |0⟩?",
          ["It returns to superposition", "It yields |0⟩ with 100% certainty", "It collapses to |1⟩", "The qubit explodes"], 1,
          "Post-measurement wave function collapse fixes the state in |0⟩, so immediate re-measurement yields |0⟩ with 100% probability."),
        q("q-1-7-2", "According to Born's Rule, what is the probability of observing state |1⟩ for state |ψ⟩ = α|0⟩ + β|1⟩?",
          ["|α|", "|β|", "|β|²", "α * β"], 2,
          "Born's rule states P(1) = |β|², the squared magnitude of the amplitude."),
        q("q-1-7-3", "What are repeated circuit executions used to estimate probability distributions on quantum hardware called?",
          ["Shots", "Clocks", "Cycles", "Spins"], 0,
          "In Qiskit and QPU hardware, repeated trial executions are called shots (e.g., 1024 or 4096 shots)."),
        q("q-1-7-4", "Is quantum measurement a deterministic or probabilistic process?",
          ["Deterministic", "Probabilistic (governed by Born's Rule)", "Reversible", "Non-physical"], 1,
          "Quantum measurement is inherently probabilistic, projecting superposition into basis eigenstates."),
        q("q-1-7-5", "What observable measurement basis is standard for Qiskit and IBM QPU hardware?",
          ["X-basis (|+\n, |-⟩)", "Y-basis (|+i⟩, |-i⟩)", "Z-basis computational basis (|0⟩, |1⟩)", "Continuous basis"], 2,
          "Standard QPU hardware measurements take place in the computational Z-basis (|0⟩, |1⟩).")
    ],
    "lesson-1-8": [
        q("q-1-8-1", "What role does an activation function σ(z) play in neural networks?",
          ["Reduces memory usage", "Introduces non-linearity to learn complex non-linear patterns", "Increases training speed", "Converts numbers to binary"], 1,
          "Without non-linear activation functions, stacked neural network layers collapse mathematically into a simple single linear transformation."),
        q("q-1-8-2", "What is the output formula for a single classical artificial neuron with weights w and bias b?",
          ["y = σ(wᵀx + b)", "y = w * x", "y = x / b", "y = w² + x²"], 0,
          "A classical artificial neuron computes y = σ(wᵀx + b)."),
        q("q-1-8-3", "Which loss function is commonly used for binary classification tasks?",
          ["Mean Squared Error (MSE)", "Binary Cross-Entropy (BCE)", "Huber Loss", "L1 Loss"], 1,
          "Binary Cross-Entropy (BCE) measures discrepancy between binary targets and predicted probabilities."),
        q("q-1-8-4", "What does backpropagation calculate in a classical multi-layer neural network?",
          ["Loss function values", "Partial derivatives of loss with respect to weights via chain rule", "Random weights", "Input features"], 1,
          "Backpropagation uses the chain rule to compute exact weight gradients ∂L/∂w."),
        q("q-1-8-5", "In a Hybrid QNN, what layer replaces or augments a classical dense neural layer?",
          ["Parameterized Quantum Circuit (PQC)", "Convolution filter", "Pooling buffer", "Lookup table"], 0,
          "Parameterized Quantum Circuits act as quantum trainable layers embedded inside neural network architectures.")
    ],
    "lesson-1-9": [
        q("q-1-9-1", "Why can classical backpropagation NOT be performed directly on physical quantum hardware?",
          ["Quantum computers are too fast", "The No-Cloning Theorem prevents copying intermediate quantum states during forward pass", "Qubits do not have derivatives", "Classical computers run out of memory"], 1,
          "The No-Cloning Theorem forbids making copies of unknown quantum states, requiring QML hardware to use evaluation methods like the Parameter Shift Rule."),
        q("q-1-9-2", "In gradient descent, what parameter controls the step size taken in the negative gradient direction?",
          ["Learning rate (η)", "Batch size", "Shot count", "Qubit frequency"], 0,
          "The learning rate η scales the step size during parameter updates θ^(t+1) = θ^(t) - η ∇L."),
        q("q-1-9-3", "What vector points in the direction of steepest increase of the loss function L(θ)?",
          ["The Hessian", "The Gradient vector ∇L(θ)", "The Momentum vector", "The Loss scalar"], 1,
          "The gradient vector ∇L points in the direction of steepest loss increase."),
        q("q-1-9-4", "What quantum analytic gradient calculation replaces backpropagation on physical QPUs?",
          ["Parameter-Shift Rule", "Finite Differences with ε=10⁻⁹", "Genetic Mutation", "Simulated Annealing"], 0,
          "The Parameter-Shift Rule evaluates exact gradients by shifting rotation parameters by ±π/2."),
        q("q-1-9-5", "What happens if the learning rate η in gradient descent is set too large?",
          ["The model converges instantly", "The optimizer overshoots the minimum and diverges", "The weights become zero", "The loss decreases monotonically"], 1,
          "An excessively large learning rate causes gradient descent to overshoot minima and oscillate or diverge.")
    ],
    "lesson-1-10": [
        q("q-1-10-1", "What measurement counts distribution do you expect from running a single-qubit Hadamard circuit over 1000 shots?",
          ["1000 shots of 0, 0 shots of 1", "Approximately 500 shots of 0 and 500 shots of 1", "1000 shots of 1", "Random numbers between 0 and 100"], 1,
          "Hadamard creates state |+⟩ with equal 50% probability for 0 and 1, producing roughly equal outcome counts."),
        q("q-1-10-2", "Which Qiskit class is used to create a quantum circuit with q qubits and c classical bits?",
          ["QuantumRegister", "QuantumCircuit(q, c)", "AerSimulator", "QiskitRuntime"], 1,
          "QuantumCircuit(q, c) initializes a circuit register with q qubits and c classical bits."),
        q("q-1-10-3", "What Qiskit code instruction measures qubit 0 into classical bit 0?",
          ["qc.measure(0, 0)", "qc.read(0)", "qc.check(0)", "qc.observe(0)"], 0,
          "qc.measure(0, 0) measures qubit index 0 and stores the result in classical bit index 0."),
        q("q-1-10-4", "Which local simulator in Qiskit simulates noiseless quantum circuits on your local CPU?",
          ["AerSimulator", "IBMHardware", "QPUCloud", "LinuxKernel"], 0,
          "AerSimulator from qiskit_aer provides fast CPU-based state-vector and shot simulation."),
        q("q-1-10-5", "What output format does Qiskit's job.result().get_counts() return?",
          ["A Python dictionary mapping bitstrings to shot frequencies (e.g., {'0': 512, '1': 512})", "A single integer", "A C++ pointer", "A float array"], 0,
          "get_counts() returns a dictionary of outcome bitstrings and their count frequencies.")
    ]
}

print("Phase 1 quizzes prepared successfully.")
