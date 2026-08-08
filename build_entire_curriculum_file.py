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

phases_data = []

phases_meta = [
    (1, "Quantum Computing Foundations", "Qubits, Linear Algebra, Gates & Classical ML Bridge", "Atom", "Master single/multi-qubit mathematics, superposition, entanglement, Pauli transformations, measurement collapse, and classical gradient descent."),
    (2, "Algorithms & Noisy Quantum Neighbors", "Quantum Circuits, Speedups & NISQ Hardware Realities", "Cpu", "Explore Deutsch-Jozsa, Grover's Search, QFT, Shor's algorithm, hardware noise channels (T1/T2), zero-noise extrapolation, and Qiskit transpilation."),
    (3, "Quantum Gym Bros Pumping Tensors (Core QML)", "PQCs, Variational Algorithms, Kernels & Gradients", "Flame", "Build Parameterized Quantum Circuits, Amplitude/Angle Embeddings, VQE, QAOA, Quantum SVMs, QNNs, Parameter-Shift gradients, and Barren Plateau mitigations."),
    (4, "Ascension to the Multiverse (Advanced Sorcery)", "QGANs, QCNNs, Quantum RL, Topological QC & Cloud Execution", "Sparkles", "Master QGANs, QCNNs, Quantum Reinforcement Learning, Hardware-Efficient Ansätze, Quantum Chemistry, Financial QML, Topological Anyons, and Cloud API deployment.")
]

lesson_titles_map = {
    1: ["Qubits & Two-Level Systems", "Superposition & Linear Algebra", "Entanglement & Bell States", "Quantum Gates & Matrices", "Single-Qubit Rotations (Rx, Ry, Rz)", "The Bloch Sphere Representation", "Measurement & Wave Function Collapse", "Classical ML Refresher (Neurons & Loss)", "Gradient Descent & Optimization", "Quantum 'Hello World' with Qiskit"],
    2: ["Quantum Circuits & Multi-Qubit Registers", "Quantum Interference", "Deutsch-Jozsa Algorithm", "Grover's Search Algorithm", "Quantum Fourier Transform (QFT)", "Shor's Factoring Algorithm", "The NISQ Era & Quantum Volume", "Decoherence & Noise Channels (T1, T2)", "Error Mitigation & ZNE", "Hardware Execution & Qiskit Transpiler"],
    3: ["Parameterized Quantum Circuits (PQCs)", "Data Encoding & Feature Maps", "Variational Quantum Eigensolver (VQE)", "Quantum Approximate Optimization (QAOA)", "Quantum Support Vector Machines (QSVM)", "Quantum Neural Networks (QNNs)", "Quantum Kernels & Hilbert Spaces", "Parameter-Shift Rule", "Barren Plateaus & Trainability", "Hybrid Classical-Quantum Architectures"],
    4: ["Quantum Generative Adversarial Networks (QGANs)", "Quantum Convolutional Neural Networks (QCNNs)", "Quantum Reinforcement Learning (QRL)", "Hardware-Efficient Ansätze (HEA)", "Quantum Chemistry Applications (VQE/UCCSD)", "Financial Modeling with QML (QAE/QUBO)", "Benchmarking QML Models & Expressibility", "Topological Quantum Computing (Anyons)", "Cloud Deployment & API Integration", "The Capstone Project"]
}

for pid, ptitle, psub, picon, pdesc in phases_meta:
    lessons = []
    titles = lesson_titles_map[pid]
    for idx, lt in enumerate(titles):
        lid = f"lesson-{pid}-{idx+1}"
        q_list = all_quizzes.get(lid, [])
        
        challenge = None
        if idx == 9:
            challenge = {
                "id": f"challenge-{pid}-10",
                "title": f"Challenge: Phase {pid} Capstone Script",
                "instructions": f"Write Qiskit Python code implementing the core algorithm for {lt}.",
                "initialCode": f"from qiskit import QuantumCircuit\n\n# Initialize circuit for {lt}\nqc = QuantumCircuit(2, 2)\nqc.h(0)\nqc.cx(0, 1)\nqc.measure([0,1], [0,1])\n",
                "expectedOutput": "Execution returned valid shot counts across quantum registers.",
                "solutionHint": "Run qc.draw() or execute on AerSimulator.",
                "validationFnType": "hadamard_superposition"
            }

        lesson_obj = {
            "id": lid,
            "phaseId": pid,
            "title": f"{idx+1}. {lt}",
            "duration": f"{15 + idx*2} mins",
            "xpReward": 100 + idx*15,
            "description": f"Master the core mathematical and computational principles of {lt}.",
            "content": f"### Introduction to {lt}\nIn this module, we explore the theoretical foundations and practical applications of **{lt}** in quantum information science and machine learning.\n\n### Key Concepts\n- Mathematical formulation in complex Hilbert space $\\mathbb{{C}}^n$\n- Quantum circuit implementation via Qiskit & PennyLane\n- Practical deployment considerations on NISQ hardware and GPU simulators.\n\n$$|\\psi\\rangle = \\sum_{{i}} \\alpha_i |i\\rangle \\quad \\text{{where }} \\sum |\\alpha_i|^2 = 1$$",
            "keyFormula": f"|\\psi\\rangle_{{m}} = U(\\theta) |\\psi\\rangle_0 \\quad \\text{{for }} {lt}",
            "quiz": q_list
        }
        if challenge:
            lesson_obj["codingChallenge"] = challenge
        lessons.append(lesson_obj)

    phase_obj = {
        "id": pid,
        "title": ptitle,
        "subtitle": psub,
        "icon": picon,
        "description": pdesc,
        "lessons": lessons,
        "interphasoryQuiz": make_interphasory_quiz(pid)
    }
    phases_data.append(phase_obj)

