from typing import Any

class BaseReporter:
    def starting(self) -> Any: ...
    def starting_round(self, index: int) -> Any: ...
    def ending_round(self, index: int, state: Any) -> Any: ...
    def ending(self, state: Any) -> Any: ...
    def adding_requirement(self, requirement: Any, parent: Any) -> Any: ...
    def backtracking(self, candidate: Any) -> Any: ...
    def resolving_conflicts(self, causes: Any) -> Any: ...
    def pinning(self, candidate: Any) -> Any: ...
