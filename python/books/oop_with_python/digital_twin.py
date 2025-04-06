class Machine:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.working: bool = False

    def start(self):
        self.working = True
        print(f"{self.name} started.")

    def stop(self):
        self.working = False
        print(f"{self.name} stopped.")


class ManufacturingPlannt:
    def __init__(self):
        self.machines: list[Machine] = []

    def add_machine(self, machine: Machine):
        self.machines.append(machine)

    def start_production(self):
        for machine in self.machines:
            machine.start()

    def stop_production(self):
        for machine in self.machines:
            machine.stop()


# Usage
machine1: Machine = Machine('Machine1')
machine2: Machine = Machine('Machine2')

plant = ManufacturingPlannt()

plant.add_machine(machine1)
plant.add_machine(machine2)

plant.start_production()

# Output:
# Machine 1 started
# Machine 2 started

plant.stop_production()

# Output.
# Machine 1 stopped.
# Machine 2 stopped.
