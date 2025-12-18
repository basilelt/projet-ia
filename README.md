# Connect 4 Game

A Python implementation of the classic Connect 4 game with a graphical user interface. Play against another human or challenge AI opponents with varying difficulty levels using alpha-beta pruning algorithm.

## Prerequisites

- Python 3.14.0 (see `.python-version` file)
- pip (Python package installer)

## Installation

1. **Clone or download the project** to your local machine.

2. **Navigate to the project directory**:
   ```bash
   cd projet-ia
   ```

3. **Install the required dependencies**:
   ```bash
   brew install pyenv  # For macOS users
   brew install tcl-tk   # For macOS users to ensure Tkinter works properly
   
   env LDFLAGS="-L$(brew --prefix openssl@1.1)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix sqlite3)/lib -L$(brew --prefix xz)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix tcl-tk)/lib" \
   CPPFLAGS="-I$(brew --prefix openssl@1.1)/include -I$(brew --prefix readline)/include -I$(brew --prefix sqlite3)/include -I$(brew --prefix xz)/include -I$(brew --prefix zlib)/include -I$(brew --prefix tcl-tk)/include" \
   PKG_CONFIG_PATH="$(brew --prefix openssl@1.1)/lib/pkgconfig:$(brew --prefix readline)/lib/pkgconfig:$(brew --prefix sqlite3)/lib/pkgconfig:$(brew --prefix xz)/lib/pkgconfig:$(brew --prefix zlib)/lib/pkgconfig:$(brew --prefix tcl-tk)/lib/pkgconfig" \
   pyenv install 3.14.0

   python -m venv .venv

   pip install -r requirements.txt
   ```

   This will install:
   - `numpy` - For efficient array operations
   - `tqdm` - For progress bars (used in AI computations)

## Running the Game

To start the Connect 4 game:

```bash
python src/main.py
```

## How to Play

1. Select player types for Player 1 and Player 2:
   - **Human**: Manual player input
   - **AI: alpha-beta level X**: AI opponent with increasing difficulty (1-42)

2. Click the "New game" button to start.

3. Click on a column to drop your piece.

4. The first player to connect 4 pieces horizontally, vertically, or diagonally wins!

## Project Structure

- `src/main.py` - Main GUI application entry point
- `src/Connect4.py` - Game logic and GUI interactions
- `src/Board.py` - Board state management
- `requirements.txt` - Python dependencies
- `sujet/` - Project documentation and skeleton code

## Features

- Graphical user interface using Tkinter
- Human vs Human gameplay
- Human vs AI gameplay with multiple difficulty levels
- AI uses alpha-beta pruning algorithm for optimal play
- Visual feedback for game state and winner announcement