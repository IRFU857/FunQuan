import json
from patch_curriculum import make_interphasory_quiz
from generate_all_curriculum import p1_quizzes
from enrich_all_lessons import p2_quizzes, p3_quizzes
from generate_final_curriculum_ts import p4_quizzes

all_quizzes = {}
all_quizzes.update(p1_quizzes)
all_quizzes.update(p2_quizzes)
all_quizzes.update(p3_quizzes)
all_quizzes.update(p4_quizzes)

# Define full phase titles, subtitles, icons, and descriptions
phases_info = [
    {
        "id": 1,
        "title": "Quantum Computing Foundations",
        "subtitle": "Qubits, Linear Algebra, Gates & Classical ML Bridge",
        "icon": "Atom",
        "description": "Master single/multi-qubit mathematics, superposition, entanglement, Pauli transformations, measurement collapse, and classical gradient descent."
    },
    {
        "id": 2,
        "title": "Algorithms & Noisy Quantum Neighbors",
        "subtitle": "Quantum Circuits, Speedups & NISQ Hardware Realities",
        "icon": "Cpu",
        "description": "Explore Deutsch-Jozsa, Grover's Search, QFT, Shor's algorithm, hardware noise channels (T1/T2), zero-noise extrapolation, and Qiskit transpilation."
    },
    {
        "id": 3,
        "title": "Quantum Gym Bros Pumping Tensors (Core QML)",
        "subtitle": "PQCs, Variational Algorithms, Kernels & Gradients",
        "icon": "Flame",
        "description": "Build Parameterized Quantum Circuits, Amplitude/Angle Embeddings, VQE, QAOA, Quantum SVMs, QNNs, Parameter-Shift gradients, and Barren Plateau mitigations."
    },
    {
        "id": 4,
        "title": "Ascension to the Multiverse (Advanced Sorcery)",
        "subtitle": "QGANs, QCNNs, Quantum RL, Topological QC & Cloud Execution",
        "icon": "Sparkles",
        "description": "Master QGANs, QCNNs, Quantum Reinforcement Learning, Hardware-Efficient Ansätze, Quantum Chemistry, Financial QML, Topological Anyons, and Cloud API deployment."
    }
]

# Define titles for 10 lessons per phase
lesson_titles = [
    # Phase 1
    ["1. Qubits & Two-Level Systems", "2. Superposition & Linear Algebra", "3. Entanglement & Bell States", "4. Quantum Gates & Matrices", "5. Single-Qubit Rotations (Rx, Ry, Rz)", "6. The Bloch Sphere Representation", "7. Measurement & Wave Function Collapse", "8. Classical ML Refresher (Neurons & Loss)", "9. Gradient Descent & Optimization", "10. Quantum 'Hello World' with Qiskit"],
    # Phase 2
    ["1. Quantum Circuits & Multi-Qubit Registers", "2. Quantum Interference", "3. Deutsch-Jozsa Algorithm", "4. Grover's Search Algorithm", "5. Quantum Fourier Transform (QFT)", "6. Shor's Factoring Algorithm", "7. The NISQ Era & Quantum Volume", "8. Decoherence & Noise Channels (T1, T2)", "9. Error Mitigation & ZNE", "10. Hardware Execution & Qiskit Transpiler"],
    # Phase 3
    ["1. Parameterized Quantum Circuits (PQCs)", "2. Data Encoding & Feature Maps", "3. Variational Quantum Eigensolver (VQE)", "4. Quantum Approximate Optimization (QAOA)", "5. Quantum Support Vector Machines (QSVM)", "6. Quantum Neural Networks (QNNs)", "7. Quantum Kernels & Hilbert Spaces", "8. Parameter-Shift Rule", "9. Barren Plateaus & Trainability", "10. Hybrid Classical-Quantum Architectures"],
    # Phase 4
    ["1. Quantum Generative Adversarial Networks (QGANs)", "2. Quantum Convolutional Neural Networks (QCNNs)", "3. Quantum Reinforcement Learning (QRL)", "4. Hardware-Efficient Ansätze (HEA)", "5. Quantum Chemistry Applications (VQE/UCCSD)", "6. Financial Modeling with QML (QAE/QUBO)", "7. Benchmarking QML Models & Expressibility", "8. Topological Quantum Computing (Anyons)", "9. Cloud Deployment & API Integration", "10. The Capstone Project"]
]

print("Script template ready")
