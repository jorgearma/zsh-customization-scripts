# Instalación y Personalización Automática de Zsh

Este script automatiza la instalación y personalización de Zsh en sistemas Linux y macOS. Además, instala **Oh My Zsh** y varios plugins útiles para mejorar la experiencia de uso de Zsh.

## Requisitos
- curl
- git
- Python 3
- Acceso de administrador (sudo) en Linux
- Homebrew (si usas macOS)

## Funcionalidad

1. **Instala Zsh**: Dependiendo del sistema operativo (Linux o macOS).
2. **Instala Oh My Zsh**: Un framework de configuración para Zsh.
3. **Personaliza `.zshrc`**: Crea un archivo `.zshrc` con configuración básica.
4. **Instala plugins**: Incluye los plugins `zsh-autosuggestions` y `zsh-syntax-highlighting`.
5. **Cambia el shell a Zsh**: Cambia el shell predeterminado a Zsh.

## Uso

1. Clona este repositorio o descarga el archivo.
2. Ejecuta el script en tu terminal:
    ```bash
    git clone https://github.com/jorgearma/zsh-customization-scripts.git
    ```
    ```bash
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

Este proyecto está bajo la licencia MIT.
