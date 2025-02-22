from pycalc.parsing.types import (
    Instruction,
    ConstantInstruction,
    BinaryOperation,
    OperationType,
    UnaryOperation,
    ConstantType,
)


class Evaluator:
    def __init__(self, expression: Instruction):
        self.expression = expression

    def _evaluate(self, instruction: Instruction) -> float | int:
        if isinstance(instruction, ConstantInstruction):
            if instruction.constant_type == ConstantType.FLOAT:
                return float(instruction.value)
            else:
                return int(instruction.value)
        elif isinstance(instruction, BinaryOperation):
            if instruction.op_type == OperationType.ADDITION:
                return self._evaluate(instruction.left) + self._evaluate(
                    instruction.right
                )
            elif instruction.op_type == OperationType.MULTIPLICATION:
                return self._evaluate(instruction.left) * self._evaluate(
                    instruction.right
                )
            elif instruction.op_type == OperationType.SUBTRACTION:
                return self._evaluate(instruction.left) - self._evaluate(
                    instruction.right
                )
            elif instruction.op_type == OperationType.DIVISION:
                return self._evaluate(instruction.left) / self._evaluate(
                    instruction.right
                )
            raise RuntimeError("Invalid operation type", instruction.op_type)

        elif isinstance(instruction, UnaryOperation):
            if instruction.op_type == OperationType.SUBTRACTION:
                return -self._evaluate(instruction.operand)
            raise RuntimeError("Invalid operation type", instruction.op_type)

    def evaluate(self):
        return self._evaluate(self.expression)
