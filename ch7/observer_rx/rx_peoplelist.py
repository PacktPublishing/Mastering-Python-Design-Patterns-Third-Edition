from pathlib import Path
import reactivex as rx
from reactivex import operators as ops


def firstnames_from_db(path: Path):
    file = path.open()

    # collect and push stored people firstnames
    return rx.from_iterable(file).pipe(
        ops.flat_map(
            lambda content: rx.from_iterable(
                content.split(", ")
            )
        ),
        ops.filter(lambda name: name != ""),
        ops.map(lambda name: name.split()[0]),
        ops.group_by(lambda firstname: firstname),
        ops.flat_map(
            lambda grp: grp.pipe(
                ops.count(),
                ops.map(lambda ct: (grp.key, ct)),
            )
        ),
    )


def main():
    db_path = Path(__file__).parent / Path("people.txt")

    # Emit data every 5 seconds
    rx.interval(5.0).pipe(
        ops.flat_map(lambda i: firstnames_from_db(db_path))
    ).subscribe(lambda val: print(str(val)))

    # Keep alive until user presses any key
    input("Starting... Press any key and ENTER, to quit\n")


if __name__ == "__main__":
    main()
