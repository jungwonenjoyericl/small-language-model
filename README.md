# Small Language Model

## Setup

Run the commands below from the project root (the folder containing `requirements.txt`).
The virtual environment keeps this project's dependencies separate from other Python projects.

### Windows (PowerShell)

Install Python if needed, then check that the Python launcher is available:

```powershell
py --version
```

Create the environment, activate it, and install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Arch Linux (Bash or Zsh)

If Python is not installed, install it while updating the system:

```bash
sudo pacman -Syu python
```

Create the environment, activate it, and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For more details, see the [ArchWiki virtual environment guide](https://wiki.archlinux.org/title/Python/Virtual_environment).

## Working with the environment

Create the environment once. Each time you open a new terminal, activate it again
from the project root:

| Shell | Activation command |
| --- | --- |
| PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Bash / Zsh | `source .venv/bin/activate` |

To deactivate it in either shell:

```text
deactivate
```

Keep `.venv/` in `.gitignore`. Commit `requirements.txt` so others can recreate
the environment. After dependencies change, run `python -m pip install -r requirements.txt`
again with the environment active.

