from collections import defaultdict
from datetime import datetime


class MonthlyTransactionSummaryProjection:
	def __init__(self):
		self.monthly_summary = defaultdict(lambda: {"deposits": 0.0, "withdrawals": 0.0, "count": 0})

	def apply(self, event):
		event_month = event.timestamp.strftime("%Y-%m")
		if event.type == "DepositMade":
			self.monthly_summary[event_month]["deposits"] += event.amount
		elif event.type == "WithdrawalMade":
			self.monthly_summary[event_month]["withdrawals"] += event.amount
		self.monthly_summary[event_month]["count"] += 1

	def get_monthly_summary(self):
		return dict(self.monthly_summary)
