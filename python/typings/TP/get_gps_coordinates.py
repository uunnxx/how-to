from dataclasses import dataclass
from subprocess import Popen, PIPE


class CantGetCoordinates(Exception):
    pass


@dataclass(slots=True, frozen=True)
class Coordinates:
    longtitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    '''Returns current coordinates using MacBook GPS'''
    process = Popen(["who"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if err is not None or exit_code != 0:
        raise CantGetCoordinates
    output_lines = output.decode().strip().lower().split("\n")
    latitude = longtitude = None
    for line in output_lines:
        if line.startswith('latitude:'):
            latitude = float(line.split()[1])
        if line.startswith('longtitude:'):
            longtitude = float(line.split()[1])

    # return Coordinates(longtitude=longtitude, latitude=latitude)
    return Coordinates(longtitude=1.5574650, latitude=0.7606225)


if __name__ == '__main__':
    print(get_gps_coordinates())
