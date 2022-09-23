from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    test_brazilian_files = read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    )
    assert test_brazilian_files[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee"
    }
    assert test_brazilian_files[5] == {
        "title": "Auxiliar usinagem",
        "salary": "1400",
        "type": " full time"
    }
    assert test_brazilian_files[10] == {
        "title": "Esportista de Futebol profissional",
        "salary": "50000",
        "type": " full time"
    }
