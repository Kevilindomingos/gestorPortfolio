# Personal Portfolio Manager

A command-line application for tracking and managing personal development projects. This project demonstrates practical Python skills including file I/O, data persistence, and iterative feature development based on real-world requirements.

## Features

- **Project Management**: Add, list, update, and delete projects with detailed tracking
- **Persistent Storage**: Automatically saves all projects to JSON format
- **Project Statistics**: View completion metrics and project history
- **Search Functionality**: Find projects by name or keyword
- **Status Tracking**: Mark projects as completed or pending
- **Project History**: Maintains immutable records of all changes made to each project
- **Error Handling**: Robust exception handling for corrupted files and invalid inputs
- **Case-Insensitive Commands**: Flexible command input regardless of case

## Project Structure

```
portfolio-manager/
├── gestor_portfolio.py          # Main application with all functions
├── portfolio.json               # Auto-generated data persistence file
└── diario_de_bordo.md          # Learning journey and development notes
```

## Architecture

### Core Data Model

Each project is stored as a dictionary with the following structure:

```python
{
    "nome": "Project Name",
    "finalizado": False,
    "observacoes": "Project notes",
    "historico": [("Project Name", False), ("Updated Name", True)]
}
```

**Key Components:**
- **nome**: Project name (string)
- **finalizado**: Completion status (boolean)
- **observacoes**: User notes and observations (string)
- **historico**: Immutable tuple records of all state changes (list of tuples)

### File Persistence

- **Format**: JSON (human-readable and parseable)
- **Encoding**: UTF-8 with accent preservation (`ensure_ascii=False`)
- **Error Recovery**: Graceful handling of missing or corrupted files
- **Auto-save**: Saves on exit via QUIT command

## How to Use

### Running the Application

```bash
python gestor_portfolio.py
```

### Command Reference

| Command | Description |
|---------|-------------|
| **ADD** | Add one or more new projects |
| **LIST** | Display all projects with status and notes |
| **UPDATE** | Modify an existing project's details |
| **DELETE** | Remove a project from the list |
| **STATS** | View completion statistics and insights |
| **SEARCH** | Find projects by name or keyword |
| **QUIT** | Save and exit the application |

### Interactive Example

```
=== GESTOR DE PORTFÓLIO PESSOAL ===
ADD    - Adicionar projeto
LIST   - Listar projetos
UPDATE - Atualizar projeto
DELETE - Remover projeto
STATS  - Estatísticas
SEARCH - Buscar termo
QUIT   - Sair

Escolha uma opção: ADD
Nome do projeto: Machine Learning Course
Projeto 'Machine Learning Course' adicionado.

Escolha uma opção: LIST
--- LISTA DE PROJETOS ---
1. Machine Learning Course 
 | Observação: Nenhuma 
 | Status: Pendente
```

## Key Functions

### `carregar_dados()`
Loads projects from `portfolio.json`. Returns empty list if file doesn't exist or is corrupted.

### `salvar_dados()`
Persists the current project list to JSON with proper formatting and UTF-8 encoding.

### `adicionar_projeto()`
Adds a new project with initialization of status, notes, and empty history.

### `listar_projetos()`
Displays all projects with formatted output including status and observations.

### `atualizar_projeto()`
Searches for a project by name and allows modification of name, status, and notes. Records changes in history.

### `remover_projeto()`
Finds and removes a project with confirmation prompt.

### `ver_estatisticas()`
Calculates and displays:
- Number of completed projects
- Number of pending projects
- Average completion rate
- Name of most recently completed project

### `buscar_por_termo()`
Searches projects by keyword (case-insensitive) and displays matching results.

## Data Persistence

### Automatic Saving
```python
# On application exit
elif opcao == "QUIT":
    salvar_dados()
    print("Dados salvos. Até logo!")
    break
```

### Error Recovery
```python
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("\nO arquivo de dados está corrompido.")
        return []
```

## Sample Output

```
--- STATUS GERAL ---
Projetos prontos: 3
Projetos fazendo: 2
Média de finalizados (por mês): 0.75 por semana
Último que você terminou: API Development

--- LISTA DE PROJETOS ---
1. Python Fundamentals 
 | Observação: Completed basic syntax 
 | Status: Finalizado
 | Histórico: [('Python Fundamentals', True)]
----------------------------------------
2. Web Scraping Project 
 | Observação: Using BeautifulSoup 
 | Status: Pendente
 | Histórico: [('Web Scraping', False), ('Web Scraping Project', False)]
```

## Technologies Used

- **Language**: Python 3.x
- **Data Format**: JSON
- **File I/O**: Built-in `json` and file operations
- **Data Structures**: Lists, Dictionaries, Tuples
- **Exception Handling**: Try-except blocks
- **String Operations**: `.upper()`, `.lower()`, `.strip()`, f-strings

## Learning Journey

This project includes a detailed **"Diário de Bordo" (Learning Log)** documenting the development process:

- **20/03/2026**: Introduction to loops (`while`)
- **25/03/2026**: Repeating operations with `for` and `range()`
- **28/03/2026**: Input validation with `isdigit()`
- **01/04/2026**: Business logic validation (preventing invalid inputs)
- **05/04/2026**: Case-insensitive command handling
- **13/04/2026**: Code refactoring and best practices
- **15/04/2026**: Data structure migration (simple list → list of dictionaries)
- **29/04/2026**: File persistence and error handling

Each entry demonstrates problem-solving, research, and progressive skill development.

## Development Evolution

### Version 1.0
- Basic project creation and listing
- Command-line menu structure

### Version 2.0
- Data persistence with JSON
- Error handling for file operations
- Case-insensitive command parsing

### Version 3.0
- Data model refactoring (dictionaries instead of strings)
- Update and delete functionality
- Project history tracking with tuples

### Version 4.0
- Statistics generation
- Search functionality
- Enhanced user feedback and error messages

## Key Learning Outcomes

This project demonstrates proficiency in:

- **File I/O & Persistence**: JSON serialization/deserialization
- **Error Handling**: Try-except patterns and graceful degradation
- **Data Structures**: Strategic use of lists, dictionaries, and tuples
- **Control Flow**: Loops, conditionals, and application flow management
- **Input Validation**: Ensuring data quality and user experience
- **Code Refactoring**: Improving code structure based on requirements
- **Iterative Development**: Adapting features based on real-world needs
- **Documentation**: Maintaining learning records throughout development

## Potential Enhancements

- Add project priority levels
- Implement due dates and reminders
- Export statistics to CSV or PDF
- Add project categories or tags
- Implement project time tracking
- Create a simple web interface (Flask)
- Add data backup functionality

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Author

**Kev** | Data Automation Intern at IBEMA | ADS Student at PUCPR | Systems Development Technician (SENAI)

- 🔗 [LinkedIn](https://linkedin.com/in/kevilin-marcondes)
- 💻 [GitHub](https://github.com/Kevilindomingos)

## License

This project is open source and available under the MIT License.

---

**Project Type**: Educational | **Focus**: Python Fundamentals & Iterative Development | **Status**: ✅ Complete

**Special Note**: This project includes a detailed learning journal ("Diário de Bordo") documenting the development journey, making it an excellent example of thoughtful, documented learning progression.
