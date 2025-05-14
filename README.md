# 🚀 Automatic Zsh Installation and Customization  

This script automates the installation, configuration, and customization of **Zsh** on **Linux** and **macOS** systems. It also installs **Oh My Zsh** and essential plugins to enhance your terminal experience.

![Visual Example](screeshoots/visualexample.png)

---

## ✅ Requirements

- `curl`
- `git`
- Python 3
- Administrator access (`sudo`) on Linux
- [Homebrew](https://brew.sh/) (for macOS)

---

## ⚙️ Features

This script automates the following:

1. **Zsh Installation**  
   Detects the operating system (Linux or macOS) and installs Zsh accordingly.

2. **Oh My Zsh Installation**  
   Downloads and installs the **Oh My Zsh** framework for easier shell customization.

3. **Environment Customization**  
   Creates a `.zshrc` file with advanced settings, visual enhancements, extended history, and more.

4. **Essential Plugins Setup**  
   Installs and configures:
   - `zsh-autosuggestions`: auto-suggests previous commands.
   - `zsh-syntax-highlighting`: highlights command syntax in real time.

5. **Change Default Shell**  
   Sets **Zsh** as the default shell for the current user.

---

## 🧪 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/jorgearma/zsh-customization-scripts.git
   cd zsh-customization-scripts
   ```

2. Run the script:
   ```bash
   python3 kali-shell-zsh.py
   ```

3. If a new terminal window opens during installation, type `exit` to continue.

4. Restart your terminal and make sure you are using **Zsh**:
   ```bash
   echo $SHELL
   ```
   If it doesn't contain "zsh", run:
   ```bash
   chsh -s $(which zsh)
   ```

5. ⚠️ **Not seeing syntax colors or suggestions?**  
   Make sure these packages are installed:
   ```bash
   sudo apt install zsh-syntax-highlighting zsh-autosuggestions
   ```

---

## 📝 Script Actions

- Installs Zsh using `apt` (Linux) or `brew` (macOS).
- Installs **Oh My Zsh** from its official repository.
- Overwrites `.zshrc` with a configuration inspired by **Kali Linux**.
- Installs plugins to improve usability.
- Sets Zsh as the default shell (restart terminal or session might be needed).

---

## 🛠️ Troubleshooting

- On macOS, Homebrew will be installed automatically if not found.
- If the shell change doesn't take effect, run:
  ```bash
  chsh -s $(which zsh)
  ```

---

## 📜 License

This project is licensed under the **GNU General Public License (GPL v2 or later)**, the same license used by the Linux kernel.

The `.zshrc` file is based on the one from **Kali Linux**, with additional automation and improvements by me. It maintains the original structure but has been adapted for multi-platform deployment.

More info:  
👉 [https://www.gnu.org/licenses/gpl-2.0.html](https://www.gnu.org/licenses/gpl-2.0.html)