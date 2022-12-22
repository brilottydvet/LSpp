from LsPrePost import execute_command


class DupNod:
    def __init__(self, tolerance: float = 0.0) -> None:
        self.tolerance = tolerance

    def show_dup_nodes(self) -> None:
        execute_command(f"dupnode showdup {self.tolerance}")

    def select_nodes(self) -> None:
        pass

    def merge_dup_nodes(self) -> None:
        execute_command(f"dupnode merge {self.tolerance}")
        execute_command("genselect clear")
        execute_command("dupnode accept")

    def clear(self) -> None:
        pass