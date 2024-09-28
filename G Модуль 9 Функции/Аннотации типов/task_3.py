def cyclic_shift(numbers: list[int| float], step: int) -> None:
    L = len(numbers)
    numbers[:] = [numbers[(i - step) % L] for i in range(L)]