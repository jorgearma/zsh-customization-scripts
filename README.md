# Instalación y Personalización Automática de Zsh  

Este script facilita la instalación y configuración de **Zsh** en sistemas **Linux** y **macOS**. Además, incorpora **Oh My Zsh** junto con varios complementos útiles para optimizar la experiencia de uso del terminal.


## Requisitos
- curl
- git
- Python 3
- Acceso de administrador (sudo) en Linux
- Homebrew (si usas macOS)

## Funcionalidad

Este script automatiza la instalación y configuración de Zsh con las siguientes características:

1. **Instalación de Zsh**: Verifica y instala Zsh según el sistema operativo (Linux o macOS).  
2. **Configuración de Oh My Zsh**: Descarga e instala Oh My Zsh, un framework que facilita la personalización del shell.  
3. **Personalización del entorno**: Genera un archivo `.zshrc` con configuraciones predeterminadas, incluyendo mejoras en la experiencia de usuario.  
4. **Instalación de plugins esenciales**: Agrega y configura los plugins `zsh-autosuggestions` (sugerencias automáticas de comandos) y `zsh-syntax-highlighting` (resaltado de sintaxis).  
5. **Cambio del shell predeterminado**: Configura Zsh como el shell por defecto para el usuario actual.  

Con esta configuración, Zsh tendrá un entorno más productivo y fácil de usar, con soporte para autocompletado avanzado y resaltado de sintaxis.  


## Uso

1. Clona este repositorio o descarga el archivo.
2. Ejecuta el script en tu terminal:
    ```bash
    git clone https://github.com/jorgearma/zsh-customization-scripts.git
    
    cd zsh-customization-scripts
    ```
    ```bash
    python3 kali-shell-zsh.py
    ```

3. ⚠️ Si no tienes Oh My Zsh instalado, escribe `exit` en la consola cuando se abra.
4. reinicia la terminal y asegúrate de estar en zsh para que los cambios surtan efecto.

## Pasos realizados por el script

- **Instalación de Zsh**:
    - En Linux, utiliza `apt` para instalar Zsh.
    - En macOS, usa `Homebrew` (se instalará automáticamente si no está presente).
  
- **Instalación de Oh My Zsh**: Se instala desde el repositorio oficial.

- **Personalización de `.zshrc`**: Se configura el tema `gnzh` y se habilitan los plugins `git`, `zsh-syntax-highlighting`, y `zsh-autosuggestions`.

- **Cambio de shell predeterminado**: Configura Zsh como el shell predeterminado, pidiendo al usuario reiniciar la terminal.

## Problemas comunes

- Si no tienes `Homebrew` en macOS, el script lo instalará automáticamente.
- Si el cambio de shell a Zsh no se aplica, intenta usar manualmente `chsh -s $(which zsh)`.

## Licencia

Este proyecto está licenciado bajo la **Licencia Pública General de GNU (GPLv2 o posterior)**, la misma utilizada por el kernel de Linux.  

El archivo `./zshrc` proviene de la distribución Kali Linux y se mantiene bajo su licencia original. La automatización y los cambios realizados para agregar control de versiones con Git fueron hechos por mí, pero el contenido base sigue siendo de Kali Linux.  

Para más información sobre la GPL, puedes consultar:  
[https://www.gnu.org/licenses/gpl-2.0.html](https://www.gnu.org/licenses/gpl-2.0.html)  
