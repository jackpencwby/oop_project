from ..internal.Bank import Bank
from ..internal.CreditCard import CreditCard

scb = Bank("scb")
kbank = Bank("kbank")

scb.add_account_id("200100")
scb.add_credit_card(CreditCard("30100","400",10000))
scb.add_paypal_id("5001000")

kbank.add_account_id("200101")