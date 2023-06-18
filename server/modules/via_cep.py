import requests

class Via_cep:
    def __init__(self, cep:int):
        print("via_cep.py -> Via_cep.__init__")
        self.cep = cep
        self.end = None
        self.set_end()
    
    def set_end(self) -> None:
        self.buscar_cep()

    def get_end(self) -> dict:
        return self.end

    def buscar_cep(self) -> None:
        url = "http://viacep.com.br/ws/"+str(self.cep)+"/json/"
        r = requests.get(url)
        self.end = r.json()