#Data structures for the VHDL parser

class component:
	
	def __init__(self, arg_identifier='', arg_inSignals=[], arg_outSignals=[]):
		self.identifier = arg_identifier
		self.inSignals = arg_inSignals
		self.outSignals = arg_outSignals
		
class signal:

	def __init__(self, arg_identifier='', arg_type='', arg_leftLinks=[], arg_rightLinks=[]):
		self.identifier = arg_identifier
		self.type = arg_type
		self.leftLinks = arg_leftLinks
		self.rightLinsk = arg_rightLinks
		
class signalAssignment:

	def __init__(self, arg_LHS='', arg_RHS='', arg_Dir='forward'):
		self.left = arg_LHS
		self.right = arg_RHS
		self.direction = arg_Dir
		
class portMap:
	
	def __init__(self, arg_identifier='', arg_componentName='', arg_signalAssignments=[]):
		self.identifier = arg_identifier
		self.componentName = arg_componentName
		self.signalAssignments = arg_signalAssignments
		