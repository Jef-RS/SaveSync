import pytest
from pathlib import Path
import os

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[: -len('Backe')]

def test_project_folders():
    # Caminho para o diretório raiz do seu projeto
    project_path = Path(diretório_raiz)

    # Lista das pastas principais do projeto
    main_folders = ['Backend', 'Frontend', 'tests']

    # Verifica se cada pasta principal existe no diretório raiz
    for folder in main_folders:
        assert (project_path / folder).exists()

if __name__ == '__main__':
    pytest.main([__file__])
