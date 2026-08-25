class Pessoa:
    especie = "Humano"

    @classmethod
    def especie_da_classe(cls):
        return f"Somos da espécie {cls.especie}"


print(Pessoa.especie_da_classe())
