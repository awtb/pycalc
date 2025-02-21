from pycalc.parsing.types import Instruction, ConstantInstruction, BinaryOperation, OperationType, UnaryOperation


class Evaluator:
    def __init__(self, expression: Instruction):
        self.expression = expression


    def _evaluate(self, instruction: Instruction) -> float:
        if isinstance(instruction, ConstantInstruction):
            return float(instruction.value)
        elif isinstance(instruction, BinaryOperation):
            if instruction.op_type == OperationType.ADDITION:
                return self._evaluate(instruction.left) + self._evaluate(instruction.right)
            elif instruction.op_type == OperationType.MULTIPLICATION:
                return self._evaluate(instruction.left) * self._evaluate(instruction.right)
            elif instruction.op_type == OperationType.SUBTRACTION:
                return self._evaluate(instruction.left) - self._evaluate(instruction.right)
            elif instruction.op_type == OperationType.DIVISION:
                return self._evaluate(instruction.left) / self._evaluate(instruction.right)

        elif isinstance(instruction, UnaryOperation):
            return -float(self._evaluate(instruction.operand))

    def evaluate(self):
        return self._evaluate(self.expression)