
import os
import subprocess
import sys

def run_command(command):
    """Ejecuta un comando en la terminal y maneja posibles errores."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando el comando: {e}")
        sys.exit(1)

def install_zsh():
    """Instala Zsh dependiendo del sistema operativo."""
    print("Instalando Zsh...")

    if sys.platform == "linux" or sys.platform == "linux2":
        # Para distribuciones basadas en Debian/Ubuntu
        run_command("sudo apt update")
        run_command("sudo apt install -y zsh")
    elif sys.platform == "darwin":
        # Para macOS
        if not is_homebrew_installed():
            print("Homebrew no está instalado. Instalando Homebrew...")
            run_command('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        run_command("brew install zsh")
    else:
        print("Sistema operativo no soportado para esta instalación automatizada.")
        sys.exit(1)

def is_homebrew_installed():
    """Verifica si Homebrew está instalado."""
    try:
        subprocess.check_call("which brew", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_oh_my_zsh():
    """Instala Oh My Zsh."""
    print("Instalando Oh My Zsh...")
    run_command('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

def customize_zshrc():
    """Personaliza el archivo .zshrc."""
    print("Personalizando .zshrc...")

    # Cambiar el tema
    zshrc_file = os.path.expanduser("~/.zshrc")
    with open(zshrc_file, "r") as file:
        zshrc_content = file.read()

    zshrc_content = zshrc_content.replace('ZSH_THEME="robbyrussell"', 'ZSH_THEME="agnoster"')
    zshrc_content = zshrc_content.replace('plugins=(git)', 'plugins=(git zsh-autosuggestions zsh-syntax-highlighting)')

    with open(zshrc_file, "w") as file:
        file.write(zshrc_content)

def install_plugins():
    """Instala los plugins zsh-autosuggestions y zsh-syntax-highlighting."""
    print("Instalando plugins zsh-autosuggestions y zsh-syntax-highlighting...")

    zsh_custom = os.environ.get("ZSH_CUSTOM", os.path.expanduser("~/.oh-my-zsh/custom"))
    plugins = {
        "zsh-autosuggestions": "https://github.com/zsh-users/zsh-autosuggestions.git",
        "zsh-syntax-highlighting": "https://github.com/zsh-users/zsh-syntax-highlighting.git"
    }

    for plugin, repo in plugins.items():
        plugin_path = os.path.join(zsh_custom, "plugins", plugin)
        if not os.path.exists(plugin_path):
            run_command(f'git clone {repo} {plugin_path}')
        else:
            print(f"El plugin {plugin} ya está instalado en {plugin_path}")

def change_shell_to_zsh():
    """Cambia el shell por defecto a Zsh."""
    print("Cambiando el shell predeterminado a Zsh...")
    run_command(f"chsh -s {subprocess.check_output('which zsh', shell=True).decode().strip()}")

def apply_changes():
    """Aplica los cambios en .zshrc."""
    print("Aplicando cambios en .zshrc...")
    run_command(". ~/.zshrc")


def main():
    """Función principal para ejecutar todas las tareas."""
    install_zsh()
    install_oh_my_zsh()
    customize_zshrc()
    install_plugins()
    change_shell_to_zsh()
    apply_changes()
    print("¡Instalación y personalización de Zsh completada!")

if __name__ == "__main__":
    main()
