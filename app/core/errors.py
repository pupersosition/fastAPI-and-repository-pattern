class RepositoryError(Exception):
    """Base exception class for repository errors."""
    def __init__(self, detail: str):
        super().__init__(detail)
        self.detail = detail
class NotFoundError(RepositoryError):
    """Raised when an item is not found in the repository."""

class CreateError(RepositoryError):
    """Raised when an item creation in the repository fails."""

class UpdateError(RepositoryError):
    """Raised when an item update in the repository fails."""

class DeleteError(RepositoryError):
    """Raised when an item deletion in the repository fails."""