from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="atlas-cluster", collection="Motorista")
motoristaDAO = MotoristaDAO(database=db)


motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()