ts_content = f"""import {{ Phase, LeaderboardUser, Badge }} from '../types';

export const ALL_BADGES: Badge[] = [
  {{
    id: 'badge-1',
    title: 'Quantum Novice',
    description: 'Unlocked by joining QML Academy and completing the onboarding tour.',
    icon: 'Atom',
    unlockedAt: '2025-01-15'
  }},
  {{
    id: 'badge-2',
    title: 'Quantum Apprentice',
    description: 'Mastered Phase 1 Foundations & Superposition.',
    icon: 'Award',
    unlockedAt: '2025-02-01'
  }},
  {{
    id: 'badge-3',
    title: 'Quantum Architect',
    description: 'Built variational circuits and parameterized QML models.',
    icon: 'Cpu',
    unlockedAt: '2025-02-20'
  }},
  {{
    id: 'badge-4',
    title: 'Quantum Sorcerer',
    description: 'Achieved mastery across all 4 Phases of Quantum Machine Learning.',
    icon: 'Sparkles'
  }}
];

export const QISKIT_TEMPLATES = [
  {{
    id: 'bell-state',
    name: 'Bell State |Φ+⟩',
    description: 'Creates maximally entangled two-qubit Bell pair using H and CNOT gates.',
    code: 'from qiskit import QuantumCircuit\\n\\n# Create a circuit with 2 qubits and 2 classical bits\\nqc = QuantumCircuit(2, 2)\\n\\n# Put qubit 0 into superposition\\nqc.h(0)\\n\\n# Entangle qubit 0 and qubit 1\\nqc.cx(0, 1)\\n\\n# Measure both qubits\\nqc.measure([0, 1], [0, 1])\\n'
  }},
  {{
    id: 'grover-2qubit',
    name: 'Grover Search (2 Qubits)',
    description: 'Demonstrates quadratic speedup for finding target state |11⟩.',
    code: 'from qiskit import QuantumCircuit\\n\\nqc = QuantumCircuit(2, 2)\\n\\n# Step 1: Uniform superposition\\nqc.h([0, 1])\\n\\n# Step 2: Oracle for |11⟩ (Controlled-Z)\\nqc.cz(0, 1)\\n\\n# Step 3: Diffusion operator\\nqc.h([0, 1])\\nqc.z([0, 1])\\nqc.cz(0, 1)\\nqc.h([0, 1])\\n\\n# Step 4: Measurement\\nqc.measure([0, 1], [0, 1])\\n'
  }},
  {{
    id: 'vqe-ansatz',
    name: 'Parameterized VQE Ansatz',
    description: 'Hardware-efficient Ry-CZ variational circuit with trainable angles.',
    code: 'from qiskit import QuantumCircuit\\nimport numpy as np\\n\\ntheta = [0.2, 0.8, 1.2, 0.5]\\nqc = QuantumCircuit(2, 2)\\n\\n# Parameterized rotations\\nqc.ry(theta[0], 0)\\nqc.ry(theta[1], 1)\\nqc.cz(0, 1)\\nqc.ry(theta[2], 0)\\nqc.ry(theta[3], 1)\\n\\nqc.measure([0, 1], [0, 1])\\n'
  }}
];

export const CURRICULUM_PHASES: Phase[] = {json.dumps(phases_data, indent=2)};

export const MOCK_LEADERBOARD: LeaderboardUser[] = [
  {{
    rank: 1,
    id: 'user-1',
    name: 'Alice Vance',
    email: 'alice.vance@mit.edu',
    username: '@alice_quantum',
    avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&q=80&w=150',
    xp: 4850,
    streak: 14,
    badgeTitle: 'Quantum Sorcerer',
    country: 'United States',
    mobile: '+1 2025550143',
    phaseScores: {{
      1: 3000,
      2: 1850
    }}
  }},
  {{
    rank: 2,
    id: 'user-2',
    name: 'Bob',
    email: 'bob@gmail.com',
    username: '@bob',
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=150',
    xp: 2800,
    streak: 7,
    badgeTitle: 'Quantum Apprentice',
    country: 'United States',
    mobile: '+1 9876543210',
    phaseScores: {{
      1: 2800
    }}
  }},
  {{
    rank: 3,
    id: 'user-3',
    name: 'Shaik Arif',
    email: 'shaikarif@gmail.com',
    username: '@shaikarif',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&q=80&w=150',
    xp: 2100,
    streak: 5,
    badgeTitle: 'Quantum Architect',
    country: 'India',
    mobile: '+91 9876543210',
    phaseScores: {{
      1: 2100
    }}
  }},
  {{
    rank: 4,
    id: 'user-4',
    name: 'Carol Danvers',
    email: 'carol@stanford.edu',
    username: '@carol_qml',
    avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&q=80&w=150',
    xp: 1920,
    streak: 4,
    badgeTitle: 'Quantum Apprentice',
    country: 'Canada',
    mobile: '+1 4165550192',
    phaseScores: {{
      1: 1920
    }}
  }},
  {{
    rank: 5,
    id: 'user-5',
    name: 'David Kim',
    email: 'dkim@kaist.ac.kr',
    username: '@david_kim',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&q=80&w=150',
    xp: 1450,
    streak: 3,
    badgeTitle: 'Quantum Novice',
    country: 'South Korea',
    mobile: '+82 1012345678',
    phaseScores: {{
      1: 1450
    }}
  }}
];
"""

with open('src/data/curriculumData.ts', 'w', encoding='utf-8') as f:
    f.write(ts_content)

print("src/data/curriculumData.ts successfully compiled with QISKIT_TEMPLATES!")
