
class make_Calculations:
    quantity=0
    AMPL_USDT=0
    AMPL_ETH=0
    ETH_USDT=0
    AMPL_account="5f2340b16ce385000791808e"
    ETH_account="5c6a49fb99a1d819392efda9"
    USDT_account="5c6a49fb99a1d819392efda9"
    def __init__(self, quantidade, verify_AMPL_USDT, verify_AMPL_ETH, verify_ETH_USDT):
        super().__init__()
        self.quantity = quantidade
        self.AMPL_USDT = verify_AMPL_USDT
        self.AMPL_ETH = verify_AMPL_ETH
        self.ETH_USDT = verify_ETH_USDT
    
    def calc_USDT_ETH_AMPL_USDT(self):
        cs = self.quantity
        first = self.quantity
        for i in range(10):
            s = cs/self.ETH_USDT
            s1 = s-(s*0.001)
            b = s1/self.AMPL_ETH
            b1 = b-(b*0.001)
            c = b1*self.AMPL_USDT
            c1 = c-(c*0.001)
            cs = c1
        return cs-first
    
    def calc_USDT_AMPL_ETH_USDT(self):  
        cs = self.quantity
        first = self.quantity   
        for i in range(10):
            s = cs/self.AMPL_USDT
            s1 = s-(s*0.001)
            b = s1*self.AMPL_ETH
            b1 = b-(b*0.001)
            c = b1*self.ETH_USDT
            c1 = c-(c*0.001)
            cs = c1
        return cs-first


