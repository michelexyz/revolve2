class ActorControl:
    """Interface for controlling degrees of freedom of actors in a simulation."""

    _dof_targets: list[tuple[int, list[float]]]  # actor, targets

    def __init__(self) -> None:
        """Initialize this object."""
        self._dof_targets = []

    def set_dof_targets(self, actor: int, targets: list[float]) -> None:
        """
        Set the degrees of freedom of an actor.

        :param actor: The actor to control.
        :param targets: The targets to set.
        """
        self._dof_targets.append((actor, targets))
