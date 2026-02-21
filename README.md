# High School Physics Tutoring Materials

Welcome to the High School Physics Curriculum Repository! This repository contains specially curated physical science learning materials designed for high school students. All materials are written in LaTeX to ensure professional and highly readable equation formatting.

## Curriculum Navigation

The repository is structured logically by physics units. Click the links below to navigate directly to the respective files.

### [`unit_1_kinematics`](./high_school_physics/unit_1_kinematics) (Unit 1: Kinematics)

- **`notes/` : Lecture Notes & Handouts**
  - [x] [`kinematics_basic.tex`](./high_school_physics/unit_1_kinematics/notes/kinematics_basic.pdf) - Fundamentals of Kinematics (includes displacement, $v-t$ graphs, and the Big Five uniform acceleration equations).
  - [x] [`kinematics_two_dimensional.tex`](./high_school_physics/unit_1_kinematics/notes/kinematics_two_dimensional.pdf) - Introduction to 2D Projectile Motion.
  - [x] [`kinematics_circular.tex`](./high_school_physics/unit_1_kinematics/notes/kinematics_circular.pdf) - Basic concepts of Kinematics in Circular Motion.

- **`practice/` : Problem Sets & Worksheets**
  - [ ] [`kinematics_pset_1.tex`](./high_school_physics/unit_1_kinematics/practice/kinematics_pset_1.pdf) - *TODO:* Focus on basic concepts (scalar vs. vector, average vs. instantaneous) and $v-t$ graph interpretation.
  - [ ] [`kinematics_pset_2.tex`](./high_school_physics/unit_1_kinematics/practice/kinematics_pset_2.pdf) - *TODO:* Focus on direct applications of the "Big Five" equations and 1D free-fall problems.
  - [x] [`kinematics_pset_3.tex`](./high_school_physics/unit_1_kinematics/practice/kinematics_pset_3.pdf) - Advanced Kinematics problem set (covering catch-up scenarios, multi-stage motion, and 2D projectile calculations).

### [`unit_2_dynamics`](./high_school_physics/unit_2_dynamics) (Unit 2: Dynamics & Circular Motion)

- **`notes/` : Lecture Notes & Handouts**
  - [x] [`force.tex`](./high_school_physics/unit_2_dynamics/notes/force.pdf) - Fundamentals of Forces and Free-Body Diagrams (Normal force, Tension, Friction).
  - [x] [`newtons_laws.tex`](./high_school_physics/unit_2_dynamics/notes/newtons_laws.pdf) - Newton's Three Laws of Motion: Concepts and Applications.
  - [x] [`circular_dynamics.tex`](./high_school_physics/unit_2_dynamics/notes/circular_dynamics.pdf) - Circular Dynamics Notes (Defining Centripetal Force, identifying "the role", banked curves, and vertical circular motion).

- **`practice/` : Problem Sets & Worksheets**
  - [x] [`circular_dynamics_examples.tex`](./high_school_physics/unit_2_dynamics/practice/circular_dynamics_examples.pdf) - Guided Examples Handout (Features blank spaces for students to fill out during lecture).
  - [x] [`circular_dynamics_pset_1.tex`](./high_school_physics/unit_2_dynamics/practice/circular_dynamics_pset_1.tex) - Problem Set 1: Horizontal Circular Motion and Friction.
  - [x] [`circular_dynamics_pset_2.tex`](./high_school_physics/unit_2_dynamics/practice/circular_dynamics_pset_2.tex) - Problem Set 2: Angled Forces (Conical Pendulums) and Vertical Circular Motion (Rollercoasters).

---

## Compilation Guide

All notes and problem sets are standard LaTeX source files.
It is recommended to compile them using `pdflatex`:

```bash
pdflatex your_file_name.tex
```

## Quick Workspace Cleanup

Generating PDFs leaves behind multiple auxiliary logs. A `Makefile` is provided in the root directory to help maintain a clean workspace. In your terminal, simply run:

```bash
make clean
```

This command automatically finds and deletes all `.aux`, `.log`, `.synctex.gz`, and other temporary files generated during LaTeX compilation throughout the entire repository, leaving only your `.tex` source code and the clean `.pdf` outputs.
