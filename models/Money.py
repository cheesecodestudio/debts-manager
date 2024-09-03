class Money:
    def __init__(self,pIngresos,pGastos,pRestante,pMovimientos):
        self.incomes=pIngresos
        self.expenses=pGastos
        self.balance=pRestante
        self.movements=pMovimientos


class Movement:
    def __init__(self,pTipo,pMonto,pTipoMovimiento):
        self.type=pTipo
        self.amount=pMonto
        self.typeMovement=pTipoMovimiento