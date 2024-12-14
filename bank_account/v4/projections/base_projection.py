from abc import ABC, abstractmethod


class BaseProjection:
	@abstractmethod
	def project(self, event):
		raise NotImplementedError("Subclasses must implement this method")