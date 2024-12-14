from bank_account.v4.projections.base_projection import BaseProjection


class ProjectionManager:
    def __init__(self):
        self.projections = []

    def register_projection(self, projection):
        if not isinstance(projection, BaseProjection):
            raise TypeError("Projection must inherit from BaseProjection")
        self.projections.append(projection)

    def project(self, event):
        for projection in self.projections:
            projection.project(event)