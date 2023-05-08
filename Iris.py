class Iris:
    def __init__(self, vector, v_type, distance, belongsto):
        self.vector = vector
        self.v_type = v_type
        self.distance = distance
        self.belongsto = belongsto

    def setbelongsto(self, newcentroid):
        self.belongsto = newcentroid

    def __str__(self):
        return f"vector: {self.vector}, belongs to: {self.belongsto}"
