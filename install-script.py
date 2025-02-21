Conversación abierta. 1 mensaje leído.

Ir al contenido
Uso de Gmail con lectores de pantalla
in:sent 
Habilita las notificaciones de escritorio para Gmail.
   Aceptar  No, gracias
1 de 137
aaaa

jorge armando escobar correa <jorgesiemprearmando@gmail.com>
Adjuntos
16:26 (hace 13 minutos)
para jorgeescobaruber


 1 archivo adjunto
•  Analizado por Gmail
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

    if sys.platform.startswith("linux"):
        run_command("sudo apt update")
        run_command("sudo apt install -y zsh")
    elif sys.platform == "darwin":
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

    # Verificar que la instalación fue exitosa
    if not os.path.exists(os.path.expanduser("~/.oh-my-zsh/oh-my-zsh.sh")):
        print("Error: Oh My Zsh no se instaló correctamente.")
        sys.exit(1)

def customize_zshrc():
    """Sobrescribe el archivo .zshrc con una nueva configuración."""
    print("Personalizando .zshrc...")

    zshrc_file = os.path.expanduser("~/.zshrc")
    
    new_zshrc_content = """# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load
ZSH_THEME="gnzh"

# Load plugins
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

# User configuration
# Add your custom aliases and settings below
"""

    with open(zshrc_file, "w") as file:
        file.write(new_zshrc_content)

    print(".zshrc actualizado correctamente.")

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
    try:
        zsh_path = subprocess.check_output("which zsh", shell=True).decode().strip()
        run_command(f"chsh -s {zsh_path}")
        print("Shell cambiado a Zsh. Reinicia tu terminal para aplicar los cambios.")
    except subprocess.CalledProcessError:
        print("Error: No se pudo cambiar el shell. Intenta hacerlo manualmente con 'chsh -s $(which zsh)'.")

def apply_changes():
    """Informa al usuario que debe aplicar los cambios manualmente."""
    print("Instalación completa. Para aplicar los cambios, ejecuta:")
    print("  source ~/.zshrc")
    print("O reinicia la terminal para que los cambios surtan efecto.")

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


