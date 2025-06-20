# Basic Image Processing Operations in Python

This repository contains a collection of Python scripts, each designed to perform a specific image processing operation. The scripts are located in the `assignment1/` directory and are run from the command line.

## Features

The repository includes scripts for the following tasks:

*   **Task 1:** Reduce the number of intensity levels in an image.
*   **Task 2:** Apply a spatial average filter with different kernel sizes.
*   **Task 3:** Rotate an image by 45 and 90 degrees.
*   **Task 4:** Reduce spatial resolution by averaging non-overlapping blocks.

## Project Structure

The repository is organized as follows:

```
.
├── assignment1/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   └── task4.py
├── requirements.txt      # Project dependencies
├── README.md             # This is the documentation file
└── sample.jpg            # An example image to use with the tasks
```

## Setup

### Prerequisites
*   Python 3.7+
*   `pip` package manager

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/TharinduGee/ComputerVision.git
    cd ComputerVision
    ```

2.  **(Recommended) Create and Activate a Virtual Environment**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    From the root directory of the project, run:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Scripts

To run a task, execute its corresponding Python script from the **root directory** of the repository. The scripts will prompt you for any required inputs.

---

### Example (Task 1: Reduce Intensity Levels)

This script reduces the number of intensity levels in an image to a power of 2 (e.g., 2, 4, 8).

**To Run:**
```bash
python assignment1/task1.py
```
**Prompts:**
1.  Enter the path to the input image (e.g., `sample.jpg`).
2.  Enter the desired number of intensity levels (e.g., `4`).

The processed image will be displayed and saved in the root project directory.

