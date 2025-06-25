# selenium-grid-selector

## Project Overview
This project is designed to automate the selection of items from a grid on a specified webpage using Selenium WebDriver. It provides a simple interface to interact with the grid and select items based on their identifiers.

## Project Structure
```
selenium-grid-selector
├── src
│   ├── main.py
│   └── selectors
│       └── grid_selector.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd selenium-grid-selector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Open `src/main.py` to configure the target webpage and item identifiers.
2. Run the script:
   ```
   python src/main.py
   ```

## Functionality
- The `GridSelector` class in `src/selectors/grid_selector.py` provides methods to:
  - `select_item(item_id)`: Selects an item from the grid using its identifier.
  - `get_items()`: Retrieves a list of all items currently available in the grid.

## Requirements
- Python 3.x
- Selenium

## License
This project is licensed under the MIT License.