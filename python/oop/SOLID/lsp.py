class KitchenAppliance:
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self):
        pass


class Toaster(KitchenAppliance):
    def on(self):
        # some code to turn on toaster
        pass

    def off(self):
        # some code to turn off toaster
        pass

    def set_temperature(self):
        # some code to set temp on toaster
        pass


class Juicer(KitchenAppliance):
    def on(self):
        # some code to turn on juicer
        pass

    def off(self):
        # some code to turn off juicer
        pass

    def set_temperature(self):
        # some code to set temp on toaster
        pass


# the correct way
class KitchenAppliance2:
    def on(self):
        pass

    def off(self):
        pass


class KitchenApplianceWithTemp2(KitchenAppliance2):
    def set_temperature(self):
        pass


class Toaster2(KitchenApplianceWithTemp2):
    def on(self):
        pass
        # some code to turn on toaster

    def off(self):
        pass
        # some code to turn off toaster

    def set_temperature(self):
        pass
        # some code to set temp on toaster

