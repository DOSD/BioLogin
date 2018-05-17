from pymongo.mongo_client import MongoClient
import datetime

class Resultado():

    t_pulsado = []
    t_vuelo = []
    usuario = ""

    def toTuple(self):
        return (self.v1, self.v2, self.isEven(), 
                self.isZero(), self.digitNumber(), 
                self.carryOn(), self.ellapsed)
    
    def predict(self, model):
        self.prediction = model.predict([self.toTuple()[:-1]])[0]

    def save(self):
        if usuario == "Noel":
            target = 0
        else:
            target = 1
        biolog = {
            "T": self.t_pulsado[0],
            "r": self.t_pulsado[1],
            "e": self.t_pulsado[2],
            "s": self.t_pulsado[3],
            "_1": self.t_pulsado[4],
            "t": self.t_pulsado[5],
            "r": self.t_pulsado[6],
            "i": self.t_pulsado[7],
            "s": self.t_pulsado[8],
            "t": self.t_pulsado[9],
            "e": self.t_pulsado[10],
            "s": self.t_pulsado[11],
            "_2": self.t_pulsado[12],
            "t": self.t_pulsado[13],
            "i": self.t_pulsado[14],
            "g": self.t_pulsado[15],
            "r": self.t_pulsado[16],
            "e": self.t_pulsado[17],
            "s": self.t_pulsado[18],
            "T_r": self.t_vuelo[0],
            "r_e": self.t_vuelo[1],
            "e_s": self.t_vuelo[2],
            "s_": self.t_vuelo[3],
            "_t": self.t_vuelo[4],
            "t_r": self.t_vuelo[5],
            "r_i": self.t_vuelo[6],
            "i_s": self.t_vuelo[7],
            "s_t": self.t_vuelo[8],
            "t_e": self.t_vuelo[9],
            "e_s": self.t_vuelo[10],
            "s_": self.t_vuelo[11],
            "_t": self.t_vuelo[12],
            "t_i": self.t_vuelo[13],
            "i_g": self.t_vuelo[14],
            "g_r": self.t_vuelo[15],
            "r_e": self.t_vuelo[16],
            "e_s": self.t_vuelo[17],
            "usuario":  target
        }

        client = MongoClient('localhost', 27017)
        db = client['myDB']
        collection = db["biologin"]
        collection.insert_one(biolog)




