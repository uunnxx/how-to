class AbstractEntity:
    pass


class Tenant(AbstractEntity):
    def __init__(self, tenant_id: str | None) -> None:
        self.tenant_id = tenant_id

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(other, Tenant):
            return False
        return self.tenant_id == other.tenant_id

    def __repr__(self) -> str:
        return f"""Tenant({self.tenant_id=})
        """
