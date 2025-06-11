# dRAGan
## Agente de consulta a Documentos impulsada por IA con técnica RAG
--- 
## ⭕ Instrucciones de Ejecución

De momento la ejecución del Agente se realiza por medio local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/c4mdax/dragan-agent-rag.git
cd dragan-agent-rag
```

### 2. Instalar Ollama (gestor de LLM)
#### Debian (y derivados)
```bash
sudo apt update
sudo apt install -y curl
curl -fsSL https://ollama.com/install.sh | bash
```

#### Fedora
```bash
sudo dnf install -y curl
curl -fsSL https://ollama.com/install.sh | bash
```

#### Arch Linux (y derivados)
```bash
sudo pacman -Syu curl
curl -fsSL https://ollama.com/install.sh | bash
```

### 3. Descargar y activar el LLM (Phi 3 Mini)
```bash
ollama pull phi3:mini
```
Una vez instalado el LLM, ejecútalo
```bash
ollama serve
```

### 4. Instalar dependencias Python
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el script para automatizar la ejecución
```bash
chmod +x dragan
```
## ⭕ Instrucciones de Ejecución

Puedes probar descargando archivos PDF o TXT (.txt) relacionados a un tema en específico, guardándolos en una carpeta misma.
Para ejecutar **dRAGan**, ejecuta
```bash
./dragan ~/ruta/a/documentos "Pregunta"
```
Reemplazando _~/ruta/a/documentos_ con la ruta que contiene los archivos PDF/TXT, y _Pregunta_ con la pregunta específica.

##### Ejemplo de uso
```bash
./dragan ~/Documentos/prueba_dragan "¿Qué es la Tuberculosis?"
```
