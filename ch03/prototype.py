import copy


class Website:
    def __init__(
        self,
        name: str,
        domain: str,
        description: str,
        **kwargs,
    ):
        self.name = name
        self.domain = domain
        self.description = description

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self) -> str:
        summary = [
            f"- {self.name} (ID: {id(self)})\n",
        ]

        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == "name":
                continue
            summary.append(f"{attr}: {val}\n")

        return "".join(summary)


class Prototype:
    def __init__(self):
        self.registry = {}

    def register(self, identifier: int, obj: object):
        self.registry[identifier] = obj

    def unregister(self, identifier: int):
        del self.registry[identifier]

    def clone(self, identifier: int, **attrs) -> object:
        found = self.registry.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = (
        "python",
        "programming",
        "scripting",
        "data",
        "automation",
    )
    site1 = Website(
        "Python",
        domain="python.org",
        description="Programming language and ecosystem",
        category="Open Source Software",
        keywords=keywords,
    )

    proto = Prototype()
    proto.register("python-001", site1)

    site2 = proto.clone(
        "python-001",
        name="Python Package Index",
        domain="pypi.org",
        description="Repository for published packages",
        category="Open Source Software",
    )

    for site in (site1, site2):
        print(site)


if __name__ == "__main__":
    main()
